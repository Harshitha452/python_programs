n1=24
n2=42
for i in range(max(n1,n2),1+(n1*n2)):
    if i%n1==i%n2==0:
        lcm=i
        break
print('lcm of n1 and n2 is:',lcm)
