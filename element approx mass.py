from element_name import (elem, num)
element_nm = elem
element_atomic_number = num
def element_mass(n):
    double = n + n
    converted = str(double)
    return converted
output = map(element_mass, element_atomic_number)
output_list = list (output)
def attaching(a, b):
    return a , b
output_final = map(attaching, element_nm, output_list)
final_result = list(output_final)
string_output = '\n'.join([str(i) for i in final_result])
print(string_output)
