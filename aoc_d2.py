#Rock = 1, paper = 2, scissor = 3 , lose = 0, draw = 3, win = 6
#Part 1
# score = {"X":1, "Y":2, "Z":3} #My score
# winPair = {"A":"Y", "B":"Z", "C":"X"}
# drawPair = {"A":"X", "B":"Y", "C":"Z"}
# with open("d2_input.txt") as fi:
#     totalScore = 0
#     for line in fi:
#         line = line.rstrip()
#         opp,me = line.split()
#         #Check win
#         if winPair[opp] == me:
#             totalScore += 6 + score[me]
#         elif drawPair[opp] == me:
#             totalScore += 3 + score[me]
#         else:
#             totalScore += 0 + score[me]
#     print(totalScore)

#Part 2
score = {"A":1, "B":2, "C":3} #My score
winPair = {"A":"B", "B":"C", "C":"A"}
losePair = {"A":"C", "B":"A", "C":"B"}
with open("d2_input.txt") as fi:
    totalScore = 0
    for line in fi:
        line = line.rstrip()
        opp,res = line.split()
        if res == "Y":
            ##Mirror
            totalScore += 3 + score[opp]
        elif res == "X": #Lose
            #Lose
            totalScore += 0 + score[losePair[opp]]
        else:
            totalScore += 6 + score[winPair[opp]]

    print(totalScore)
