let s = Array(readLine()!).map{ String($0) }

var alphabetIdx = Array(repeating: -1, count: 26)

for i in 0..<s.count {
    let sIdxAscii = Int(UnicodeScalar(s[i])!.value)
    
    if alphabetIdx[sIdxAscii - 97] == -1 {
        alphabetIdx[sIdxAscii - 97] = i
    }
}

print(alphabetIdx.map{ String($0) }.joined(separator: " "))
