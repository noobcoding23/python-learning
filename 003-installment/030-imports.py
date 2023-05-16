# import math
# from math import sqrt, pi # Incase you only want to import sqrt and pi from math module
# from math import * # Here we are importing everythin available in math module. However it is not recomended to do that cause it can lead to confusion and make it hard to understand where specific function and variables are coming from
# from math import pi, sqrt as s # Import specific functions or variables using 'as' keyword
import math as m
import time as tm
from jk import welcome, jkp
# from jk import * # Importing everything inside jk module

# result = s(9) * pi
# sqrt(x) returns square root of x
result = m.sqrt(9) * m.pi
print(result)
print()
print(dir(m))
print()
print(dir(tm))
print()
print(m.nan, type(m.nan))
print()
welcome()
print()
print(jkp)
