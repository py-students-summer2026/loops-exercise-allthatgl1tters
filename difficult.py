def one(number):
    print("\ndifficult.one:")
    print("\t", "Prime factors:", end=' ')
    for i in range(2, number + 1):
        if number % i == 0:
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print(i, end=' ')

def two (n):
    print("\ndifficult.two:")
    a = 0
    b = 1
    count = 0
    while count < n:
        total = a + b
        a = b
        b = total
        count += 1
    print("\t", f"The {n}th Fibonacci number is: {a}")

def three(word1, word2):
    print("\ndifficult.three:")
    if len(word1) != len(word2):
        print("\t", f"{word1} and {word2} are not anagrams.")
        return
    letters1 = sorted(word1.lower())
    letters2 = sorted(word2.lower())
    is_anagram = True
    for i in range(len(letters1)):
        if letters1[i] != letters2[i]:
            is_anagram = False
            break
    if is_anagram:
        print("\t", f"{word1} and {word2} are anagrams.")
    else:
        print("\t", f"{word1} and {word2} are not anagrams.")
    
def four(n):
    print("\ndifficult.four:")
    term = 2
    count = 0
    while count < n:
        print("\t", term)
        term += 2
        count += 1

def five(numbers):
    print("\ndifficult.five:")
    numbers.sort()
    length = len(numbers)
    if length % 2 == 1:
        median = numbers[length // 2]
    else:
        middle1 = numbers[length // 2 - 1]
        middle2 = numbers[length // 2]
        median = (middle1 + middle2) / 2
    print("\t", f"The median is: {median}")

def six(number):
    print("\ndifficult.six:")
    total = 0
    divisor = 1
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1
    if total == number:
        print("\t", f"{number} is a perfect number.")
    else:
        print("\t", f"{number} is not a perfect number.")

def seven(number):
    print("\ndifficult.seven:")
    total = 0
    for digit in str(number):
        total += int(digit)
    print("\t", f"The sum of the digits is: {total}")

def eight(sentence):
    print("\ndifficult.eight:")
    words = sentence.split()
    longest = words[0].strip(".,!?;:")
    i = 1
    while i < len(words):
        word = words[i].strip(".,!?;:")
        if len(word) > len(longest):
            longest = word
        i += 1
    print("\t", f"The longest word is: {longest}")

def nine(sentence):
    print("\ndifficult.nine:")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    is_pangram = True
    for letter in alphabet:
        if letter not in sentence:
            is_pangram = False
            break
    if is_pangram:
        print("\t", "The sentence is a pangram.")
    else:
        print("\t", "The sentence is not a pangram.")
    
def ten():
    print("\ndifficult.ten:")
    number = 2
    while number <= 1000:
        is_prime = True
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            print("\t", number)
        number += 1