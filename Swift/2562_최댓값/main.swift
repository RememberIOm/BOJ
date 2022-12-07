var maxVal = 0
var maxIdx = 0

for i in 1...9 {
    let inputNum = Int(readLine()!)!
    
    if inputNum > maxVal {
        maxVal = inputNum
        maxIdx = i
    }
}

print(maxVal, maxIdx, terminator: "\n")
