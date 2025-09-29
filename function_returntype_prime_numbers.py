def prime(a):

    print("Prime numbers are:",end=" ")
    for i in range(2, num+1):
        count = 0
        for j in range(1,i+1):
            if(i%j==0):
                count+=1
        if(count==2):
            print(i,end=",")
     return i
        
num = int(input("Enter the prime number upto which you want to find out prime numbers:"))
prime(num) 
