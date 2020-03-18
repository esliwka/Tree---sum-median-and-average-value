from node import Node


# drzewo 1
a = Node(3)
b = Node(5)
c = Node(4)
d = Node(2)
e = Node(7)
f = Node(4)
b.setParent(a)
c.setParent(b)
d.setParent(b)
b.addChild(c)
c.addChild(e)
c.addChild(f)

# drzewo 2
a2 = Node(54)
b2 = Node(14)
c2 = Node(21)
d2 = Node(41)
e2 = Node(142)
f2 = Node(92)
g2 = Node(31)
a2.addChild(b2)
a2.addChild(c2)
b2.addChild(d2)
c2.addChild(e2)
c2.addChild(f2)
f2.addChild(g2)


print("\nTree 1:")
c.getRoot().printTree()  #pobiera korzeń i rysuje całe drzewo

print("Suma od korzenia: " + str(a.sumTreeValues()))

print("Średnia od korzenia: " + str(a.avgValue()))

print("Mediana od korzenia: " + str(a.medianValue()))

print("Suma od c: " + str(c.sumTreeValues()))

print("Średnia od c: " + str(c.avgValue()))

print("Mediana od c: " + str(c.medianValue()))

print("\nTree 2:")
a2.printTree()

print("Suma od korzenia: " + str(a2.sumTreeValues()))

print("Średnia od korzenia: " + str(a2.avgValue()))

print("Mediana od korzenia: " + str(a2.medianValue()))

print("Suma od c2: " + str(a2.sumTreeValues()))

print("Średnia od c2: " + str(c2.avgValue()))

print("Mediana od c2: " + str(c2.medianValue()))