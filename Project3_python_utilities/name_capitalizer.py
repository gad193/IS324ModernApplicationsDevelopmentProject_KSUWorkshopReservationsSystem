#ghadah alhoshan 443200505
def name (name):
 name_split = name.split()
 for name in name_split:
     capitalize = name[0].upper()+ name[1:]
     print(capitalize)

full_name = input("Enter your full name: ")
name(full_name)