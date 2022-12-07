import Foundation

func makePrime(limit: Int) -> Array<Bool> {
    var prime = Array(repeating: true, count: limit + 1)
    prime[1] = false
    
    for i in 1...Int(sqrt(Double(limit))) {
        if prime[i] == true {
            var j = 2
            
            while i * j <= limit {
                prime[i * j] = false
                
                j += 1
            }
        }
    }
    
    return prime
}

for _ in 0..<Int(readLine()!)! {
    let n = Int(readLine()!)!
    
    let prime = makePrime(limit: n)
    
    for b in n / 2...n {
        let a = n - b
        
        if prime[a] && prime[b] {
            print(a, b)
            break
        }
    }
}
