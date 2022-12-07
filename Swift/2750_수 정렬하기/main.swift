var arr = [Int]()

for _ in 0..<Int(readLine()!)! {
    arr.append(Int(readLine()!)!)
}

arr.sort()

for arr_i in arr {
    print(arr_i)
}
