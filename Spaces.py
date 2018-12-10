string = input("enter the data:")
counter = 0
for z in string:
    if z == ' ' or z == '\n':
        counter += 1
print(counter)
