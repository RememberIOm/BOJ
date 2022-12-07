import Foundation

let lineArr = readLine()!.split(separator: " ").map{ Double(String($0))! }

let a = lineArr[0]
let b = lineArr[1]
let v = lineArr[2]

let up = a - b

print(Int(ceil((v - a) / up)) + 1)
