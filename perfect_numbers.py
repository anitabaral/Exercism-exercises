def classify(number):
    if number <= 0:
        raise ValueError("Not a natural number")
    total = sum(num for num in range(1, number) if number % num == 0 )
    if total == number:
        return "perfect"
    elif(total < number):
        return "deficient"
    else:
        return "abundant"

        
