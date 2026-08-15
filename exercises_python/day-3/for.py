# # # # for i in range(10):
# # # #     print(i)

# # # for i in range(1,11):
# # #     print(i)

# # for i in range(1,6):
# #     for j in range(i):
# #         print("*", end="")
# #     print()

# for i in range(6,1,-1):
#     for j in range(i):
#         print("*", end="")
#     print()

for i in range(1,6):
    for j in range(5-i):
        print(" ", end="")
    for j in range(1,i+1):
        print(j," ", end="")
    print()