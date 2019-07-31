import random
def Process(i):
    rand= random.randint(2000,100000000)
    def isPrime(n):
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True
    if isPrime(rand):
        print(rand)