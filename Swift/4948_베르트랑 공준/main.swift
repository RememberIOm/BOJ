import Foundation

while true {
    let n = Int(readLine()!)!
    
    if n == 0 {
        break
    }
    
    var prime = Array(repeating: true, count: 2 * n + 1)
    prime[1] = false
    
    for i in 1...Int(sqrt(Double(2 * n))) {
        if prime[i] == true {
            var j = 2
            
            while i * j <= 2 * n {
                prime[i * j] = false
                
                j += 1
            }
        }
    }
    
    var cnt = 0
    
    for i in n + 1...2 * n {
        if prime[i] == true {
            cnt += 1
        }
    }
    
    print(cnt)
}
