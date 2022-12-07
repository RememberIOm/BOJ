import Foundation

let lineArr = readLine()!.split(separator: " ").map{Int($0)!}

let m = lineArr[0]
let n = lineArr[1]

var prime = Array(repeating: true, count: n + 1)
prime[1] = false

for i in 1...Int(sqrt(Double(n))) {
    if prime[i] == true {
        var j = 2
        
        while i * j <= n {
            prime[i * j] = false
            
            j += 1
        }
    }
}

for i in m...n {
    if prime[i] == true {
        print(i)
    }
}
