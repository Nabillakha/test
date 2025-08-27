matrix = [[1,2], 
[3,4]] 
for row in matrix: 
    for element in row: 
        print(element, end=' ') 
    print() 

# Output:
# 1 2
# 3 4

for i in range(5): 
    for j in range(i + 1): 
        print("*", end=' ')
    print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * * 

