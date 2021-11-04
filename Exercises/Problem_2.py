'''This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index
`i` of the new array is the product of all the numbers in the original array
except the one at `i`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120(2*3*4*5), 60(3*4*5), 40(4*5*2), 30(3*5*2), 24(3*4*2)]`.
If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.'''

numbers = [1, 2, 3, 4, 5]
new_array = []


def multiplication():
    result = 1
    for number in numbers:
        result = result * number
    for not_wanted in numbers:
        new_array.append(int(result / not_wanted))
    return new_array


print(multiplication())