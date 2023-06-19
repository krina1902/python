d= {123:"krina",234:"kri",456:"deep",678:"dhruvin"}

print(d)
print(d.get(123))
print(d[123])
print(d.items())
print(d.keys())
print(d.pop(123))
print(d.popitem())
print(d.values())
print(d.setdefault(234))
d1={123:"krina",234:"kri",456:"deep",567:"bunny"}
d.update(d1)
print(d)

for i in d:
    print(i,":",d[i])
