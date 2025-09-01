try:
    file = open("Names.txt", 'a')
    for i in range(3):
        name = input("Enter name: ")
        file.write(name + "\n")
    file.close()

    file = open("Names.txt", 'r')
    names = file.readlines()

    def longest_name(names):
        longest = ""
        for name in names:
            if len(name) > len(longest):
                longest = name.strip()
        return longest

    def create_file():
        output_name = input("Enter output file name: ")
        output_file = open(output_name, 'w')
        line_number = 1
        for name in names:
            output_file.write("<" + str(line_number) + ">" + name)
            line_number += 1
        output_file.close()

    print("The longest name is:", longest_name(names))
    create_file()

except FileNotFoundError:
    print("File not found")