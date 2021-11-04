'''Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.

Bonus: Can you do this in one pass?'''

#* First Solution
numbers = [10, 15, 3, 7, 15]

k = int(input())
result = 0

def adding_number():
    sonuc = False
    for number in range(len(numbers)):
        for innernumber in range(len(numbers)):
            if innernumber is not number:
                result = numbers[number] + numbers[innernumber]
                if k == result:
                    sonuc = True
    return sonuc

print(adding_number())

#* Second Solution
numbers = [2,3,7,10,13,17,21]
k = 19

def equivalent_sum(numbers):
    for num in numbers:
        diff = k - num
        if diff in numbers:
            return True
    return False

print(equivalent_sum(numbers))