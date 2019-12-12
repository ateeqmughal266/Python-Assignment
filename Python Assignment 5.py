def factorial(num):
  assert num>0,"only positive numbers"
  factorial=1
  for i in range(1,num+1): 
    factorial = factorial * i 
  return factorial
number=int(input("Enter the number: "))
print(factorial(number))

def case(string):
  upper=0
  lower=0
  for x in string:
    if x.isupper():
      upper+=1
    elif x.islower():
      lower+=1
  return upper,"letters are capital", lower,"letters are small"

inp=input("Enter string: ")
print(case(inp))

def even(lis):
  for x in lis:
    if x %2==0:
      print (x,sep=',')

inp=int(input("Enter the number of elements in list: "))
l=[]
while inp:
  a=int(input("Enter the number: "))
  l.append(a)
  inp-=1
even(l)

def palindrome(palin):
  palin=palin.lower()
  z = palin[::-1]
  if z == palin:
      print ("This is a palindrome")
  else:
      print ("Not a palindrome")
inp=input("Enter string: ")
palindrome(inp)

def prime(num):
  if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
          
  else:  
    print(num,"is not a prime number")
inp=int(input("Enter the number: "))
print(prime(inp))

def shopping_list(*args):
  print (args)
shopping_list("bag","shirt","soap","apples","books","shoes")
