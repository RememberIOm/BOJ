let n_origin = Int(readLine()!)!

var n = n_origin
var cnt = 0

while true {
    n = (n % 10) * 10 + ((n / 10) + (n % 10)) % 10
    
    cnt += 1
    
    if n == n_origin {
        break
    }
}

print(cnt)
