# Fizzbuzz

lst = []
for i in range(0,3):
    N = input()
    lst.append(N)
    
    for i in lst:
        #print(i)
        if i != "Fizz" and i != "Buzz" and i != "FizzBuzz":
            number = int(i)
            #print(int(i))
            index = lst.index(i)
        
        
add_value  = abs(index -3)
next_number = number + add_value
if next_number % 3 == 0 and next_number % 5 == 0:
    print("FizzBuzz")
elif next_number % 3 == 0:
    print("Fizz")
elif next_number % 5 == 0:
    print("Buzz")
else:
    print(next_number)
