#!/usr/bin/env python
# coding: utf-8

# In[5]:


##Q3. Write a program to check if two strings are a rotation of each other?


def checkString(s1, s2, indexFound, Size):
    for i in range(Size):
     
        
        if(s1[i] != s2[(indexFound + i) % Size]):
            return False
         
        
    return True
 

s1 = "abcd"
s2 = "cdab"
 
if(len(s1) != len(s2)):
    print("s2 is not a rotation on s1")
else:
     
    indexes = []
    Size = len(s1)
    firstChar = s1[0]
    for i in range(Size):
        if(s2[i] == firstChar):
            indexes.append(i)
 
    isRotation = False
 
    
    for idx in indexes:
 
        isRotation = checkString(s1, s2, idx, Size)
 
        if(isRotation):
            break
 
    if(isRotation):
        print("s2 is rotation of s1")
    else:
        print("s2 is not a rotation of s1")
 


# In[11]:


##Q4. Write a program to print the first non-repeated character from a string?

from collections import Counter

def repeatFunc(myStr):
    
    freq = Counter(myStr)
    
    for i in myStr:
        
        if(freq[i] == 1):
            
            print(i)
            
            break


myStr = "janeshwar"

repeatFunc(myStr)


# In[ ]:


##Q7. Write a program to convert prefix expression to infix expression.

def infixToPostfix(expression): 

    stack = [] # initialization of empty stack

    output = '' 

    

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output+= character

        elif character=='(':  # else Operators push onto stack

            stack.append('(')

        elif character==')':

            while stack and stack[-1]!= '(':

                output+=stack.pop()

            stack.pop()

        else: 

            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:

                output+=stack.pop()

            stack.append(character)

    while stack:

        output+=stack.pop()

    return output


expression = input('Enter infix expression ')

print('infix notation: ',expression)

print('postfix notation: ',infixToPostfix(expression))


# In[ ]:


##Q9. Write a program to reverse a stack.



class Stack:
  
    
    def __init__(self):
        self.Elements = []
          
   
    def push(self, value):
        self.Elements.append(value)
        
   
    def pop(self):
        return self.Elements.pop()
    
    def empty(self):
        return self.Elements == []
      
    
    def show(self):
        for value in reversed(self.Elements):
            print(value)
  

    def BottomInsert(s, value):
        
        if s.empty(): 
          
      
        s.push(value)
  
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
  

  def Reverse(s):
        
        if s.empty():
            pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
  
stk = Stack()
  
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
  
print("Original Stack")
stk.show()
  
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# In[ ]:


largest = None

smallest = None

while True:

        num = input("Enter a number: ")

        if num == 'done':

            break

        try:

            fnum = float(num)

        except:

            print("Invalid input")

            continue

      lst = []

numbers = int(input('How many numbers: '))

for n in range(numbers):

    lst.append(num)

print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
    largest = None

smallest = None

while True:

        num = input("Enter a number: ")

        if num == 'done':

            break

        try:

            fnum = float(num)

        except:

            print("Invalid input")

            continue

      lst = []

numbers = int(input('How many numbers: '))

for n in range(numbers):

    lst.append(num)

print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))


# In[ ]:





# In[ ]:


##Write a program to find all pairs of an integer array whose sum is equal to a given number?
def printPairs(arr, n, sum):
 
    
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep = "")
 
 

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
printPairs(arr, n, sum)
 


# In[ ]:





# In[ ]:





# In[ ]:




