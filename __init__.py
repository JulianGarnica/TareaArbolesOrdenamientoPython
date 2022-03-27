from tree import Tree
# (5, 3, 4, 2, 1, 6)

arrayOrdernar = (5, 3, 4, 2, 1, 6, 8, 7, 9, 11, 10)

arbol = Tree(arrayOrdernar[0])

for numeroIterado in arrayOrdernar[1:]:
  arbol.insert(numeroIterado)

arbol.printValues()