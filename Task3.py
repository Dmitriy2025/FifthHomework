k = 300

def delit(n):
    list1 = []
    sum = 0
    for i in range(1, n):
        if n%i == 0:
            sum += i
            list1.append(i)
    #print(sum)
    return list1
    
def comp(list1, list2):
    if list1 == list2:
        return True
    return False
    
print(delit(k))
print(delit(568))

print(comp(delit(k), delit(568)))
