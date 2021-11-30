name = input('>>>')
ascending_order = name.split(',')
for i in range(len(ascending_order)):
     ascending_order[i] = int(ascending_order[i])
ascending_order = sorted(ascending_order, reverse=False)
print(ascending_order)
ascending_order = sorted(ascending_order, reverse=True)
print(ascending_order)