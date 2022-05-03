from mod.node import nodes

a = nodes('a')
b = nodes('b')

a.connectTo('1', b, '1', 1)

print(a.routing_table)
print(b.routing_table)

b.connectTo('1', a, '2', 2)
b.connectTo('2', a, '1', 9)

