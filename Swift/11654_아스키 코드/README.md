## 1. 분석

문자가 주어지면 해당 문자의 아스키 코드를 출력하는 문제이다.

## 2. 접근

Swift에서 ASCII → `Int` 연산을 하는 방법은 `UnicodeScalar`에 포함된 `value`를 이용하는 것이다.