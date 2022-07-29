# 1)From the given list of string remove string which is substring of other

# Example : input = [‘work’,’office’,’work from home’]

# Output = [’office’,’work from home’]

Input_Str = sorted(list(input().split(',')))# #[‘work’,’office’,’work from home’]
Output_str = []

for s in Input_Str:
    for i in range(Input_Str.index(s)+1,len(Input_Str)):
        if s in Input_Str[i]:
            break
    else:
        Output_str.append(s)
print(f'Output:{Output_str}')


# 2)find all possible palindromes from the given string and give the no of substrings need to be removed to get that palindrome

# Example : Input : ‘acscyini’

# Output : csc : 2,ini : 1

# Explanation : To get ‘csc’ from the given string we need to remove ‘a’ and ‘yini’ so csc : 2

# To get ‘ini’ from the given string we need to remove ’acscy’ so ini : 1

Input_Str = input('enter string:') 
Output = []

for i in range(len(Input_Str)):
    for j in range(i+1,len(Input_Str)):
        if Input_Str[i] == Input_Str[j]:
            temp = Input_Str[i:j+1]
            if temp == temp[::-1]:
                if i > 0 and j < len(Input_Str)-1:
                    count = '2'
                    Output.append(str(temp+':'+count))
                elif i == 0 and j == len(Input_Str)-1:
                    count = '0'
                    Output.append(str(temp+':'+count))
                elif i == 0 or j == len(Input_Str)-1:
                    count = '1'
                    Output.append(str(temp+':'+count))

print(*Output,sep = ',')

# 3) You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

# Examlpe :
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
# the max area of water (blue section) the container can contain is 49.

input1 = list(map(int,input().split()))
max_area = 0
for i in range(len(input1)):
    height = input1[i]
    index = i
    for j in range(len(input1)-1,i,-1):
        width = j-index
        length = min(height,input1[j])
        current_area = length*width
        if current_area > max_area:
            max_area = current_area
print(max_area)



# 4) Write a program to display only those numbers from a list that satisfy the following conditions

# · The number must be divisible by five

# · If the number is greater than 150, then skip it and move to the next number

# · If the number is greater than 500, then stop the loop

Input = list(map(int,input().split()))
Output = []
for num in Input:
    if num%5 == 0 and num <= 150 :
        Output.append(num)
    elif num > 150:
        continue
    elif num > 500:
        break
print(Output)


# 5) Given an integer array. find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# Input : [2,3,-2,4]

# Output : 6

# explanation : [2,3] has largest product 6

Input1 = list(map(int,input().split()))
max_product = 0
current_product = 1
for window_size in range(2 , len(Input1)+1):
    for i in range((len(Input1)-window_size)+1):
        for j in range(window_size):
            current_product *= Input1[i+j]
        if current_product > max_product:
            max_product = current_product
        current_product = 1
print(max_product)


#6)Write a program to find the sum of series: 1 + 1/2 + 1/3 + ….. + 1/N.

N = int(input("enter N value:"))
sm = 0
for i in range(1,N+1):
    sm += (1/i)
print(sm)

#7) convert binary number to decimal and hexadecimal

def binary_to_decimal(b):
    return int(b,2)
def binary_to_hex(b):
    h = binary_to_decimal(b)
    return hex(h)
print(binary_to_decimal('1100'),binary_to_hex('1111'))

#8)Write a generator function to return sequence of Fibonacci series.

def fibonacci_series():
    first = 1
    second = 1
    while True:
        yield first
        third = first + second
        first = second
        second = third
        
seq = fibonacci_series()
r = int(input('Enter length of sequence:'))
for num in range(r):
    print(next(seq), end=' ')

#9)Find the list of anagrams from the given paragraph.

paragraph = input()
paragraph = paragraph.replace(' ' , '@' )
paragraph = paragraph.replace('.' , '@')
paragraph = paragraph.replace('-' , '')
words_list = paragraph.split('@')
anagrams = []
for word in words_list:
    for next_word in words_list:
        if next_word == word:
            continue
        if sorted(word.lower()) == sorted(next_word.lower()) and next_word not in anagrams:
            if word not in anagrams:
                anagrams.append(word)
            anagrams.append(next_word)
print(anagrams)


# 10) Get the difference between max and min number can be formed from input number

# ex: input 126345

# output 530865

# explanation => 654321-123456

num = sorted(list(input()))
diff = int(''.join(num[::-1]))-int("".join(num))
print(diff)

# 11) find whether parentheses in string is balanced or not

# ex : "((a)(kd.))" --> True

# "((())" --> False

input_1 = input()
stack = []
Trigger = 1

for s in input_1:
    if s in ('(' , '{' , '['):
        stack.append(s)
    else:
        if len(stack) == 0:
             Trigger = 0
             break
        if (s == ')' and stack[-1] == '(') or (s == '}' and stack[-1] == '{') or (s == ']' and stack[-1] == '['):
            stack.pop()
        else:
            Trigger = 0
            break  
if len(stack) != 0:
    Trigger = 0
if Trigger == 1:
    print(True)
else:
    print(False)


# 12) get unique and common numbers from 2 input list

# ex: first input -> 1 5 6 8 7 3

# second input -> 8 6 7 9 2

# output - > common -> [6,8,7]

# unique -> [1,5,3,9,2]

#i)
finput=list(map(int,input().split())) #[1,5,6,8,7,3]
sinput=list(map(int,input().split())) #[8,6,7,9,2]
common=[]
unique=[]
tlist=list(set(finput+sinput))
for num in tlist:
    if (num in finput) and (num in sinput):
        common.append(num)
    else:
        unique.append(num)
print('common->{0}\nunique->{1}'.format(common,unique))

#ii)
finput=set(map(int,input().split()))
sinput=set(map(int,input().split()))
common=finput & sinput
unique=finput ^ sinput
print(common,unique)

# 13) form the largest number from the given list of non negative numbers

# ex: [3,8,5,9,98,101] -> 998853101
#101 and 98 from the list are not separated

from itertools import permutations     

list1 = list(map(int, input("Enter Elements of the List: ").split()))

perm = map(str,permutations(list1))   
res = [] 
for i in perm:
    temp=''
    for j in i:
       if j not in ('(',')',',',' '):
        temp +=j
    res.append(int(temp))
print(max(res))

# 14) Get first non-repeating character from given string

# ex: abcdcd --> a

# abacd ----> b

s=input('enter a string:')
for i in range(len(s)):
    if s.count(s[i])==1 :
        print(f'{s}---->{s[i]}')
        break


# 15) form the below pattern based on the input number(no of iteration should not exceed 1):

# input ->6

# output ->

# 1

# 2 2

# 3 3 3

# 4 4 4 4

# 5 5 5 5 5

# 6 6 6 6 6
#i)
input_num=int(input())
for i in range(input_num+1):
    print(f"{i} "*i,sep=' ')
    print()

#ii)
def pattern(limit,i = 1):
    if limit <= 0:
        return
    print(f'{i} '*i)
    pattern(limit-1, i+1)
        
pattern(int(input()))