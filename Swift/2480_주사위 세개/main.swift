let dice = readLine()!.split(separator: " ").map{Int($0)!}

let dice_set = Set(dice)
var dice_index = Array(repeating: 0, count: 7)
for dice_i in dice {
    dice_index[dice_i] += 1
}

var prize: Int

if dice_set.count == 1 {
    prize = 10000 + dice[0] * 1000
}
else if dice_set.count == 2 {
    var duplicate = 0
    
    for dice_set_i in dice {
        if dice_index[dice_set_i] == 2 {
            duplicate = dice_set_i
            
            break
        }
    }
    
    prize = 1000 + duplicate * 100
}
else {
    prize = dice.max()! * 100
}

print(prize)
