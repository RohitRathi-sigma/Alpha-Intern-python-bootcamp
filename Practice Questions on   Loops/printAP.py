#Print the AP 5,7,9,11,13……


def print_AP(n):
    a = 1 
    d = 2 
    for i in range(n):
        print(a, end=" ")
        a += d

print_AP(10)
