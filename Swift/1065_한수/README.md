## 1. 분석

문제에 주어진 정수보다 작거나 같은 한수의 개수를 출력하는 문제이다.

한수란, 모든 자릿수가 증가하는 등차수열로 이루어진 수이다.

## 2. 접근

먼저 한수를 제작하는 방식으로는 구현이 복잡하고, 1부터 `n`까지 모든 수를 판정하는 브루트포스 알고리즘으로도 시간복잡도가 $O(n)$으로 될 것이므로 브루트포스 알고리즘으로 구현하였다.

먼저 한수의 개수를 카운트하는 `hanCnt` 변수를 만들어 놓고, 1부터 `n`까지의 수 모두를 판정하였다.

**판정 방법**

1. 정수를 자릿수로 된 배열 `nArray`로 만든다.
2. 각 자릿수의 차를 저장하는 `Set` 자료구조 `nArraySub`를 만든다.
3. 반복문으로 각 자릿수의 차를 `nArraySub`에 저장한다.
4. `nArraySub`의 값이 0이라면 원래의 정수의 자릿수가 1이라는 뜻이며 자동으로 한수가 되고, 1이라면 각 자릿수의 차가 모두 같다는 것이므로 한수가 된다. 그래서 `nArraySub`의 값이 0과 1 둘 중 하나라면 `hanCnt`의 값을 1 올려준다.
5. 모든 수의 범위를 탐색했다면 `hanCnt`를 출력한다.