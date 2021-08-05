def factorial(val):
    if(val == 1 or val == 0):
        return 1
    else:
        return (val*factorial(val-1))

def permutationsCalculator(n,k):
    if(k > n):
        return 0;
    else:
        nFact = factorial(n)
        nMinusk = factorial(n-k)
    return(nFact/nMinusk)

def combinationsCalculator(n,k):
    if(k > n):
        return 0;
    else:
        nFact = factorial(n)
        nMinusk = factorial(n-k)
        kFact = factorial(k)
    return(nFact/(nMinusk*kFact))

        
while True:
    try:
        a = int(input("Enter how many things you want to arrange: "))
        while(a < 0):
            a = int(input("Enter a positive number: "))
    except ValueError:
        print("Enter a valid entry")
        continue
    else:
        break
while True:
    try:
        b = int(input("Enter how many things you want to arrange: "))
        while(b < 0):
            b = int(input("Enter a positive number: "))
    except ValueError:
        print("Enter a valid entry")
        continue
    else:
        break
order = input("Does order matter? (Enter 'y' for yes or 'n' for no): ")
while(order != 'y' and order !='n'):
    order = input("Please enter a valid input: ")
if(order == 'y'):
    c = permutationsCalculator(a,b)
else:
    c = combinationsCalculator(a,b)
c = int(c)
a = str(a)
b = str(b)
c = str(c)
print("There are " + c + " ways to arrange " + a + " things in " + b + " things")
