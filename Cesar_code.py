eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

print("Выберите язык: aнглийский/русский (e/r)")
language = input()
print("Выберите шифрование: шифрование/дешифрование (c/d))")
encrypt = input()
print("Введите ключ шифрования")
key = int(input())
print("Введите фразу")
phrase = input()


def encryption(encrypt, key, language, phrase):
    if language == 'r':
        quantity_symbol = 32
    if language == 'e':
        quantity_symbol = 26
    if encrypt == 'd':
        key = - key
    for i in range(len(phrase)):
        if phrase[i].isalpha():
            if phrase[i] == phrase[i].upper():
                for j in range(quantity_symbol):
                    if quantity_symbol == 32:
                        if phrase[i] == rus_upper_alphabet[j]:
                            print(rus_upper_alphabet[(j + key) % quantity_symbol], end='')
                            break
                    if quantity_symbol == 26:
                        if phrase[i] == eng_upper_alphabet[j]:
                            print(eng_upper_alphabet[(j + key) % quantity_symbol], end='')
                            break
            elif phrase[i] == phrase[i].lower():
                for j in range(quantity_symbol):
                    if quantity_symbol == 32:
                        if phrase[i] == rus_lower_alphabet[j]:
                            print(rus_lower_alphabet[(j + key) % quantity_symbol], end='')
                            break
                    if quantity_symbol == 26:
                        if phrase[i] == eng_lower_alphabet[j]:
                            print(eng_lower_alphabet[(j + key) % quantity_symbol], end='')
                            break
        else:
            print(phrase[i], end='')


encryption(encrypt, key, language, phrase)
