# Дампим алфавит с матрицы за экраном
dumped = "{mcf3r'40a}ne_histd?"
# Выравниваем до 5 бит (32 символа)
alphabet = dumped + " " * (32 - len(dumped))

# Дампим память
memory = [
    0b01001,
    0b01000,
    0b10001,
    0b10010,
    0b11101,
    0b10100,
    0b11000,
    0b11110,
    0b01011,
    0b10010,
    0b11101,
    0b01001,
    0b01001,
    0b10011,
    0b11000,
    0b10110,
    0b11100,
    0b10101,
    0b10000,
    0b11011,
    0b01000,
    0b11010,
    0b11001,
    0b01000,
    0b10111,
    0b11110,
    0b01000,
    0b11111,
    0b01001,
    0b10100,
    0b11100,
    0b11101,
    0b01011
]

# Перебираем и выводим результат

results = []

for key in range(32):
    results.append("")
    for char in memory:
        results[key] += alphabet[char ^ key]

for solution in results:
    solution = ''.join(solution)
    if "mirea" in solution:
        print(solution)
