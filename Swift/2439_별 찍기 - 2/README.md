## 1. 분석

입력 받은 정수 줄 만큼 별을 오른쪽 정렬하여 출력하는 문제이다.

## 2. 접근

예제 답안을 통해 별의 형태를 분석해보자.

5가 들어왔을 때,

첫번째 줄은 공백이 4개, 별이 1개

두번째 줄은 공백이 3개, 별이 2개

…

마지막 줄은 공백이 0개, 별이 5개이다.

이는 입력 받은 정수가 `n`일 때,

**`i`번째 줄은 공백이 `n - i`개, 별이 `i`개**

로 일반화가 되며, 이를 코드로 표현하려면 반복문을 이용해 `i`의 수를 늘려주면서 출력하면 된다.

Swift로 구현할 때, 공백 배열과 별 배열 2개를 만들어 각각 일반화 공식에 맞게 초기화 한 후, 배열 덧셈으로 합치고, 문자열 `joined()`를 이용해 출력하였다.