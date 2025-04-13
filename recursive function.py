#  recursive function it will 
def countdown(n):
    if(n==1):
        print("blast")
    else:
        print(n)
        countdown(n-1)
countdown(10)
# infinate loop
def countdown(n):
   
        print(n)
        countdown(n-1)
countdown(10)