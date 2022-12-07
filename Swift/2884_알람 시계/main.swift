let listArr = readLine()!.split(separator: " ").map{Int($0)!}

var h = listArr[0]
var m = listArr[1]

m -= 45

if m < 0 {
    m += 60
    h -= 1
}

if h < 0 {
    h += 24
}

print("\(h) \(m)")
