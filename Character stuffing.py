FLAG = "F"  # Special flag character
ESC = "E"   # Escape characte
def character_stuffing(data):
    stuffed_data = ""
    for char in data:
        if char in (FLAG, ESC): 
            stuffed_data += ESC + char
        else:
            stuffed_data += char
    return FLAG + stuffed_data + FLAG  
def character_destuffing(stuffed_data):
    destuffed_data = ""
    i = 1  # Start after initial FLAG
    while i < len(stuffed_data) - 1:  # Ignore end FLAG
        if stuffed_data[i] == ESC:  # If ESC is found, skip it
            i += 1
        destuffed_data += stuffed_data[i]
        i += 1
    return destuffed_data
original_data = "ABCFDEFGF"  # Contains FLAG 'F'
stuffed = character_stuffing(original_data)
print("Stuffed Data:", stuffed)
destuffed = character_destuffing(stuffed)
print("Destuffed Data:", destuffed)
