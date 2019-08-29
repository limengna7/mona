r = ["name", "age", "sex"]
n = ["lisa", "18", "girl"]

t = []
s = {}

for i in range(3):
    s[r[i]]=[n[i]]  #赋值放在字典里
    t.append(s)     #把字典储存在列表里
    i+=1
print(t)







