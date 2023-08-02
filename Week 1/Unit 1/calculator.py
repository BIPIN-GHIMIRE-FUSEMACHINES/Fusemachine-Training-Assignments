def add(a,b):
    print(f"{a} + {b} = ", a+b)

def sub(a,b):
    print(f"{a} - {b} = ", a-b)

def mul(a,b):
    print(f"{a} * {b} = ", a*b)

def div(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    else:
        print(f"{a} / {b} = ", a/b) 

add(2,3)
sub(2,3)
mul(2,3)
