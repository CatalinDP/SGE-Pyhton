setMutable1 = set([1, 2, 3, 4, 6, 7, 8, 9, 10, 5])
setMutable2 = set([1, 2, 3, 6, 7, 8, 5, 11, 23, 12])
# print(setMutable2.difference(setMutable1))
# Que tiene el primero que no tenga el segundo

# Métodos a saber: add, clear(), copy(), difference(), discard(),
# intersection(), isdisjoint(), issubseb(), issuperset(), pop(),
# remove(), symmetric_difference(),
print(setMutable1.symmetric_difference(setMutable2))
