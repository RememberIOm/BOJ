let lineArr = readLine()!.split(separator: " ").map{Int($0)!}

let x = lineArr[1]

let a = readLine()!.split(separator: " ").map{Int($0)!}

for a_i in a {
    if a_i < x {
        print(a_i, terminator: " ")
    }
}
