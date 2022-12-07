import Foundation

let a = Double(readLine()!)!

var x: Double = 1

while pow(x, 3) - pow(x - 1, 3) < a {
    x += 1
}

print(Int(x))
