for _ in 0..<Int(readLine()!)! {
    let lineArr = readLine()!.split(separator: " ")
    
    for sIdx in lineArr[1] {
        for _ in 0..<Int(String(lineArr[0]))! {
            print(sIdx, terminator: "")
        }
    }
    
    print()
}
