# bounce.py
#
# Exercise 1.5

height = 100.0
count = 0

for x in range(10):
    height = height * 3 / 5
    count += 1
    print(str(count) + " " + str(round(height, 2)))
    
    
