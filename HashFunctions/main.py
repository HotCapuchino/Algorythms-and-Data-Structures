from hash_functions.ascii_hash import calculate_ascii_hash
from hash_functions.polynomial_hash import calculate_polynomial_hash

hash_size = int(input("Enter hash size: "))
hash_table_size = 2 ** hash_size
polynomial_coef = int(input("Enter polynomial coefficient, p > 1: "))
if polynomial_coef <= 1:
    print("Polynomial hash is out of range!")
    exit(-1)

with open('res/endict.txt') as f:
    hash_table_ascii = [False] * hash_table_size
    hash_table_polynomial = [False] * hash_table_size
    collisions_amount_ascii = 0
    collisions_amount_polynomial = 0
    while True:
        string = f.readline()[:-1]
        if not string:
            break
        index_ascii = calculate_ascii_hash(string) % hash_table_size
        index_polynomial = calculate_polynomial_hash(string, polynomial_coef) % hash_table_size
        # checking if there is collision for ascii method
        if not hash_table_ascii[index_ascii]:
            hash_table_ascii[index_ascii] = True
        else:
            collisions_amount_ascii += 1
        # checking if there is collision for polynomial method
        if not hash_table_polynomial[index_polynomial]:
            hash_table_polynomial[index_polynomial] = True
        else:
            collisions_amount_polynomial += 1
    print("Total collision number for ascii hash calculation is: ", collisions_amount_ascii)
    print("Total collision number for polynomial hash calculation is: ", collisions_amount_polynomial)
f.close()
