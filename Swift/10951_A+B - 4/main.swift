while let lineArr = readLine() {
    print(lineArr.split(separator: " ").map{Int($0)!}.reduce(0, +))
}
