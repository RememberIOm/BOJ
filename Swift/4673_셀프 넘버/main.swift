var selfNum = Array(repeating: true, count: 10050)

for i in 1...9999 {
    let digit = String(i).compactMap{Int(String($0))}
    
    let nextNum = i + digit.reduce(0, +)
    
    selfNum[nextNum] = false
}

for i in 1...10000 {
    if selfNum[i] {
        print(i)
    }
}
