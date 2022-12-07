for i in 1...Int(readLine()!)! {
    let lineArr = readLine()!.split(separator: " ").map{Int($0)!}
    
    print("Case #\(i): \(lineArr[0]) + \(lineArr[1]) = \(lineArr.reduce(0, +))")
}
