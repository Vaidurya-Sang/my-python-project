from my_package import my_module

print(my_module.total(1, 2, 3))
print(my_module.author)

from my_package.my_module import total
print(total(1,2,3))

from my_package.my_module import *
print(total(1,2,3))
print(author)

