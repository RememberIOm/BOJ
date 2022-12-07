var modSet = Set<Int>()

for _ in 0..<10 {
    modSet.insert(Int(readLine()!)! % 42)
}

print(modSet.count)
