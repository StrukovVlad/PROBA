# def find_short(s):
#     a = []
#     b = s.split()
#     print(b)
#     for i in range(len(b)):
#         a.append(len(b[i]))
#     l = min(a)
#     return l
#
#
#
# s = "bitcoin take over the world maybe who knows perhaps"
# w = find_short(s)




def high_and_low(numbers):
    a = max(int(x) for x in numbers.split())
    b = min(int(x) for x in numbers.split())
    numbers = str(a)+str(b)
    return numbers





numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"

print (high_and_low(numbers))