#computer understands binary language (0,1)
#0 = 0
#1 = 1
#2 = 10         jahan 1,0 ka combination aayega wo binary hoga
#3 = 11
#4 = 100
#5 = 101
#6 = 110
#7 = 111

# ASCII CODE

# a,b,c,d,......,z = 97,98,99,......,122
# A,B,C,D,......,Z = 65, 66, 67,....., 90


print(" hi this is hardik")

num1 = 10
num2 = 20
sum = num1 + num2
print(sum)

a = 10     # integer( int )
a = str(10)
print(a)

a = float(10)
print(a)

a = int(10.5)
print(a)

a = 10
a = 20        # here a = 20 likhne pe a = 10 overwrite ho gaya means ab a 20 hoga
print(a)
                
# varible have to be one word like 'hardikarora'  it can't be 'hardik arpra' but it can be 'hardik_arora'

 # Q 1
 # a = 10 ,b = 20  
 # we need to swap value of a,b and need a = 20, b = 10 as answer       
a = 10
b = 20
n = a   # means n = 10               
a =  b   # means a = 20             # this is long way with third variable
b = n   # means b = 10 
print(a)
print(b)         

a = 10
b = 20
a,b = b,a          # this is short way without any variable  
print(a)
print(b)

a = 10 
b = 20 
sol = (a+b)**2
print(sol)


name="tony stark"
print(name.upper())                 # TONY STRARK
print(name.find("s"))            # it will give index of element entered
print(name.replace("tony","mony"))
print("tony" in name)           # it will ki tony us present in name or not




# CONDITIONAL STATEMNTS
# IF ELSE STATEMENTS




a = 10 
b = 20
if b>a:      # in if else condition if, else ke baad ':' aayaga
    print(" b is greater than a")     # indentation means a mandatory space which has to be given, like here there is space before print

if 5>6:
    print(" false ")
else:
    print("true")





# IF ELSE LADDER





a=10
b=20
if b>a:                # here first statment is true therefore it will not procced further and will print'hardik'
  print("hardik")          
elif a==b:            # elif works as if statement but we can use it many times 
  print("arora")
else:
  print("hardik arora")        # to compare two numbers == is used

       
 
hardik=65
if hardik>90:
  print("congo")
elif hardik>80 and hardik<=90:
  print("not bad")
elif hardik>70 and hardik<=80:
  print("b grade")
else:
  print("hard work")              # by using 'and' it will analyse both statements then will give answer




import random
random.random()                # by this any random number wil come but here float is coming


import random 
random.randint(1,8)               #by this any int value wil come ranging 1 to 8




# SLICING




b="cipher schools"             # by this 3 se 6 ke alawa sab hat jayega. Here c(0) i(1) p(2) h(3)
print(b[3:6])

a="hardik arora"           # dik
print(a[3:6])


c="CIPHERSCHOLLS"
print(c.lower())
print(c.replace("CI","PI"))


x= "cipher"
y= "schools"
sum=x+y
print(sum)            # by this cipherschools will come
sum=x+" " +y          # by this cipher schools will come
print(sum)



#  x+=2
#  x=x+2



#  LISTS



fruits=["apple","garpes","watermelon",1]
print(fruits)  
print(len(fruits))               # 4
print(type(fruits))              # it will give <class 'list'>

marks=[96,98,97]
print(marks[1])

marks.append(99)         # append means add karna 
print(marks)           # [96,98,97,99]

marks.insert(1,99)    # by this 99 will enter at specified index
print(marks)           # [96,99,98,97]





# LOOPS, WHILE LOOP





i=1
while i<10:                    # i = 1 pe 1 print hoga then i = 2 hoga then 2 print hoga 
  print(i)
  i=i+1                   # i+=1   # here 123456789 aayega as 10 is not <10
  

i=1
while i<=5:
  print(i * "*")
  i=i+1  

 


  
# BREAK AND CONTINUE KEYWORD


i=1
while i<8:
  print(i)
  if i == 3:                  # == isliye aaya kyunki hume yahan compare karana tha 
    break               # when i will 3 it will follow condition of break and it will break 
  i=i+1
  
  
student=["ram","hardik","arora","anurag"]
for i in student:
  if i == "ram":
    continue       # by continue this loop will be skipped means ram will be skippd
  print(i)




# ROCK PAPER SCISSORS




import random
print("welcome to the game")                             # uc is userchoice, cc is computerchoice, cs is computer selection of rock paper scissors 
uc = input("enter either rock or paper or scissors")
cc = ["rock","paper","scissors"]                        # we have used list here bcoz at a time multiple objects ko cjoose karwana hai
cs = random.choice(cc)
print(cs)
if uc == "rock" and cs == "paper":
  print("you lost")
elif uc == "rock" and cs == "rock":
  print("tie")
elif uc == "rock" and cs == " scissors":
  print("you won")
else:
  print ("game over")



  
  # FOR LOOP





from typing import OrderedDict


student=["anurag","harshit", "vinod"]
for i in student:                        # in this i will enter in student and see every words and it will print those 
    print(i)

for i in "anurag":
    print(i)                            # here i enter anurag and print every letter

student=["anurag","harshit", "vinod"]
for i in student:
    print(i)
    if i ==  "harshit":
         break

for i in range(5):
    print(i)

student=["anurag","harshit", "vinod"]        # this is called  NESTED LOOPING
color=["red","blue","green"]
for i in student:
    for j in color:
        print(i,j)


i = 1
while i < 5:            # when i = 1 then i < 5 true phir next pe aayenge, then j=1 then j<10 true hai then j = 2 hoga phir  upar jayega 
    j = 1               # and i = 1 hoga but j =  2 hoga 
    while j < 10:
        print( i*j)
        j = j + 1
    i = i + 1  
    print("\n")





