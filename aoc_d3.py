#Part 1
# from collections import defaultdict
# with open("d3_input.txt") as fi:
#     alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     outputSum = []
#     output = []
#     for line in fi:
#         hashTable =defaultdict(str)
#         line = line.rstrip()
#         breakPoint = len(line)/2
#         for i,char in enumerate(line):
#             if i < breakPoint:
#                 hashTable[char] = char
#             else:
#                 if char in hashTable:
#                     if char.isupper():
#                         outputSum.append((alphabetList.index(char.lower())+1)+26)
#                     else:
#                         outputSum.append((alphabetList.index(char)+1))                    
#                     output.append(char)
#                     break
#     print(sum(outputSum))

#Part 2
from collections import defaultdict
with open("d3_input.txt") as fi:
    # Create sets for all 3 items, then get the unique one via intersection
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    setList = []
    noOfSets = 0
    score = 0     
    for line in fi:
        line = line.rstrip()
        currSet = set(line)
        setList.append(currSet)
        noOfSets += 1
        if noOfSets == 3:
            # Get intersection of all 3 sets
            commonChar = set.intersection(setList[0],setList[1],setList[2])
            if list(commonChar)[0].isupper():
                score += alphabetList.index(list(commonChar)[0].lower()) + 1 + 26
            else:
                score += alphabetList.index(list(commonChar)[0]) + 1
            # Reset
            setList = []
            noOfSets = 0
    print(score)



        