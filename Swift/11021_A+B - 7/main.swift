for i in 1...Int(readLine()!)! {
    let ans = readLine()!.split(separator: " ").map{Int($0)!}.reduce(0, +)
    
    print("Case #\(i): \(ans)")
}
