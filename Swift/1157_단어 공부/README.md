## 1. 분석

문자열을 받은 후 각각 알파벳(소문자 대문자 도합)이 가장 많이 나온 것을 출력하는 문제이다. (중복일 땐 ?를 출력)

## 2. 접근

1. 먼저 소문자와 대문자를 동시에 카운팅하기 위해 `uppercased` 함수를 이용해 모두 대문자로 만들어준다.
2. 알파벳의 개수를 저장하는 배열 `abcNum`을 초기화 해준다.
3. 문자열을 탐색하면서 `abcNum`에 값을 저장해준다.
4. **가장 많은 알파벳**을 저장하는 배열 `abcMax`를 초기화하고, **가장 많은 알파벳의 수**를 저장하는 `abcMaxNum` 변수를 `abcNum`의 최댓값으로 초기화한다.
5. `abcNum`을 탐색하면서 `abcMaxNum`과 같은 값을 가지는 인덱스를 `abcMax`에 저장한다.
6. 만약 `abcMax`가 1개라면 그대로 출력하고, 여러개라면 ?를 출력한다.