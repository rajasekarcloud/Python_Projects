#Challenge: Print Half Pyramid using Loops (*)
# If the value of n is 5, this is the expected output:
#
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
for row in range(5):
    for space in range(row,5):
        print(" ",end="");
    for column in range(row+1):
        print("*",end="");
    print("\n");
