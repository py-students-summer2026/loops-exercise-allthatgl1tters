def one(numbers):
    print("\nmedium.one:")
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    print('\t', f'The largest number = {largest}')

def two(numbers):
    print("\nmedium.two:")
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    average = total / len(numbers)
    print('\t', f'The average = {average}')

def three(text):
    print("\nmedium.three:")
    is_palindrome = True
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            is_palindrome = False
            break
    if is_palindrome:
        print('\t', f'"{text}" is a palindrome')
    else:
        print('\t', f'"{text}" is not a palindrome')

def four(n):
    print("\nmedium.four:")
    term = 2
    i = 1
    while i <= n:
        print('\t', term)
        term = term * 2
        i += 1

def five(numbers):
    print("\nmedium.five:")
    largest = numbers[0]
    second_largest = numbers[0]
    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number
    print('\t', f'The second largest number = {second_largest}')

def six(numbers):
    print("\nmedium.six:")
    factorial = 1
    i = 1
    while i <= numbers:
        factorial *= i
        i += 1
    print('\t', f'{numbers}! = {factorial}')

def seven(numbers):
    print("\nmedium.seven:")
    is_square = False
    for i in range(numbers + 1):
        if i * i == numbers:
            is_square = True
            break
    if is_square:
        print('\t', f'{numbers} is a perfect square')
    else:
        print('\t', f'{numbers} is not a perfect square')
    
def eight():
    print("\nmedium.eight:")
    total = 0
    number = 2
    while number <= 100:
        is_prime = True
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            total += number
        number += 1
    print('\t', f'The sum of all prime numbers between 1 and 100 = {total}')

def nine(sentence):
    print("\nmedium.nine:")
    punctuation = [',', '.', '!', '?', ':', ';']
    clean_sentence = ""
    for character in sentence:
        if character in punctuation:
            clean_sentence += " "
        else:
            clean_sentence += character
    words = clean_sentence.split()
    count = 0
    for word in words:
        count += 1
    print('\t', f'The number of words in the sentence = {count}')

def ten(list1, list2):
    print("\nmedium.ten:")
    i = 0
    print('\t', 'The common elements in the two lists are: ', end='')
    while i < len(list1):
        if list1[i] in list2:
            print(list1[i], end=' ')
        i += 1
    print()
