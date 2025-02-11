def bit_stuffing(data):
    stuffed_data = ""
    count = 0
    
    for bit in data:
        if bit == '1':
            count += 1
        else:
            count = 0
        
        stuffed_data += bit
        
        if count == 5:  # If five consecutive 1s are found, insert a 0
            stuffed_data += '0'
            count = 0  # Reset count after stuffing
    
    return stuffed_data


def bit_destuffing(stuffed_data):
    destuffed_data = ""
    count = 0
    i = 0
    
    while i < len(stuffed_data):
        destuffed_data += stuffed_data[i]
        
        if stuffed_data[i] == '1':
            count += 1
        else:
            count = 0
        
        if count == 5 and i + 1 < len(stuffed_data) and stuffed_data[i + 1] == '0':
            i += 1  # Skip the stuffed 0
            count = 0  # Reset count after destuffing
        
        i += 1
    
    return destuffed_data



data = "1111101111101111"
print(f"Original Data: {data}")

stuffed = bit_stuffing(data)
print(f"Stuffed Data:  {stuffed}")

destuffed = bit_destuffing(stuffed)
print(f"Destuffed Data: {destuffed}")
