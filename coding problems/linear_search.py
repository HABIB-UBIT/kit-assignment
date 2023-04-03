my_list = []
count = int(input("How many elements you want to add"))
i= 0
while i < count:
    inp = int(input("Enter list elements"))
    my_list.append(inp)
    i+=1
print(my_list)
search = int(input("Enter what do you want to search"))
for i in range (len(my_list)):
    if my_list[i] == search:
        print(f"Index of {search} is" , i)
    i=i+1




