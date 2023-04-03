a = []
print("For Binary Search array must be sorted")
count = int(input("How many elements you want to add"))
i= 0
while i < count:
    inp = int(input("Enter list elements"))
    a.append(inp)
    i+=1
print(a)
search = int(input("Enter what do you want to search"))
low_index = 0
high_index = len(a) -1
isfound = False
mid_index = 0
while low_index <= high_index:
    mid_index = (low_index + high_index)//2
    mid_number = a[mid_index]
    if mid_number == search:
        isfound = True
        break
    elif mid_number < search:
        low_index = mid_index + 1
    else:
        high_index = mid_index - 1
if isfound == True:
    print(f"The value {search} is found at index" , mid_index)
else:
    print("key is not found")