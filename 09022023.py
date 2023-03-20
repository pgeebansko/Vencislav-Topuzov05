print("Моля въведете десетично число")
a = int(input())
c = list()
print("Molia izberete broina sistema")
y = int(input())
while a != 0:
    b = a % y
    if b == 10:
        b = 'A'
    if b == 11:
        b = 'B'
    if b == 12:
        b = 'C'
    if b == 13:
        b = 'D'
    if b == 14:
        b = 'E'
    if b == 15:
        b = "F"
    c .append(b)
    a = int(a/y)
c . reverse()
print(c)
#kjkljkljlj


