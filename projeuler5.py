'''What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 leaving reminder 0'''

x=0
for i in range(1,1000000000):
    x=0
    for j in range(1,21):
        if(i%j==0):
            x=x+1
            if(x==20):
                print(i)
