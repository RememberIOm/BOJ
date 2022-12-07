import Foundation

let line = readLine()!
let lineArr = line.components(separatedBy: " ")

let chess_cur = lineArr.map{Int($0)!}
let chess_need = [1, 1, 2, 2, 2, 8]

for i in 0...5 {
    print(chess_need[i] - chess_cur[i], terminator: " ")
}
