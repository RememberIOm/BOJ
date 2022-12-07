let n = Int(readLine()!)!

var hanCnt = 0

for i in 1...n {
    let nArray = String(i).compactMap{Int(String($0))}
    
    var nArraySub = Set<Int>()
    
    for nArray_i in 1..<nArray.count {
        nArraySub.insert(nArray[nArray_i] - nArray[nArray_i - 1])
    }
    
    if Set([0, 1]).contains(nArraySub.count) {
        hanCnt += 1
    }
}

print(hanCnt)
