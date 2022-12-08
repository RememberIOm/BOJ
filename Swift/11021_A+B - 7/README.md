## 1. 분석

처음 받은 정수만큼 2개의 정수를 받아서 덧셈을 주어진 출력 형식에 맞게 출력하는 문제이다.

## 2. 접근

`for`문에 직접 `Int(readLine()!)!`을 넣어서 반복을 한다

`ans`같은 경우는 먼저 `readLine()!.split(separator: " ").map{Int($0)!}` 까지는 일반적인 정수 배열을 만드는 것인데, 여기서 `reduce` 함수를 이용해 각 원소 덧셈을 해준다.

---

**`reduce`에 대한 설명**

`reduce` 함수의 정의는 다음과 같다.

```swift
func reduce<U>(initial: U, combine: (U, T) -> U) -> U
```

배열 내부의 값을 하나하나씩 이전 결과와 다음 원소를 계속 호출하여 연산을 실행하는 함수이다.

예를 들어 `[0, 1, 2, 3, 4]` 라는 배열이 있다면 `reduce`로 덧셈을 적용시키면

```swift
{0 + 1} -> {1 + 2} -> {3 + 3} -> {6 + 4}
```

와 같이 진행되며 함수의 출력은 10이 된다.

`reduce` 함수의 단축은 다음과 같은 과정을 거친다.

```swift
array.reduce(0, { (s1: Int, s2: Int) -> Int in
    return s1 + s2
})
```

여기서 클로저가 함수의 마지막에 위치하고 있으니 인자를 분리하여 작성할 수 있다.

```swift
array.reduce(0) { (s1: Int, s2: Int) -> Int in
    return s1 + s2
}
```

위 코드에서 `s1`, `s2`의 타입은 추론 가능하므로 생략.

```swift
array.reduce(0) { (s1, s2) in s1 + s2 }
```

`s1`과 `s2`는 `$0`, `$1`로 대신하여 사용할 수 있다.

```swift
array.reduce(0) { $0 + $1 }
```

여기서 연산자는 중위 연산자이므로 왼쪽 값이 `$0`, 오른쪽 값이 `$1`임을 추론 가능하므로 다음과 같이 생략된다.

```swift
array.reduce( 0, + )
```

이것이 최종적으로 위에서 사용된 `reduce`의 용법이다.

## 3. 참고 자료

[Swift) 클로저(Closure) 정복하기(1/3) - 클로저, 누구냐 넌 (tistory.com)](https://babbab2.tistory.com/81)

[[Swift]Map, Filter, Reduce 그리고 추론 (minsone.github.io)](https://minsone.github.io/mac/ios/swift-map-filter-reduce-and-inference)