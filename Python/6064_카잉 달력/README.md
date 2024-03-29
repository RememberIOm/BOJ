## 1. 분석

처음에는 `x`, `y`를 하나씩 증가시키며 답을 구하려했다. 그러나 시간 제한이 1초이고, `x`와 `y`의 값이 40000 까지 입력될 수 있는데, 이때 최악의 경우 둘의 최소공배수가 16억 정도로 나오므로(`x`가 39999,`y`가 40000일 때) 시간 초과가 날 것이므로 다른 방법으로 풀어야 했다.

다음으로 생각한 방법은 `x`로 인해 나올 수 있는 연도만 골라서 `y`와 대조를 해보는 것이다.

`x`가 정해져 있다면, 나올 수 있는 연도는 `m`으로 나눴을 때, 나머지가 `x`인 연도밖에 없다. 이 연도 중에 `n`으로 나눴을 때, 나머지가 `y`인 연도가 유일한 답이 될 것이다.

연도의 상한은 `m`과 `n`의 최소공배수가 될 것이다.

## 2. 접근

`for`문으로 `x`부터 `m`씩 증가하고, `m`과 `n`의 최소공배수까지 증가하는 `i`를 만들었다. 이렇게 하면 `x`가 정해졌을 때 될 수 있는 연도만을 추릴 수 있게 된다.

이후 그 `i`를 `n`으로 나눴을 때, 나머지가 `y % n`인 연도를 `result`에 넣어주고 출력한다. (나머지가 0일 때는 `y == n` 일 것이기 때문이다.)

만약 위의 `for`문에서 연도를 찾지 못하면 해당 `<x, y>`는 올바른 연도가 아니므로, `-1`을 출력하도록 하였다.