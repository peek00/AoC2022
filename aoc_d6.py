#Part 1
# with open("d6_input.txt") as fi:
#     for line in fi:
#         line = line.rstrip()
#         slidingWindow = []
#         index = 0
#         for char in line:
#             if char in slidingWindow:
#                 # Editing sliding Window
#                 slidingWindow = slidingWindow[slidingWindow.index(char)+1:]
#                 slidingWindow.append(char)
#                 index += 1
#             else:
#                 slidingWindow.append(char)
#                 index += 1
#                 #Truncate to 4
#                 if len(slidingWindow) == 4:
#                     break
#         print(index)           
            
#Part 2
with open("d6_input.txt") as fi:
    for line in fi:
        line = line.rstrip()
        slidingWindow = []
        index = 0
        for char in line:
            if char in slidingWindow:
                # Editing sliding Window
                slidingWindow = slidingWindow[slidingWindow.index(char)+1:]
                slidingWindow.append(char)
                index += 1
            else:
                slidingWindow.append(char)
                index += 1
                #Truncate to 4
                if len(slidingWindow) == 14:
                    break
        print(index)   
            
            
            
