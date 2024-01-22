"""
Метод translate
"""
data = 'юбщс'
symbol_map = {
    ord('ю'): 'u',
    ord('б'): 'b',
    ord('щ'): 'shch',
    ord('с'): 's',
}

new_str = data.translate(symbol_map)
print(new_str)