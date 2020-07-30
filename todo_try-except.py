todos = ["learn python", "attack rest of bootcamp", "graduate and conquer the world!"]

print("Here's My Todo List:")
print("First:", todos[0])
print("Second:", todos[1])
print("Third:", todos[2])

try:
    print("This item does not exist:", todos[3])
except IndexError:
    print("What more do you want?! Youve already conquered the world!")
