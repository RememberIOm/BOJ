## 1. 분석

각각 킹, 퀸, 룩, 비숍, 나이트, 폰의 현재 갖고 있는 개수를 입력 받은 후에 계산을 거쳐 필요한 말의 개수를 출력하는 문제

## 2. 접근

```swift
let chess_cur = lineArr.map{Int($0)!}
```

`map{}` 함수를 이용해서 `String`으로 받아진 `lineArr`의 각각 원소들을 `Int`로 형변환 해주는 코드.

`$0`이 원소들이 들어가는 자리이다.

파이썬의 `map()`과 기능이 같다.

```swift
for i in 0...5 {
```

`0…5`는 0부터 5까지의 정수를 가진 배열이다.

5를 포함 하는 것에 주의

```swift
    print(chess_need[i] - chess_cur[i], terminator: " ")
```

`print()` 함수의 `terminator` 매개변수는 `print()`가 끝나고 출력되는 값을 가진 `String` 변수이다.

기본값은 `\n`이다. 그렇기에 `terminator`를 생략하는 대부분의 경우에선 `print()`가 실행된 후에 개행이 된다.

파이썬의 `print()` 함수의 `end` 매개변수와 기능이 같다.