import Animal

a1 = Animal.Animal("kitty",2,"cat")
a2 = Animal.Animal("kitty",2,"cat")
a3 = Animal.Animal("kitty",2,"dog")
a4 = Animal.Animal("kitty",2,"dog")

list=[]

list.append(a1)
list.append(a2)
list.append(a3)
list.append(a4)

for i in list:
    print(i)


def increment_age(list):
    for i in list:
        age = i.get__age()
        i.set__age(age + 1)

    for i in list:
        print(i)

increment_age(list)
def search_animal(list, type):
    count = 0
    for i in list:
        if i.get__type() == type:
            count += 1
    return count

type = input("Enter type value ")
count = search_animal(list, type)
print(count)