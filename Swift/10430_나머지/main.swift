let lineArr = readLine()!.split(separator: " ").map{Int($0)!}

let a = lineArr[0]
let b = lineArr[1]
let c = lineArr[2]

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
