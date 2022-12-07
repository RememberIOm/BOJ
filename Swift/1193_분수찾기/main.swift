let x = Int(readLine()!)!

var floor = 0
var floor_end = 0

while floor_end < x {
    floor_end += floor + 1
    floor += 1
}

var numerator = floor_end - x + 1
var denominator = floor + 1 - numerator

if floor % 2 == 0 {
    swap(&numerator, &denominator)
}

print("\(numerator)/\(denominator)")
