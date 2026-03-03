a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
a.add(6)
a.remove(4)

print(a | b) #union
print(a & b) #intersecion
print(a - b) #diferencia


# Validar si un elemento existe dentro de un set
print(f"\n {20 in a}")