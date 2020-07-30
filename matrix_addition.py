#prewritten example (not my own, but wanted to practice...)


x = [[1,2,3],
    [4 ,5,6], 
    [7 ,8,9]]
print(x)

y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
print(y)

result = [[x[i][j] + y[i][j] for j in range 
(len(x[0]))] for i in range(len(x))]

for r in result:
    print(r)

