let n = Int(readLine()!)!

for i in 1...n {
    let blank = Array(repeating: " ", count: (n - i))
    let star = Array(repeating: "*", count: i)
    
    let ans = blank + star
    
    print(ans.joined(separator: ""))
}
