let cost = Int(readLine()!)!
let num = Int(readLine()!)!

var costNew = 0

for _ in 0..<num {
    let lineArr = readLine()!.split(separator: " ").map{Int($0)!}
    let costCur = lineArr[0]
    let numCur = lineArr[1]
    
    costNew += costCur * numCur
}

if cost == costNew {
    print("Yes")
}
else {
    print("No")
}
