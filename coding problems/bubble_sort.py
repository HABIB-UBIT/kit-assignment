my_list = []
count = int(input("How many elements you want to add"))
i= 0
while i < count:
    inp = int(input("Enter list elements"))
    my_list.append(inp)
    i+=1
print("You entered this array",my_list)
for i in range (len(my_list)-1):
    flag = 0
    for j in range (len(my_list)-1-i):
        if my_list[j] > my_list[j+1]:
            my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
            flag = 1
if (flag == 0):
    print("The given array is sorted")
print(my_list)

