def to_hex(num):
    hex_str = hex(num)[2:].upper()
    return hex_str
num = input('Введите число: ')
hex_str = to_hex(num)
print(f'Шестнадцатеричное представление числа: {hex_str}')
print(f'Проверка результата: {hex(num)}')