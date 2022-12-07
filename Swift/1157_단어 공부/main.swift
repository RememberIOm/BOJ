let s = readLine()!.uppercased().map{ String($0) }

var abcNum = Array(repeating: 0, count: 26)

for sIdx in s {
    abcNum[Int(UnicodeScalar(sIdx)!.value) - 65] += 1
}

var abcMax = [Int]()
let abcMaxNum = abcNum.max()!

for i in 0..<26 {
    if abcNum[i] == abcMaxNum {
        abcMax.append(i + 65)
    }
}

if abcMax.count == 1 {
    print(UnicodeScalar(abcMax[0])!)
}
else {
    print("?")
}
