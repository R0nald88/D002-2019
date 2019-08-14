def checker(sentence, letter):
    result = []
    for n in range(0, len(sentence)):
        if str(sentence[n]) == str(letter):
            result.append(n)
    return result
    
    
a = checker("Apple", "p") # a = [1, 2]
b = checker("Banana", "p") # b = []
c = checker("Cat", "a") # c = [1]
print(a, b, c)
