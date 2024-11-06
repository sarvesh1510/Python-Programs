print("Bytes Example")
# Creating a byte object
b = bytes([65, 66, 67, 68])
print(b)         # Output: b'ABCD'
print(b[0])      # Output: 65
print(b[2])      # Output: 67

for byte in b:
    print(byte, end=' ')
print("\n")

# Bytearray Example
print("Bytearray Example")
# Creating Bytearray object
ba = bytearray([65, 66, 67, 68])
print(ba)        # Output: bytearray(b'ABCD')

# Modifying elements in a bytearray
ba[0] = 97       # Changing bytearray from 65 to 97
print(ba)        # Output: bytearray(b'aBCD')

for byte in ba:
    print(byte, end=' ')
print("\n")

# Memoryview Example
print("Memoryview Example:")
# Creating a byte object
b_mv = bytes([65, 66, 67, 68, 69])

# Creating a memoryview object
mv = memoryview(b_mv)
print(mv)        # Output: <memory at 0x...>

# Accessing elements through memoryview
print(mv[0])     # Output: 65

# Slicing memoryview
mv_slice = mv[1:4]
print(mv_slice.tobytes())  # Output: b'BCD'

# Creating a bytearray and a memoryview
ba_mv = bytearray([65, 66, 67, 68, 69])
mv_ba = memoryview(ba_mv)

# Modifying the original bytearray through memoryview
mv_ba[0] = 97
# Changing 'A'(65) to 'a'(97)
print(ba_mv)    # Output: bytearray(b'aBCDE')

print("WRITTEN BY SARVESH BHARDWAJ ERP :- 0221BCA062")
