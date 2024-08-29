marks=(80,68,97,46,97,46,75,75,97)

print(marks)
print(marks[2])
print(len(marks))

for i in marks:
    print(i)

if 37 in marks:
    print('number exists')
else:
    print('no number')

dummy=(42,36,47,85,14,26)

print(dummy)

del dummy


m1=list(marks)
print(m1)
m1[1]=70
print(m1)

m=tuple(m1)

print(m)

x=m.index(97)
print(x)

y=m.index(46,2,7)
print(y)