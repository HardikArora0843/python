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



fruits=["apple","garpes","watermelon",1]
print(fruits)  
print(len(fruits))               # 4
print(type(fruits))              # it will give <class 'list'>



# LOOPS, WHILE LOOP


i=1
while i<10:                    # i = 1 pe 1 print hoga then i = 2 hoga then 2 print hoga 
  print(i)
  i=i+1                   # i+=1   # here 123456789 aayega as 10 is not <10

  
# BREAK KEYWORD


i=1
while i<8:
  print(i)
  if i == 3:                  # == isliye aaya kyunki hume yahan compare karana tha 
    break               # when i will 3 it will follow condition of break and it will break 
  i=i+1


  
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