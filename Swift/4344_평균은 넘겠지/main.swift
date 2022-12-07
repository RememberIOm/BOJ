import Foundation

for _ in 0..<Int(readLine()!)! {
    let nums = readLine()!.split(separator: " ").map{Double($0)!}
    let n = nums[0]
    let scores = nums[1...]
    
    let avg = scores.reduce(0, +) / n
    
    var overAvgCnt = 0
    
    for scoresIdx in scores {
        if scoresIdx > avg {
            overAvgCnt += 1
        }
    }
    
    print("\(String(format: "%.3f", Double(overAvgCnt) / Double(n) * 100))%")
}
