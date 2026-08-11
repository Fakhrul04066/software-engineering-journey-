def result(*marks,n):
    return sum(marks)/n
print(result(40,90,39,75,n=4))

#highest mark
def high(*marks):
    return max(marks)

print(high(4,4,5,3,5,8))