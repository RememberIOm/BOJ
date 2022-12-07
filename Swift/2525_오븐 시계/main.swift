let listArr = readLine()!.split(separator: " ").map{Int($0)!}

var h = listArr[0]
var m = listArr[1]
var t = Int(readLine()!)!

let t_h = t / 60
let t_m = t % 60

h += t_h
m += t_m

if m >= 60 {
    m -= 60
    h += 1
}

if h >= 24 {
    h -= 24
}

print(h, m)
