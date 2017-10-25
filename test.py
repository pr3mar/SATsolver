import boolean

x = boolean.Variable('1')
nx = boolean.Not(x)

xornx = boolean.Or(boolean.T, x, nx)
# xandnx = boolean.And(boolean.T, x, boolean.Not(boolean.Or(x, boolean.Not(x))))
# xandnx = boolean.Not(boolean.Or(x, boolean.Not(x)))
# xandnx = boolean.Or(x, boolean.Not(x), boolean.Variable('2'))
xandnx = boolean.And(boolean.Not(boolean.Or(boolean.Not(x), boolean.Variable('3'))), boolean.Not(x), boolean.Variable('2'))

print(xornx)
print(xornx.simplify())

print(xandnx)
print(xandnx.simplify())
# print(xandnx.evaluate({'1':boolean.T, '2':boolean.T, '3':boolean.F}))
