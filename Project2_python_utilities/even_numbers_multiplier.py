#ghadah alhoshan 443200505
import random
def mulitiply_even(N):
    result = 1
    for i in range(2,N+1,2):
     result*=i
    return result

randon_num = random.randint(1,10)
result = mulitiply_even(randon_num)

print("The generated random number is:" ,randon_num)
print("The result of multiplying all even numbers until",randon_num ,"is:", result)