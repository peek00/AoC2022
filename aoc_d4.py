#Part 1
# with open("d4_input.txt") as fi:
#     output = 0
#     for line in fi:
#         range1, range2 = line.rstrip().split(',')
#         r1Start, r1End = range1.split("-")
#         r2Start, r2End = range2.split("-")
#         # Check range1 inside range 2
#         # If both start are the same
#         if int(r1Start) == int(r2Start):
#             #You missed out this one
#             output += 1
#         elif int(r1Start) > int(r2Start):
#             #Check if end is smaller
#             if int(r1End) <= int(r2End):
#                 # print(range1, range2)
#                 # print("Yes")
#                 output += 1
#         elif int(r1Start) < int(r2Start):
#             if int(r1End) >= int(r2End):
#                 # print(range1, range2)
#                 # print("Yes1")
#                 output += 1
#     print(output)


        
#Part 2
with open("d4_input.txt") as fi:
    output = 0
    for line in fi:
        range1, range2 = line.rstrip().split(',')
        r1Start, r1End = range1.split("-")
        r2Start, r2End = range2.split("-")
        # Check range1 inside range 2
        # If any of the numbers in both columns are the same, then they confirm overlap
        if int(r1Start) == int(r2Start) or int(r1Start) == int(r2End) or int(r1End) == int(r2Start) or int(r1End) == int(r2End):
            output += 1
        elif int(r1Start) < int(r2Start):
            if int(r1End) < int(r2Start):
                pass
            else:
                output += 1
        elif int(r1Start) > int(r2Start):
            if int(r2End) < int(r1Start):
                pass
            else:
                output += 1
    print(output)


        