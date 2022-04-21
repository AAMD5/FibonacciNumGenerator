# Function that returns nth element of fibonacci sequence

def fib(signature, n):
    
    if n == 0:
        return []
    
    next_fib = 0
    #1, 1, 2, 3, 5, 8, 13, ...
    #p, c, n,
        #p, c, n,
    
    lst = []
    print("Starting terms for Fibonacci sequence are:", signature)
    for i in range(n):
      #print(signature[0])
      lst.append(signature[0])
      next_fib = signature[0] + signature[1]
      signature[0] = signature[1]
      signature[1] = next_fib
    
    return "The first " + str(n) + " terms of the Fibonacci sequence are: " + str(lst)

print(fib([1,1],15))