def calculate_ascii_hash(string):
    total_size = 0
    for char in string:
        total_size += ord(char)
    return total_size
