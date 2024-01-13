#Q1. Create one variable containing following type of data:
#(i) string
#(ii) list
#(iii) float
#(iv) tuple
Answer
a='kawya is a student of PWskills'
b=[1,2,3,4.5,'kawya', 4+5J]
c=9.5
d=(5,'kawya', 5.4 )

print(type(a), type(b), type(c), type(d))

output
<class 'str'> <class 'list'> <class 'float'> <class 'tuple'>


#Q2. Given are some following variables containing data:
#(i) var1 = ‘ ‘
#(ii) var2 = ‘[ DS , ML , Python]’
#(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
#(iv) var4 = 1.
#What will be the data type of the above given variable.

#Answer
#1) string
#2) string
#3)list
#4)float

#Q3. Explain the use of the following operators using an example:
#(i) /
#(ii) %
#(iii) //
#(iv) **

#1) /, it gives the Quotient in the Output
4/2
2.0

#2) %, it gives the remainder
4%2
0

#3) //, it gives the quotient by making it to equivalent integer
4//2
2

#example 2)
5//2
2

#4) **, it is a exponential operator, which takes the right hand side value to the power of the left hand side value
2**2
4

#Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the element and its data type.
a=[2, 4.5, 'kawya', True, 5+8j, False, 'pwskills', 4,99.0, 89+4J, 100]
for i in a:
    print(i,type(i))

out put
2 <class 'int'>
4.5 <class 'float'>
kawya <class 'str'>
True <class 'bool'>
(5+8j) <class 'complex'>
False <class 'bool'>
pwskills <class 'str'>
4 <class 'int'>
99.0 <class 'float'>
(89+4j) <class 'complex'>
100 <class 'int'>


#Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many times it can be divisible.
a=int(input())
b=int(input())
while a%b==0:
    print('a is divisible by b', 'and a is divisible by b for', a/b, 'times')
    break
else:
    print('a is not divisible by b')
out put
 4
 2
a is divisible by b and a is divisible by b for 2.0 times

#Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is divisible by 3 or not.
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
type(a)
list

for i in a:
    if i%3==0:
        print(i, 'is divisible by 3')
    else:
            print(i, 'is not divisible by 3')
output
1 is not divisible by 3
2 is not divisible by 3
3 is divisible by 3
4 is not divisible by 3
5 is not divisible by 3
6 is divisible by 3
7 is not divisible by 3
8 is not divisible by 3
9 is divisible by 3
10 is not divisible by 3
11 is not divisible by 3
12 is divisible by 3
13 is not divisible by 3
14 is not divisible by 3
15 is divisible by 3
16 is not divisible by 3
17 is not divisible by 3
18 is divisible by 3
19 is not divisible by 3
20 is not divisible by 3
21 is divisible by 3
22 is not divisible by 3
23 is not divisible by 3
24 is divisible by 3
25 is not divisible by 3

#Q7. What do you understand about mutable and immutable data types? Give examples for both showing this property.
#Immutable date type: A data type which cannot be eddited, which means we cannot do any changes in terms of adding, removing, replacing with the help of index value.
#example
a='kawya, 3, 4'
type(a)
str

a[0]=p
NameError                                 Traceback (most recent call last)
Cell In[32], line 1
----> 1 a[0]=p

NameError: name 'p' is not defined

#Mutable data type: A data type which can be eddited, which means we can do any changes in terms of adding, removing, replacing with the help of index value.
b=[10,5.6,'kawya']
type(b)
list
b[0]=50
b
[50, 5.6, 'kawya']
