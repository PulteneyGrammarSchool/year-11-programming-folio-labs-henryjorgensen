def min3(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return(num1)
    if num2 < num1 and num2 < num3:
        return(num2)
    if num3 <= num2 and num3 <= num1:
        return(num3)
    



print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))


def box(height, width):
    for x in range (height):
        print('*'*width)
          
box(7,5)  
print()
box(3,2)
print()
box(3,10)


my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

def find(numbers, key):
    i = 0
    for number in numbers:  
      if number == key:
           print('Found', key, 'at position', i )
      i = i + 1
    
      
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)


import random


def create_list(listsize):
    my_list = [] # Empty list
    for i in range(5):
        mynum = random.randint(1,6)
        my_list.append(mynum)



my_list = create_list(5)
print(my_list)