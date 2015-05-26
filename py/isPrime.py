def isPrime(num):   
    # all numbers can be divided by 1, so begins with 2  
    i = 2  
    isPrime = True   
    while(i*i <= num):   
        # can be divided by i, so is not prime   
        if(num % i == 0):   
            isPrime = False   
            break  
        else:   
            i += 1  
    return isPrime   
  
print( [ i for i in range(1, 200) if isPrime(i)] )  
