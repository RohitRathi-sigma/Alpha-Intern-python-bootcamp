#. Print the GP 6, 18, 54, 162

def print_GP(n):
    a = 1
    r = 3  
    for i in range(n):
        print(a, end=" ")
        a *= r

print_GP(4)
