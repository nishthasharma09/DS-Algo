def generate(N):
    numbers = [1]
    for i in range(N - 1):
        if numbers[-1] % 10 == 1:
            lengthOfNumber = len(str(numbers[-1]))
            numberFormed = '1' + ('0' * lengthOfNumber)
            numbers.append(int(numberFormed))
        elif numbers[-1] % 10 == 0:
            numbers.append(numbers[-1] + 1)
    return numbers

print(generate(4))