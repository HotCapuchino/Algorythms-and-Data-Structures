def calculate_polynomial_hash(string, p_coeff):
    power = 0
    total_size = 0
    for char in string:
        total_size += ord(char) * p_coeff ** power
        power += 1
    return total_size
