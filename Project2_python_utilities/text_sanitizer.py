#ghadah alhoshan 443200505
def remove(text):
    result = ''
    for i in text:
        if i in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '?'):
            continue
        result += i
    return result

text = input("Enter a text: ")
result = remove(text)
print("The result text:")
print(result)
