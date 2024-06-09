k = 300

def delit(n):
    sum = 0
    list1 = []
    for i in range(1, n):
        if n % i == 0:
            sum += i
            list1.append(i)
    return sum, list1

def comp(number1, list1, number2, list2):
    if list1 == list2 and number1 == number2:
        return True
    return False

# a = delit(k)
# b, c = a[0], a[1]

# d = delit(b)
# e, f = d[0], d[1]

# print(comp(b, c, e, f))

# print(b)
# print(c)
# print(e)
# print(f)

print(delit(220))
print(delit(284))
