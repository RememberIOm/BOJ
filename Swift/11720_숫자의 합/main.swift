let _ = readLine()

let nums = Array(readLine()!).map{ Int(String($0))! }

print(nums.reduce(0, +))
