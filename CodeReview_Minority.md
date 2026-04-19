## P2:Medium - 2026/04/19

#### [P2:Header pollution][정훈희][5af0c3a][Test.h/global/Line:5]
[원인] 헤더에 using namespace std 전역 오염
```cpp
using namespace std;
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `Test.h`에서 `using namespace std;`를 전역 네임스페이스에 선언. 이 헤더를 포함하는 모든 소스가 std 네임스페이스를 강제로 끌어와 이름 충돌 위험 증가.
  <br><br>- 의견 : 헤더에서 `using namespace std;` 제거하고 필요 시 소스 파일에서만 선언하거나 `std::` 접두어 명시.
  <br><br>- 기타 : `<iostream>`은 포함되어 있으나 본 헤더에서 사용처 없음. 헤더 자체의 필요성 재검토 필요.
 </details>

#### [P2:Missing return][정훈희][3136b89][Test.cpp/main()/Line:19-26]
[원인] int main 반환값 누락
```cpp
int main()
{
	int* pM = nullptr;

	printf("T2 %d.\n ", 123);

	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 30, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int main()` 블록 끝에 `return` 문 없음. C++ 표준상 `main`은 암묵적으로 0을 반환하지만 명시적 반환 권장.
  <br><br>- 의견 : 함수 마지막에 `return 0;` 추가.
  <br><br>- 기타 : `main` 외 함수라면 UB. 해당 파일의 `TEST()` 함수는 `return true;`가 있으나 타입 불일치 별도 이슈.
 </details>

#### [P2:Unused variable][정훈희][3136b89][Test.cpp/main()/Line:21]
[원인] pM 선언 후 미사용
```cpp
int* pM = nullptr;
```
 <details>
  <summary>상태 : [미결] , 위험 : 20, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 커밋 `3136b89`에서 `printf("T1 %d.\n ", *pM);`을 제거하면서 `pM`이 선언만 되고 참조되지 않는 dead variable이 됨.
  <br><br>- 의견 : `pM` 선언 라인 제거.
  <br><br>- 기타 : `3136b89` 커밋이 역참조는 제거했지만 변수 자체 정리 누락. 미사용 변수 경고 발생 가능.
 </details>

## P3:Low - 2026/04/19

#### [P3:Type mismatch][정훈희][5af0c3a][Test.cpp/TEST()/Line:16]
[원인] int 반환형에 bool 반환
```cpp
int TEST()
{
	int* pT = nullptr;

	if(  false)
	{
		printf("T4 %d.\n ", *p5);
	}

	printf("T5 %d.\n ", *pT);

printf("T7 %d.\n ", *pT);

	return true;
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 15, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int TEST()`의 반환 타입이 int인데 `return true;`로 bool 상수 반환. 암묵 변환되어 1을 반환하지만 비표준적.
  <br><br>- 의견 : `return 0;` 또는 `return 1;`로 명시적 정수 반환 또는 반환형을 `bool`로 변경.
  <br><br>- 기타 : 컴파일은 가능하나 의미 혼동 유발. 경고 레벨 상향 시 -Wconversion 경고 발생 가능.
 </details>

## P2:Medium - 2026/04/19

#### [P2:Header pollution][정훈희][203c200][Test.h/global/Line:5]
[원인] 헤더에 using namespace std 전역 오염
```cpp
using namespace std;
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `Test.h`에서 `using namespace std;`를 전역 네임스페이스에 선언. 이 헤더를 포함하는 모든 소스가 std 네임스페이스를 강제로 끌어와 이름 충돌 위험 증가.
  <br><br>- 의견 : 헤더에서 `using namespace std;` 제거하고 필요 시 소스 파일에서만 선언하거나 `std::` 접두어 명시.
  <br><br>- 기타 : `<iostream>`은 포함되어 있으나 본 헤더에서 사용처 없음. 헤더 자체의 필요성 재검토 필요.
 </details>

#### [P2:Missing return][정훈희][3136b89][Test.cpp/main()/Line:19-26]
[원인] int main 반환값 누락
```cpp
int main()
{
	int* pM = nullptr;

	printf("T2 %d.\n ", 123);

	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 30, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int main()` 블록 끝에 `return` 문 없음. C++ 표준상 `main`은 암묵적으로 0을 반환하지만 명시적 반환 권장.
  <br><br>- 의견 : 함수 마지막에 `return 0;` 추가.
  <br><br>- 기타 : `main` 외 함수라면 UB. 해당 파일의 `TEST()` 함수는 `return true;`가 있으나 타입 불일치 별도 이슈.
 </details>

#### [P2:Unused variable][정훈희][3136b89][Test.cpp/main()/Line:21]
[원인] pM 선언 후 미사용
```cpp
int* pM = nullptr;
```
 <details>
  <summary>상태 : [미결] , 위험 : 20, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 커밋 `3136b89`에서 `printf("T1 %d.\n ", *pM);`을 제거하면서 `pM`이 선언만 되고 참조되지 않는 dead variable이 됨.
  <br><br>- 의견 : `pM` 선언 라인 제거.
  <br><br>- 기타 : `3136b89` 커밋이 역참조는 제거했지만 변수 자체 정리 누락. 미사용 변수 경고 발생 가능.
 </details>

## P3:Low - 2026/04/19

#### [P3:Type mismatch][정훈희][203c200][Test.cpp/TEST()/Line:16]
[원인] int 반환형에 bool 반환
```cpp
int TEST()
{
	int* pT = nullptr;

	if(  false)
	{
		printf("T4 %d.\n ", *p5);
	}

	printf("T5 %d.\n ", *pT);

printf("T7 %d.\n ", *pT);

	return true;
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 15, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int TEST()`의 반환 타입이 int인데 `return true;`로 bool 상수 반환. 암묵 변환되어 1을 반환하지만 비표준적.
  <br><br>- 의견 : `return 0;` 또는 `return 1;`로 명시적 정수 반환 또는 반환형을 `bool`로 변경.
  <br><br>- 기타 : 컴파일은 가능하나 의미 혼동 유발. 경고 레벨 상향 시 -Wconversion 경고 발생 가능.
 </details>

## P2:Medium - 2026/04/19

#### [P2:Header pollution][정훈희][203c200][Test.h/global/Line:5]
[원인] 헤더에 using namespace std 전역 오염
```cpp
using namespace std;
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `Test.h`에서 `using namespace std;`를 전역 네임스페이스에 선언. 이 헤더를 포함하는 모든 소스가 std 네임스페이스를 강제로 끌어와 이름 충돌 위험 증가.
  <br><br>- 의견 : 헤더에서 `using namespace std;` 제거하고 필요 시 소스 파일에서만 선언하거나 `std::` 접두어 명시.
  <br><br>- 기타 : `<iostream>`은 포함되어 있으나 본 헤더에서 사용처 없음. 헤더 자체의 필요성 재검토 필요.
 </details>

#### [P2:Missing return][정훈희][3136b89][Test.cpp/main()/Line:17-24]
[원인] int main 반환값 누락
```cpp
int main()
{
	int* pM = nullptr;

	printf("T2 %d.\n ", 123);

	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 30, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int main()` 블록 끝에 `return` 문 없음. C++ 표준상 `main`은 암묵적으로 0을 반환하지만 명시적 반환 권장.
  <br><br>- 의견 : 함수 마지막에 `return 0;` 추가.
  <br><br>- 기타 : `main` 외 함수라면 UB. 해당 파일의 `TEST()` 함수는 `return true;`가 있으나 타입 불일치 별도 이슈.
 </details>

#### [P2:Unused variable][정훈희][3136b89][Test.cpp/main()/Line:19]
[원인] pM 선언 후 미사용
```cpp
int* pM = nullptr;
```
 <details>
  <summary>상태 : [미결] , 위험 : 20, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 커밋 3136b89에서 `printf("T1 %d.\n ", *pM);`을 제거하면서 `pM`이 선언만 되고 참조되지 않는 dead variable이 됨.
  <br><br>- 의견 : `pM` 선언 라인 제거.
  <br><br>- 기타 : 3136b89 커밋이 역참조는 제거했지만 변수 자체 정리 누락. 미사용 변수 경고 발생 가능.
 </details>

## P3:Low - 2026/04/19

#### [P3:Type mismatch][정훈희][203c200][Test.cpp/TEST()/Line:14]
[원인] int 반환형에 bool 반환
```cpp
int TEST()
{
	int* pT = nullptr;

	if(  false)
	{
		printf("T4 %d.\n ", *p5);
	}

	printf("T5 %d.\n ", *pT);

	return true;
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 15, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int TEST()`의 반환 타입이 int인데 `return true;`로 bool 상수 반환. 암묵 변환되어 1을 반환하지만 비표준적.
  <br><br>- 의견 : `return 0;` 또는 `return 1;`로 명시적 정수 반환 또는 반환형을 `bool`로 변경.
  <br><br>- 기타 : 컴파일은 가능하나 의미 혼동 유발. 경고 레벨 상향 시 -Wconversion 경고 발생 가능.
 </details>

## P2:Medium - 2026/04/19

#### [P2:Header pollution][정훈희][9f0471c][Test.h/global/Line:5]
[원인] 헤더에 using namespace std 전역 오염
```cpp
using namespace std;
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `Test.h`에서 `using namespace std;`를 전역 네임스페이스에 선언. 이 헤더를 포함하는 모든 소스가 std 네임스페이스를 강제로 끌어와 이름 충돌 위험 증가.
  <br><br>- 의견 : 헤더에서 `using namespace std;` 제거하고 필요 시 소스 파일에서만 선언하거나 `std::` 접두어 명시.
  <br><br>- 기타 : `<iostream>`은 포함되어 있으나 본 헤더에서 사용처 없음. 헤더 자체의 필요성 재검토 필요.
 </details>

#### [P2:Missing return][정훈희][3136b89][Test.cpp/main()/Line:17-24]
[원인] int main 반환값 누락
```cpp
int main()
{
	int* pM = nullptr;

	printf("T2 %d.\n ", 123);

	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 30, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int main()` 블록 끝에 `return` 문 없음. C++ 표준상 `main`은 암묵적으로 0을 반환하지만 명시적 반환 권장.
  <br><br>- 의견 : 함수 마지막에 `return 0;` 추가.
  <br><br>- 기타 : `main` 외 함수라면 UB. 해당 파일의 `TEST()` 함수는 `return true;`가 있으나 타입 불일치 별도 이슈.
 </details>

#### [P2:Unused variable][정훈희][3136b89][Test.cpp/main()/Line:19]
[원인] pM 선언 후 미사용
```cpp
int* pM = nullptr;
```
 <details>
  <summary>상태 : [미결] , 위험 : 20, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 커밋 3136b89에서 `printf("T1 %d.\n ", *pM);`을 제거하면서 `pM`이 선언만 되고 참조되지 않는 dead variable이 됨.
  <br><br>- 의견 : `pM` 선언 라인 제거.
  <br><br>- 기타 : 3136b89 커밋이 역참조는 제거했지만 변수 자체 정리 누락. 미사용 변수 경고 발생 가능.
 </details>

## P3:Low - 2026/04/19

#### [P3:Type mismatch][정훈희][9f0471c][Test.cpp/TEST()/Line:14]
[원인] int 반환형에 bool 반환
```cpp
int TEST()
{
	int* pT = nullptr;

	if(  false)
	{
		printf("T4 %d.\n ", *p5);
	}

	printf("T5 %d.\n ", *pT);

	return true;
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 15, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int TEST()`의 반환 타입이 int인데 `return true;`로 bool 상수 반환. 암묵 변환되어 1을 반환하지만 비표준적.
  <br><br>- 의견 : `return 0;` 또는 `return 1;`로 명시적 정수 반환 또는 반환형을 `bool`로 변경.
  <br><br>- 기타 : 컴파일은 가능하나 의미 혼동 유발. 경고 레벨 상향 시 -Wconversion 경고 발생 가능.
 </details>

## P2:Medium - 2026/04/19

#### [P2:Missing return][정훈희][3136b89][Test.cpp/main()/Line:17-24]
[원인] int main 반환값 누락
```cpp
int main()
{
	int* pM = nullptr;

	printf("T2 %d.\n ", 123);

	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 30, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int main()` 블록 끝에 `return` 문 없음. C++ 표준상 `main`은 암묵적으로 0을 반환하지만 명시적 반환 권장.
  <br><br>- 의견 : 함수 마지막에 `return 0;` 추가.
  <br><br>- 기타 : `main` 외 함수라면 UB. 해당 파일의 `TEST()` 함수는 `return true;`가 있으나 타입 불일치 별도 이슈.
 </details>

#### [P2:Unused variable][정훈희][3136b89][Test.cpp/main()/Line:19]
[원인] pM 선언 후 미사용
```cpp
int* pM = nullptr;
```
 <details>
  <summary>상태 : [미결] , 위험 : 20, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 커밋 3136b89에서 `printf("T1 %d.\n ", *pM);`을 제거하면서 `pM`이 선언만 되고 참조되지 않는 dead variable이 됨.
  <br><br>- 의견 : `pM` 선언 라인 제거.
  <br><br>- 기타 : 3136b89 커밋이 역참조는 제거했지만 변수 자체 정리 누락. 미사용 변수 경고 발생 가능.
 </details>

## P3:Low - 2026/04/19

#### [P3:Type mismatch][정훈희][3136b89][Test.cpp/TEST()/Line:14]
[원인] int 반환형에 bool 반환
```cpp
int TEST()
{
	int* pT = nullptr;

	if(  false)
	{
		printf("T4 %d.\n ", *p5);
	}

	printf("T5 %d.\n ", *pT);

	return true;
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 15, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int TEST()`의 반환 타입이 int인데 `return true;`로 bool 상수 반환. 암묵 변환되어 1을 반환하지만 비표준적.
  <br><br>- 의견 : `return 0;` 또는 `return 1;`로 명시적 정수 반환 또는 반환형을 `bool`로 변경.
  <br><br>- 기타 : 컴파일은 가능하나 의미 혼동 유발. 경고 레벨 상향 시 -Wconversion 경고 발생 가능.
 </details>

## P2:Medium - 2026/04/19

#### [P2:Missing return][정훈희][3136b89][Test.cpp/main()/Line:17-24]
[원인] int main 반환값 누락
```cpp
int main()
{
	int* pM = nullptr;

	printf("T2 %d.\n ", 123);

	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 30, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int main()` 블록 끝에 `return` 문 없음. C++ 표준상 `main`은 암묵적으로 0을 반환하지만 명시적 반환 권장
  <br><br>- 의견 : 함수 마지막에 `return 0;` 추가
  <br><br>- 기타 : `main` 외 함수라면 UB. 해당 파일의 `TEST()` 함수는 `return true;`가 있으나 타입 불일치 별도 이슈
 </details>

#### [P2:Unused variable][정훈희][3136b89][Test.cpp/main()/Line:19]
[원인] pM 선언 후 미사용
```cpp
int* pM = nullptr;
```
 <details>
  <summary>상태 : [미결] , 위험 : 20, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 커밋 3136b89에서 `printf("T1 %d.\n ", *pM);`을 제거하면서 `pM`이 선언만 되고 참조되지 않는 dead variable이 됨
  <br><br>- 의견 : `pM` 선언 라인 제거
  <br><br>- 기타 : 3136b89 커밋이 역참조는 제거했지만 변수 자체 정리 누락. 미사용 변수 경고 발생 가능
 </details>

## P3:Low - 2026/04/19

#### [P3:Type mismatch][정훈희][3136b89][Test.cpp/TEST()/Line:14]
[원인] int 반환형에 bool 반환
```cpp
int TEST()
{
	int* pT = nullptr;

	if(  false)
	{
		printf("T4 %d.\n ", *p5);
	}

	printf("T5 %d.\n ", *pT);

	return true;
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 15, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int TEST()`의 반환 타입이 int인데 `return true;`로 bool 상수 반환. 암묵 변환되어 1을 반환하지만 비표준적
  <br><br>- 의견 : `return 0;` 또는 `return 1;`로 명시적 정수 반환 또는 반환형을 `bool`로 변경
  <br><br>- 기타 : 컴파일은 가능하나 의미 혼동 유발. 경고 레벨 상향 시 -Wconversion 경고 발생 가능
 </details>

## [해결] - 2026/04/19

## P2:Medium - 2026/04/19

#### [P2:Missing return][정훈희][3136b89][Test.cpp/main()/Line:17-24]
[원인] int main 반환값 누락
```cpp
int main()
{
	int* pM = nullptr;

	printf("T2 %d.\n ", 123);

	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 30, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int main()` 블록 끝에 `return` 문 없음. C++ 표준상 `main`은 암묵적으로 0을 반환하지만 명시적 반환 권장
  <br><br>- 의견 : 함수 마지막에 `return 0;` 추가
  <br><br>- 기타 : `main` 외 함수라면 UB. 해당 파일의 `TEST()` 함수는 `return true;`가 있으나 타입 불일치 별도 이슈
 </details>

#### [P2:Unused variable][정훈희][3136b89][Test.cpp/main()/Line:19]
[원인] pM 선언 후 미사용
```cpp
int* pM = nullptr;
```
 <details>
  <summary>상태 : [미결] , 위험 : 20, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 커밋 3136b89에서 `printf("T1 %d.\n ", *pM);`을 제거하면서 `pM`이 선언만 되고 참조되지 않는 dead variable이 됨
  <br><br>- 의견 : `pM` 선언 라인 제거
  <br><br>- 기타 : 3136b89 커밋이 역참조는 제거했지만 변수 자체 정리 누락. 미사용 변수 경고 발생 가능
 </details>

## P3:Low - 2026/04/19

#### [P3:Type mismatch][정훈희][3136b89][Test.cpp/TEST()/Line:14]
[원인] int 반환형에 bool 반환
```cpp
int TEST()
{
	int* pT = nullptr;

	if(  false)
	{
		printf("T4 %d.\n ", *p5);
	}

	printf("T5 %d.\n ", *pT);

	return true;
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 15, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `int TEST()`의 반환 타입이 int인데 `return true;`로 bool 상수 반환. 암묵 변환되어 1을 반환하지만 비표준적
  <br><br>- 의견 : `return 0;` 또는 `return 1;`로 명시적 정수 반환 또는 반환형을 `bool`로 변경
  <br><br>- 기타 : 컴파일은 가능하나 의미 혼동 유발. 경고 레벨 상향 시 -Wconversion 경고 발생 가능
 </details>

## [해결] - 2026/04/19

## P2:Medium - 2026/04/19

#### [P2:Compile undef][정훈희][151efc0][Test.cpp/main()/Line:27]
[원인] 미정의 변수 pP 역참조 컴파일 오류
```
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 65, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `151efc0` 커밋부터 존재. `main()` 라인 27에서 선언되지 않은 변수 `pP`를 `*pP`로 역참조하여 컴파일 실패. `Huns.h`(include 대상) 파일이 현 저장소에 존재하지 않아 외부 선언도 확인 불가. 빌드 자체가 불가능한 상태.
  <br><br>- 의견 : `pP` 선언 추가(`int* pP = nullptr;` 등) 또는 정의된 변수로 교체.
  <br><br>- 기타 : T4(Line:9)의 `p5`와 동일 패턴(미정의 식별자). RV4 적용.
 </details>

## P3:Low - 2026/04/19

#### [P3:DeadCode undef][정훈희][f625d50][Test.cpp/TEST()/Line:7-10]
[원인] 데드코드 내 미정의 변수 p5 컴파일 오류
```
if(  false)
{
	printf("T4 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `f625d50` 커밋에서 도입. `if(false)` 데드코드 블록 내에서 선언되지 않은 변수 `p5`를 역참조. 런타임 미실행이지만 C++ 컴파일 단계에서 식별자 탐색 실패로 오류 발생. `if(  false)` 내 중복 공백도 존재하여 가독성 저하.
  <br><br>- 의견 : `p5` 선언 추가, 데드코드 블록 전체 제거, 또는 `#if 0` 전처리로 교체. 공백 정리.
  <br><br>- 기타 : T3(Line:27)의 `pP`와 동일 패턴(미정의 식별자). 데드코드 자체 정리 대상. RV4 적용.
 </details>

## P2:Medium - 2026/04/19

#### [P2:Compile undef][정훈희][151efc0][Test.cpp/main()/Line:27]
[원인] 미정의 변수 pP 역참조 컴파일 오류
```
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 65, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 선언되지 않은 변수 `pP`를 `*pP`로 역참조. 컴파일 오류로 빌드 불가. `Huns.h` 등 포함 헤더에도 선언 미확인. `151efc08` 커밋부터 존재.
  <br><br>- 의견 : `pP` 선언 추가(`int* pP = nullptr;` 등) 또는 정의된 변수 사용.
  <br><br>- 기타 : T4(Line:9)의 `p5`와 동일 패턴. RV4 및 RV7 적용.
 </details>

## P3:Low - 2026/04/19

#### [P3:DeadCode undef][정훈희][f625d50][Test.cpp/TEST()/Line:7-10]
[원인] 데드코드 내 미정의 변수 p5 컴파일 오류
```
if(  false)
{
	printf("T4 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `if(false)` 데드코드 블록 내에서 선언되지 않은 변수 `p5` 역참조. 실행되지 않지만 C++ 컴파일 단계에서 오류 발생. `if(  false)` 공백 중복도 존재. `f625d50` 커밋에서 도입.
  <br><br>- 의견 : `p5` 선언 추가 또는 데드코드 블록 전체 제거. 공백 정리.
  <br><br>- 기타 : T3(Line:27)의 `pP`와 동일 패턴. 데드코드 자체도 정리 대상. RV7 적용.
 </details>
