let lineArr = readLine()!.split(separator: " ").map{Int($0)!}

let a = lineArr[0]
let b = lineArr[1]

if a > b {
    print(">")
}
else if a == b {
    print("==")
}
else if a < b {
    print("<")
}
