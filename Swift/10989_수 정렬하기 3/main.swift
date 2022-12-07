var arr = Array<Int>(repeating: 0, count: 10_001)

for _ in 0..<Int(readLine()!)! {
    arr[Int(readLine()!)!] += 1
}

var result = ""

for i in 1...10_000 {
    result += String(repeating: String(i) + "\n", count: arr[i])
}

print(result)
