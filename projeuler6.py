'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

ans1=0
a1=0
for i in range(1,101):
    sq1=i**2
    ans1=ans1+sq1
    sq2=i
    a1=a1+sq2
    ans2=a1**2
    a=ans2-ans1
print(a)
