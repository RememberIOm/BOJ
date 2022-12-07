extension Bool {
    static func ^ (lhs: Bool, rhs: Bool) -> Bool {
        return lhs != rhs
    }
}

let year = Int(readLine()!)!

let mod4 = (year % 4 == 0)
let mod100 = (year % 100 == 0)
let mod400 = (year % 400 == 0)

if mod4 ^ mod100 ^ mod400 {
    print("1")
}
else {
    print("0")
}
