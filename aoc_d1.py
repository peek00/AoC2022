#Part 1
# with open("d1_test.txt") as fi:
#     top3 = []
#     currMax = 0
#     currSum = 0
#     for line in fi:
#         line = line.rstrip()  
#         if len(line) == 0:
#             #Check max 
#             currMax = max(currMax, currSum)
#             #Reset currSum
#             currSum = 0
#         else:
#             currSum += int(line)
#     print(currMax)

#Part 2
with open("d1_test.txt") as fi:
    top3 = []
    currSum = 0
    for line in fi:
        line = line.rstrip()  
        if len(line) == 0:
            #Check max 
            if len(top3) < 3:
                top3.append(currSum)
            else:
                if currSum > min(top3):
                    top3.remove(min(top3))
                    top3.append(currSum)
            #Reset currSum
            currSum = 0
        else:
            currSum += int(line)
    print(sum(top3))