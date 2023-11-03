def s_box(input_value):
    sbox_values = [3, 1, 0, 2]
    return sbox_values[input_value]

def differential_uniformity(sbox_function):
    # Dynamically determine the field size based on the S-box definition.
    field_size = len(sbox_values)  # Directly determine the size from sbox_values
    max_count = 0

    # Iterate over all possible input and output differences
    for a in range(1, field_size):  # We skip a=0 because it's trivial
        for b in range(1, field_size):  # Similarly, we skip b=0
            count = sum(1 for x in range(field_size) if sbox_function(x ^ a) ^ sbox_function(x) == b)
            
            if count > max_count:
                max_count = count
                
    return max_count

sbox_values = [3, 1, 0, 2] 
print("Differential Uniformity of the S-box:", differential_uniformity(s_box))
