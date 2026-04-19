#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CodeReview.py - CodeReview 이슈 관리 헬퍼

조회:
  python CodeReview.py stats
  python CodeReview.py list include [--status 미결|해결] [--priority P1] [--reason include]

파일 조작 (이동/삭제, 추론 없음):
  python CodeReview.py clean-output           # Output 삭제
  python CodeReview.py drop-resolve           # Output [해결] 삭제
  python CodeReview.py move-resolve           # Include,Exclude [해결] → Resolve
  python CodeReview.py make-workers           # Include P0-P1 → 작업자별 파일 재생성
  python CodeReview.py push-minority          # Output P2-P3 [미결] → Minority 맨위
"""

import re
import sys
import argparse
from pathlib import Path
from datetime import date

# ─── 경로 ─────────────────────────────────────────────────────────────────────
WRK_DIR  = Path(__file__).resolve().parent.parent
INCLUDE  = WRK_DIR / "CodeReview_Include.md"
EXCLUDE  = WRK_DIR / "CodeReview_Exclude.md"
RESOLVE  = WRK_DIR / "CodeReview_Resolve.md"
MINORITY = WRK_DIR / "CodeReview_Minority.md"
_FIXED   = {p.name for p in (INCLUDE, EXCLUDE, RESOLVE, MINORITY)}

PRIORITY_LABEL = {
    "P0": "P0:Critical", "P1": "P1:High",
    "P2": "P2:Medium",   "P3": "P3:Low", "P4": "P4:Minimal",
}

# ANSI
R="\033[91m"; Y="\033[93m"; G="\033[92m"; B="\033[94m"
CY="\033[96m"; DIM="\033[2m"; RST="\033[0m"

# ─── I/O ──────────────────────────────────────────────────────────────────────
def read_md(path: Path) -> str:
    if not path.exists():
        return ""
    for enc in ("utf-8-sig", "utf-8", "cp949"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")

def write_md(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8-sig")

# ─── 파싱 ─────────────────────────────────────────────────────────────────────
_STATUS_RE  = re.compile(r'상태 : \[(미결|해결)\]')
_RISK_RE    = re.compile(r'위험 : (\d+)')
_REASON_RE  = re.compile(r'^- 사유 : (.*)$', re.MULTILINE)
_HEAD_RE    = re.compile(r'^#### (\[(P(\d)):[^\]]+\]\[([^\]]*)\]\[[^\]]*\]\[[^\]]*\])')
_SECTION_RE = re.compile(r'^## (P\d:[A-Za-z]+) - \d{4}/\d{2}/\d{2}')

# 이슈 필수 구성요소 검증 (list 표시용)
_CODE_RE    = re.compile(r'```')
_DETAIL_RE  = re.compile(r'<details>.*?</details>', re.DOTALL)
_DESC_RE    = re.compile(r'- 설명 :')
_OPINION_RE = re.compile(r'- 의견 :')

def validate_issue(raw: str) -> list:
    missing = []
    lines = raw.splitlines()
    if len(lines) < 2 or not lines[1].strip():
        missing.append("한줄요약")
    if not _CODE_RE.search(raw):
        missing.append("코드블록")
    if not _DETAIL_RE.search(raw):
        missing.append("<details>")
    else:
        if not _DESC_RE.search(raw):    missing.append("설명")
        if not _OPINION_RE.search(raw): missing.append("의견")
        if not _STATUS_RE.search(raw):  missing.append("상태")
    return missing

class Issue:
    __slots__ = ('key','priority','author','status','risk','reason','raw')
    def __init__(self, key, priority, author, status, risk, reason, raw):
        self.key=key; self.priority=priority; self.author=author
        self.status=status; self.risk=risk; self.reason=reason; self.raw=raw

def parse_issues(content: str) -> list:
    lines = content.splitlines()
    n = len(lines)
    issues, i = [], 0
    while i < n:
        line = lines[i]
        if _SECTION_RE.match(line):
            i += 1; continue
        hm = _HEAD_RE.match(line)
        if not hm:
            i += 1; continue
        bracket  = hm.group(1)
        priority = "P" + hm.group(3)
        author   = hm.group(4) or ''
        key      = "#### " + bracket
        block, i, in_code = [line], i+1, False
        while i < n:
            l = lines[i]
            if l.strip().startswith("```"): in_code = not in_code
            if not in_code and (_HEAD_RE.match(l) or _SECTION_RE.match(l)): break
            block.append(l); i += 1
        while block and not block[-1].strip(): block.pop()
        raw    = '\n'.join(block)
        sm     = _STATUS_RE.search(raw)
        rm     = _RISK_RE.search(raw)
        rsm    = _REASON_RE.search(raw)
        status = sm.group(1) if sm else '미결'
        risk   = int(rm.group(1)) if rm else 0
        reason = rsm.group(1) if rsm else ''
        issues.append(Issue(key, priority, author, status, risk, reason, raw))
    return issues

def extract_file_header(content: str) -> str:
    result = []
    for line in content.splitlines(keepends=True):
        s = line.rstrip()
        if _HEAD_RE.match(s) or _SECTION_RE.match(s): break
        result.append(line)
    return ''.join(result).rstrip('\n')

# ─── 파일 재구성 ──────────────────────────────────────────────────────────────
def _group_by_priority(issues: list) -> dict:
    groups: dict = {}
    for iss in issues:
        groups.setdefault(iss.priority, []).append(iss)
    return groups

def _render_groups(groups: dict) -> list:
    today = date.today().strftime("%Y/%m/%d")
    parts = []
    for prio in sorted(groups):
        parts.append(f"## {PRIORITY_LABEL.get(prio, prio)} - {today}\n")
        for iss in sorted(groups[prio], key=lambda x: x.risk, reverse=True):
            parts.append(iss.raw); parts.append("")
    return parts

def build_sorted(issues: list, header: str = "") -> str:
    parts = [header, ""] if header else []
    parts.extend(_render_groups(_group_by_priority(issues)))
    return '\n'.join(parts).rstrip('\n') + '\n'

def prepend_issues(path: Path, new_issues: list) -> int:
    """파일 맨위에 추가 (중복 제외, 기존 내용 유지)"""
    if not new_issues: return 0
    content    = read_md(path)
    exist_keys = {i.key for i in parse_issues(content)}
    to_add     = [i for i in new_issues if i.key not in exist_keys]
    if not to_add: return 0
    new_block   = '\n'.join(_render_groups(_group_by_priority(to_add)))
    file_header = extract_file_header(content)
    rest        = content[len(file_header):].lstrip('\n') if file_header else content
    combined    = (file_header + '\n\n' + new_block + '\n' + rest) if file_header else (new_block + '\n' + rest)
    write_md(path, combined.rstrip('\n') + '\n')
    return len(to_add)

def merge_sorted_issues(path: Path, new_issues: list) -> int:
    """파일에 병합 후 중요도>위험도 정렬 (중복 key는 new_issues로 덮어씀)"""
    if not new_issues: return 0
    content    = read_md(path)
    existing   = parse_issues(content)
    new_keys   = {i.key for i in new_issues}
    kept       = [i for i in existing if i.key not in new_keys]
    write_md(path, build_sorted(new_issues + kept, extract_file_header(content)))
    return len(new_issues)

# ─── 유틸 ─────────────────────────────────────────────────────────────────────
def get_all_outputs() -> list:
    return sorted(WRK_DIR.glob("CodeReview_????????_*.md"))

def get_latest_output() -> Path | None:
    outputs = get_all_outputs()
    return outputs[-1] if outputs else None

def get_worker_files() -> list:
    return [f for f in WRK_DIR.glob("CodeReview_*.md")
            if f.name not in _FIXED and not re.match(r'CodeReview_\d{8}_', f.name)]

def resolve_path(name: str) -> Path:
    aliases = {"include":INCLUDE, "exclude":EXCLUDE, "resolve":RESOLVE,
               "minority":MINORITY, "output":get_latest_output()}
    lo = name.lower()
    if lo in aliases and aliases[lo]: return aliases[lo]
    p = Path(name)
    if p.exists(): return p
    p2 = WRK_DIR / name
    return p2 if p2.exists() else WRK_DIR / name

# ─── 조회 명령 ────────────────────────────────────────────────────────────────
def cmd_stats(args):
    files = {"Include":INCLUDE, "Exclude":EXCLUDE, "Resolve":RESOLVE, "Minority":MINORITY}
    out = get_latest_output()
    if out: files[f"Output({out.name[:23]})"] = out
    print(f"\n{'파일':<38} {'미결':>5} {'해결':>5} {'합계':>5}")
    print("─" * 58)
    for label, path in files.items():
        if not path or not path.exists():
            print(f"  {DIM}{label:<36}{RST}  (없음)"); continue
        issues  = parse_issues(read_md(path))
        pending = sum(1 for i in issues if i.status == '미결')
        solved  = sum(1 for i in issues if i.status == '해결')
        pcnt: dict = {}
        for i in issues:
            if i.status == '미결': pcnt[i.priority] = pcnt.get(i.priority, 0) + 1
        detail = "  " + " ".join(f"{k}:{v}" for k,v in sorted(pcnt.items())) if pcnt else ""
        print(f"  {B}{label:<36}{RST} {R}{pending:>5}{RST} {G}{solved:>5}{RST} {len(issues):>5}  {DIM}{detail}{RST}")
    print()

def cmd_list(args):
    path = resolve_path(args.file)
    if not path.exists():
        print(f"파일 없음: {path}"); return
    issues = parse_issues(read_md(path))
    if args.status:   issues = [i for i in issues if i.status == args.status]
    if args.priority: issues = [i for i in issues if i.priority == args.priority.upper()]
    if args.reason:   issues = [i for i in issues if args.reason.lower() in i.reason.lower()]
    pending = sum(1 for i in issues if i.status == '미결')
    solved  = sum(1 for i in issues if i.status == '해결')
    print(f"\n{B}[{path.name}]{RST}  미결:{R}{pending}{RST}  해결:{G}{solved}{RST}  합계:{len(issues)}\n")
    cur_prio = None
    for iss in sorted(issues, key=lambda x: (x.priority, -x.risk)):
        if iss.priority != cur_prio:
            cur_prio = iss.priority
            print(f"  {CY}── {PRIORITY_LABEL.get(iss.priority, iss.priority)} ──{RST}")
        sc  = R if iss.status == '미결' else G
        rc  = R if iss.risk >= 80 else (Y if iss.risk >= 50 else DIM)
        tag = f" {G}[Include]{RST}" if '[Include]' in iss.reason else \
              (f" {DIM}[Exclude]{RST}" if '[Exclude]' in iss.reason else "")
        missing = validate_issue(iss.raw)
        warn    = f" {R}⚠ 누락:{','.join(missing)}{RST}" if missing else ""
        print(f"  {sc}[{iss.status}]{RST} {rc}{iss.risk:2d}{RST}  {iss.key[6:]}{tag}{warn}")
    print()

# ─── 파일 조작 명령 ────────────────────────────────────────────────────────────
def cmd_clean_output(args):
    targets = get_all_outputs() + sorted(
        f for f in WRK_DIR.glob("CodeReview_????????.md") if f.name not in _FIXED
    )
    if not targets:
        print(f"{G}clean-output 완료{RST}"); return
    obj_dir = WRK_DIR / "obj"
    obj_dir.mkdir(exist_ok=True)
    keep = max(targets, key=lambda f: f.stat().st_mtime)
    for f in targets:
        if f == keep:
            print(f"  유지: {f.name}"); continue
        f.rename(obj_dir / f.name); print(f"  이동: {f.name} → obj/")
    print(f"{G}clean-output 완료{RST}")

def cmd_move_resolve(args):
    ic = read_md(INCLUDE); ii = parse_issues(ic)
    ec = read_md(EXCLUDE); ei = parse_issues(ec)
    inc_resolve   = [i for i in ii if i.status == '해결']
    inc_remaining = [i for i in ii if i.status != '해결']
    exc_resolve   = [i for i in ei if i.status == '해결']
    exc_remaining = [i for i in ei if i.status != '해결']
    resolve = inc_resolve + exc_resolve
    if not resolve:
        print("Include/Exclude에 [해결] 이슈 없음"); return
    content     = read_md(RESOLVE)
    file_header = extract_file_header(content)
    rest        = content[len(file_header):].lstrip('\n') if file_header else content
    new_block   = '\n'.join(_render_groups(_group_by_priority(resolve)))
    combined    = (file_header + '\n\n' + new_block + '\n' + rest) if file_header else (new_block + '\n' + rest)
    write_md(RESOLVE, combined.rstrip('\n') + '\n')
    if inc_resolve:
        write_md(INCLUDE, build_sorted(inc_remaining, extract_file_header(ic)))
    if exc_resolve:
        write_md(EXCLUDE, build_sorted(exc_remaining, extract_file_header(ec)))
    print(f"{G}[해결] {len(resolve)}건 → Resolve 맨위 누적 (Include: {len(inc_resolve)}, Exclude: {len(exc_resolve)}){RST}")

def cmd_make_workers(args):
    issues = [i for i in parse_issues(read_md(INCLUDE))
              if i.priority in ('P0','P1') and i.status == '미결' and i.author]
    workers: dict = {}
    for iss in issues:
        workers.setdefault(iss.author, []).append(iss)
    for f in get_worker_files():
        f.unlink(); print(f"  삭제(Worker): {f.name}")
    if not workers:
        print("작성자 정보 있는 P0-P1 [미결] 이슈 없음"); return
    for author, w_issues in workers.items():
        wp = WRK_DIR / f"CodeReview_{author}.md"
        write_md(wp, build_sorted(w_issues))
        print(f"  {wp.name}: {len(w_issues)}건 ({', '.join(i.priority for i in w_issues)})")
    print(f"{G}make-workers 완료{RST}")

def cmd_push_minority(args):
    out = get_latest_output()
    if not out: print(f"{R}Output 없음{RST}"); return
    low = [i for i in parse_issues(read_md(out))
           if i.status == '미결' and i.priority in ('P2','P3')]
    if not low:
        print("Output에 P2-P3 [미결] 이슈 없음"); return
    content     = read_md(MINORITY)
    file_header = extract_file_header(content)
    rest        = content[len(file_header):].lstrip('\n') if file_header else content
    new_block   = '\n'.join(_render_groups(_group_by_priority(low)))
    combined    = (file_header + '\n\n' + new_block + '\n' + rest) if file_header else (new_block + '\n' + rest)
    write_md(MINORITY, combined.rstrip('\n') + '\n')
    print(f"{G}P2-P3 {len(low)}건 → Minority 맨위 누적{RST}")
    mc = read_md(MINORITY); mi = parse_issues(mc)
    if len(mi) > 1000:
        # 파일 상단 = 최신 (prepend 방식). 재정렬 없이 1001번째 이슈 직전에서 절단
        lines = mc.splitlines(keepends=True)
        count = cut = 0
        for idx, line in enumerate(lines):
            if _HEAD_RE.match(line.rstrip()):
                count += 1
                if count > 1000:
                    cut = idx
                    while cut > 0 and (not lines[cut-1].strip() or
                                       _SECTION_RE.match(lines[cut-1].rstrip())):
                        cut -= 1
                    break
        if cut:
            write_md(MINORITY, ''.join(lines[:cut]).rstrip('\n') + '\n')
        print(f"  Minority: {len(mi)}건 → 1000건 (오래된 {len(mi)-1000}건 삭제)")

def cmd_drop_resolve(args):
    out = get_latest_output()
    if not out: print(f"{R}Output 없음{RST}"); return
    oc = read_md(out); oi = parse_issues(oc)
    remaining = [i for i in oi if i.status == '미결']
    dropped   = len(oi) - len(remaining)
    if not dropped:
        print("Output에 [해결] 이슈 없음"); return
    write_md(out, build_sorted(remaining, extract_file_header(oc)))
    print(f"{G}Output에서 [해결] {dropped}건 삭제{RST}")

# ─── 메인 ─────────────────────────────────────────────────────────────────────
def main():
    if sys.platform == "win32":
        import os; os.system("")
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    p = argparse.ArgumentParser(
        description="CodeReview 이슈 관리 헬퍼",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="파일 별칭: include, exclude, resolve, minority, output")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("stats", help="전체 현황").set_defaults(func=cmd_stats)

    pl = sub.add_parser("list", help="이슈 목록")
    pl.add_argument("file")
    pl.add_argument("--status", choices=["미결","해결"])
    pl.add_argument("--priority")
    pl.add_argument("--reason")
    pl.set_defaults(func=cmd_list)

    sub.add_parser("clean-output",   help="Output·Worker 삭제, Minority 1000개 제한"  ).set_defaults(func=cmd_clean_output)
    sub.add_parser("move-resolve",  help="Include [해결] → Resolve"                  ).set_defaults(func=cmd_move_resolve)
    sub.add_parser("push-minority", help="Output P2-P3 [미결] → Minority 맨위"        ).set_defaults(func=cmd_push_minority)
    sub.add_parser("make-workers",  help="Include P0-P1 → 작업자별 Worker 파일"       ).set_defaults(func=cmd_make_workers)
    sub.add_parser("drop-resolve",  help="Output에서 [해결] 삭제"                     ).set_defaults(func=cmd_drop_resolve)

    args = p.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
