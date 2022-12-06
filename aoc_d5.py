# #Part 1
# with open("d5_input.txt") as fi:
#     #Parse the info into 3 lists
#     stackList = []
#     atInstructions = False
#     for line in fi:
#         # Use a stack system for all 3 
#         if len(line) == 1:
#             #This is the divider for instructions
#             atInstructions = True
#         elif atInstructions:
#             #Instruction passed in [move X, from X, to X]
#             instruction = [int(x) for x in line.split() if x.isdigit()] 
#             moveHowMany = instruction[0]
#             moveFrom = instruction[1]-1
#             moveTo = instruction[2]-1
#             for i in range(moveHowMany):        
#                 poppedItem = stackList[moveFrom].pop(0)
#                 stackList[moveTo].insert(0,poppedItem)
#         elif "[" not in line:
#             #Targets the label
#             pass 
#         else:
#             # X means empty spot
#             line = line.rstrip().replace("    ", " ").split(" ")
#             currPos =  0 #Start at 0 to match stack name
#             for seg in line:
#                 print(f"Seg is {seg}")
#                 if "[" not in seg:
#                     ## Up pos by 1
#                     currPos += 1
#                 else:                  
#                     #Create a new list if it is not in
#                     if currPos >= len(stackList):
#                         for i in range(currPos - len(stackList) + 1):
#                             stackList.append([])
#                     stackList[currPos].append(seg)
#                     currPos += 1
#                 # Reset currPos
#     for stack in stackList:
#         print(stack[0])

#MCD    
#Part 2
with open("d5_input.txt") as fi:
    #Parse the info into 3 lists
    stackList = []
    atInstructions = False
    for line in fi:
        # Use a stack system for all 3 
        if len(line) == 1:
            #This is the divider for instructions
            atInstructions = True
        elif atInstructions:
            #Instruction passed in [move X, from X, to X]
            instruction = [int(x) for x in line.split() if x.isdigit()] 
            moveHowMany = instruction[0]
            moveFrom = instruction[1]-1
            moveTo = instruction[2]-1
            # Popping and moving
            poppedItem = stackList[moveFrom][0:moveHowMany]
            for item in poppedItem[::-1]:
                stackList[moveTo].insert(0,item)
            stackList[moveFrom] = stackList[moveFrom][moveHowMany:]
            # stackList[moveTo].insert(0,poppedItem)
        elif "[" not in line:
            #Targets the label
            pass 
        else:
            # X means empty spot
            line = line.rstrip().replace("    ", " ").split(" ")
            currPos =  0 #Start at 0 to match stack name
            for seg in line:
                if "[" not in seg:
                    ## Up pos by 1
                    currPos += 1
                else:                  
                    #Create a new list if it is not in
                    if currPos >= len(stackList):
                        for i in range(currPos - len(stackList) + 1):
                            stackList.append([])
                    stackList[currPos].append(seg)
                    currPos += 1
    #             # Reset currPos
    for stack in stackList:
        print(stack[0])

                



