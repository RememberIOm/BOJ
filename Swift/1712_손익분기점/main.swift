let lineArr = readLine()!.split(separator: " ").map{ Int(String($0))! }

let a = lineArr[0]
let b = lineArr[1]
let c = lineArr[2]

if c - b > 0 {
    print(a / (c - b) + 1)
}
else {
    print(-1)
}
