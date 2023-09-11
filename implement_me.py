
def lcm(a, b):
  """compute Least Common Multiple between two integers."""

  if a > b:
       greater = a
  else:
       greater = b

  while(True):
       if((greater % a == 0) and (greater % b == 0)):
           lcm = greater
           break
       greater += 1

  return lcm

num1 = 54
num2 = 24
print("The L.C.M. is", lcm(num1, num2))


