#ghadah alhoshan 443200505
names = []
while True:
    name = input("Enter students names, or press -1 if you want exit:" )
    if name == "-1":
        break
    names.append(name)
print("1-",names)
print("2- Number of elements is:", len(names))
names.sort()
print("3- The sorted list is:",names)
print("4- ",'*'.join(names))

if "Sara" in names:
    names.remove("Sara")
    print("5- My list after removing Sara: ", names)
print("6-", tuple(names))