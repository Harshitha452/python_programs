def perfect_no(a):
  sum=0
  for i in range(1,a):
    if(a%i==0):
      sum=sum+i
  if(sum==a):
    return "perfect number"
  else:
    return "not a perfect number"
print(perfect_no(6))
    
