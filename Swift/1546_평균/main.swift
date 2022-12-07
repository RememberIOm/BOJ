let n = Float(readLine()!)!
let scoreLi = readLine()!.split(separator: " ").map{Float($0)!}

let scoreMax = scoreLi.max()!

var scoreNewSum: Float = 0

for scoreLiIdx in scoreLi {
    scoreNewSum += scoreLiIdx / scoreMax * 100
}

print(scoreNewSum / n)