# ANOTHER DATA TYPE:TUPLE
# UNCHANGEABLE & ORDERED



 
a = ("anurag","vinod","hardik")   # ( ) means tuple , [ ] means lists
print(a)
for i in a:
    print(i)

a = ("anurag","vinod","hardik")     
if "anurag" in a:
    print("yes")

 
a = ("anurag","vinod","hardik")     
b = list(a)
b[1] = "virus"                       # this is the to change value in tuple jabki tuple unchangable hai
a = tuple(b)
print(a)


a = ("anurag","vinod","hardik")
b = (1,2,3)
c = a+b                                    # by this we can add date in tuple by entering data in tuple form[ ( ) ]
print(c)     

marks=(96,98,97,97,97)
print(marks.count(97))




# ANOTHER DATA TYPE IS SET
# UNORDERED & UNCHANGABLE





a = {"anurag","hardik","vinod"}      #  { } means set  
print(a)

for i in a:
    print(i)

a = {"anurag","hardik","vinod"}  
a.add("virus")
print(a)

a = {"anurag","hardik","vinod"}  
b = {1,2,3}
c = a.union(b)                       # .union is used to add date in set  
print(c)






# ANOTHER DATA TYPE : DICTI0NARY
# ORDERED, CHANGEABLE ,NO DUPLICATE
# WORKS ON THE CONCEPT OF KEY AND VALUE





a = {
    "name":"hardik",
    "company":"cipher schools",     # this is synntax for dictionary 
    "college":"LPU"
}
print(a)


a = {
    "name":"hardik",
    "company":"cipher schools",     
    "college":"LPU"
}
print(a["name"])                           #  by this we get data stored in "name"
a["degree"] = "engineering"
print(a.keys())                            # keys is used when we need object in which we will save data
print(a)


 
def hardik():           # here function ' hardik ' is defined               
  print(" Hi I am a user defined function hardik")        # here ' hardik ' function is given a task
  
hardik()          # here we have called a function and task is performed which is given to function 'hardik'


 # paramterised function, function capable of accepting value
 
def pr(name):         # here function is defined with variable name 
   print("hi my name is " + name)    # task is given       
pr("hardik")   # here function is called with value 'hardik'  by this name == hardik hoga    

def pr( first_name, last_name):         # function defined
  print(" hi my name is " + first_name + "" + last_name)      # task is given         
pr("hardik"," arora")                 # function is called  

def pr(*name):                      # '*'  is used to call multiple elements for only one variable 'name'
  print("my name is " + name[2])
pr("hardik","arora","anurag","mishra")      # here multiple elements are called 

def pr( name1, name2, name3):         
  print(" hi my name " + name3)
pr( name1="hardik",name2="arora", name3="anurag")  

def pr(name):             
  for i in name:
    print(i)
name=["anurag","mishra","cipher"]
pr(name)   

# return

def pr(n):                      
  return n*5    # by return, the value of 25 is returned to machine but as we haven't said to print so it will not print
pr(5)

def pr(n):
  return n*5               
print(pr(5))         


# recursion function calls itself to perform task  

def factorial(x):
  if x==1:          # when we call factorial(4) then x=4 then return(4*factorial(3)) , here also factorial(3) will call and then again x=3 hoga it will return (3*factorial(2)) and then factorial (2) is called then x=2 hoga then it will return (2*factorial(1)) then factorial(1) is called and x=1 it will return 1   
    return 1        
  else:
    return(x*factorial(x-1))
print(factorial(4)) 

def sum(x):
  if x<=1:
    return 1
  else: 
    return(x + sum(x-1))
print(sum(5))   
      
 
# reverse a number

numb= int(input("Enter the number: "))
revs=0
while (numb>0):
  remainder=numb%10
  revs=(revs*10) + remainder       
  numb= numb//10
print(revs)  


# simple calculator

def add(x,y):
  return x+y
 
def sub(x,y):        # function is defined
  return x-y


def mul(x,y):
  return x*y


def div(x,y):
  return x/y

print("select the operation that you want to perform")
print("1.Addition")
print("1.subtract")
print("1.multiply")
print("1.division")

choice = input("choose 1/2/3/4")    
#if choice in ('1','2','3','4'):
n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
  
if choice=='1':
  print(add(n1,n2))
elif choice=='2':
  print(sub(n1,n2))       # here function is called 
elif choice=='3':
  print(mul(n1,n2))
elif choice=='4':
  print(div(n1,n2))
else:
  print("select the correct option")                    
  
  
a=int(input("Enter the number: "))
if a%2==0:
  print("even")
else:
  print("odd") 
 
 
num = int(input("Enter the number")) 
count = 0
i = 1
while i <= num:
  if num % 1 == 0:  
    count = count + 1    
  i = i + 1
if count == 2:
  print("is prime")
else:
  print("not a prime")
  
# ARMSTRONG NUMBER
# is a number sum of digits**len(a)
# a=153 if  1*1*1 + 2*2*2 + 3*3*3 = 153 then it is armstrong number
# a=12 if 1*1 + 2*2 = 12 then it is armstrong number 


# PALINDROME
# a= nitin from L to R and R to L is same then palindrome

# TO REVERSE A STRING USE  a[::-1] 

a=input()             # by :: jo humne index enter kiya wahan se non stop jayega 
print(a[::-1])           # like -1 put kiya hai to last se continous print hoga




# IMPORT MATH


import math
print(dir(math))
 
 
import math
print(math.sqrt(4))
   
   
     
  
    



























                     