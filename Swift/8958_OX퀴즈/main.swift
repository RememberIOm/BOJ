for _ in 0..<Int(readLine()!)! {
    let inputStr = readLine()!
    
    var continuity = 0
    var score = 0
    
    for inputStrIdx in inputStr {
        if inputStrIdx == "O" {
            continuity += 1
            score += continuity
        }
        else {
            continuity = 0
        }
    }
    
    print(score)
}
