var arr = Array<Int>(repeating: 0, count: 2_000_001)

for _ in 0..<Int(readLine()!)! {
    arr[Int(readLine()!)! + 1_000_000] += 1
}

var result = ""

for i in 0..<2_000_001 {
    result += String(repeating: String(i - 1_000_000) + "\n", count: arr[i])
}

print(result)
