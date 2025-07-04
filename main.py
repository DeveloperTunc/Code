# Some pyramid patterns
import timeit


for i in range (1,7):
    print(i*"*")

print("*********************************")

i = 6
while(i>=1):
    print(i*"*")
    i -= 1

print("*********************************")

space = 5
for i in range(1,7):
    print(space * " " + i*"*")
    space -= 1

print("************************************")

space = 0
i = 6
while(i >= 1):
    print(space*" " + "*"*i )
    space +=1
    i -= 1

print("************************************")


#FizzBuzz

for i in range(1,100):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)

#Find minimum element in array

array = [5,6,1,2,8,9,3,4]
min = array[0]
for i in array:
    if i < min:
        min = i
print(f"Minimum element in array: {min}")

#Find maximum element in array

array = [5,6,1,2,8,9,3,4]
max = array[0]
for i in array:
    if i > max:
        max = i
print(f"Maximum element in array: {max}")

#Palindrome check 

string_a = "Hello World"
string_b = "1221"

def isPalindrome(arg):
    if arg == arg[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
isPalindrome(string_a)
isPalindrome(string_b)

# Search for element in a list

list_a = [x for x in range(0,100,3)]
def search(arg:list, element:int) -> str: 
    for i in range(len(arg)):
        if arg[i] == element:
            return f"Found element:{element} in index :{i}"
    return f"Element doesn't exists"
print(search(list_a,9))

# Sort a list

list_a = [35,23]
def sortedList(arg:list) -> list:
    n = len(arg)
    for i in range(n):
        for k in range(n-i-1):
            if arg[k] > arg[k+1]:
                arg[k], arg[k+1] = arg[k+1],arg[k]
    return arg
print(sortedList(list_a))

# Remove duplicates from list

list_a = [1,11,1,22,22,3,5,7,7,1,2,3]
set_a = set(list_a)
list_a = set_a
print(list_a)









