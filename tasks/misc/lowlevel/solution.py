# Dump of alphabet from the matrix behind the screen padded to 5 bit length (32 characters)
alphabet = "d4a_rs3i'0mf}enh5t{c"
alphabet += "?" * (32 - len(alphabet))

# Dump of ring memory
data = [
    0b11110,
    0b11011,
    0b10011,
    0b10100,
    0b01100,
    0b01101,
    0b11101,
    0b11011,
    0b11001,
    0b11110,
    0b11000,
    0b10101,
    0b01100,
    0b11100,
    0b10010,
    0b01100,
    0b01111,
    0b10110,
    0b01100,
    0b01110,
    0b11111,
    0b10000,
    0b11001,
    0b11010,
    0b10111,
    0b10001,
    0b01101,
    0b11000,
    0b11011,
    0b10011,
    0b11101,
    0b11100,
    0b10111
]

for key in range(32):
    # Data array is reversed due to dump direction which was wrong initially
    print(f"{key:2d} - ", end='')
    for char in data[::-1]:
        print(alphabet[(char ^ key) & 0b11111], end='')
    print()

# Output determines the key value of 29
# Rotation is needed because data dump started at a random position in ring memory
def rotate(l, n):
    return l[n:] + l[:n]

for char in rotate(data[::-1], 8):
    print(alphabet[(char ^ 29) & 0b11111], end='')

# mireactf{th4t's_r3d5t0n3_m4dn3s5}