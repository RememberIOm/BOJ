for _ in 0..<Int(readLine()!)! {
    let lineArr = readLine()!.split(separator: " ").map{Int($0)!}
    
    print(lineArr[0] + lineArr[1])
}
