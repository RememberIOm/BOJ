## 1. 분석

1부터 10000까지 셀프 넘버를 출력하는 문제이다.

셀프 넘버에 대한 정의는 문제에 설명되어 있다.

## 2. 접근

먼저 셀프 넘버를 구하려면 10000보다 살짝 큰 `true`로 이루어진 배열을 만들고, 생성자가 있는 수가 나올 때 마다 `false`로 값을 바꾼 후 `true`인 값만 출력 해야겠다고 생각했다.

Swift에서 정수 1234를 [1, 2, 3, 4] 와 같이 만들 때 사용하는 방법을 인터넷에서 검색하였다.

```swift
let digit = String(i).compactMap{Int(String($0))}
```

String에 포함된 `compactMap` 함수와 일반 `Map`과 다른 점은 옵셔널을 기본적으로 언패킹 해준다는 것이다.

여기서 `Int($0)` 이 아닌 `Int(String($0))`으로 이중 변환 한 이유에 대해서는 하단의 자료를 참고하였다.

이 배열의 원소를 전부 더해서 각 자리수의 합으로 사용하였다.

1부터 9999까지 모든 수의 탐색을 마친 후에 `selfNum` 배열에서 `true`인 인덱스만 출력해주었다.

## 3. 참고 자료

[[Swift] Int(String(SubString)), Int(SubString)의 속도 차이 원인 (tistory.com)](https://icksw.tistory.com/218)