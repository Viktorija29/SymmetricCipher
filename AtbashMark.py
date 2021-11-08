# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

# А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я
# Я Ю Э Ь Ы Ъ Щ Ш Ч Ц Х Ф У Т С Р П О Н М Л К Й И З Ж Ё Е Д Г В Б А

D = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R',
     'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I',
     'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}
d = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r',
     'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
     's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}
D_ru = {'А': 'Я', 'Б': 'Ю', 'В': 'Э', 'Г': 'Ь', 'Д': 'Ы', 'Е': 'Ъ', 'Ё': 'Щ', 'Ж': 'Ш', 'З': 'Ч',
        'И': 'Ц', 'Й': 'Х', 'К': 'Ф', 'Л': 'У', 'М': 'Т', 'Н': 'С', 'О': 'Р', 'П': 'П', 'Р': 'О',
        'С': 'Н', 'Т': 'М', 'У': 'Л', 'Ф': 'К', 'Х': 'Й', 'Ц': 'И', 'Ч': 'З', 'Ш': 'Ж', 'Щ': 'Ё',
        'Ъ': 'Е', 'Ы': 'Д', 'Ь': 'Г', 'Э': 'В', 'Ю': 'Б', 'Я': 'А'}
d_ru = {'а': 'я', 'б': 'ю', 'в': 'э', 'г': 'ь', 'д': 'ы', 'е': 'ъ', 'ё': 'щ', 'ж': 'ш', 'з': 'ч',
        'и': 'ц', 'й': 'х', 'к': 'ф', 'л': 'у', 'м': 'т', 'н': 'с', 'о': 'р', 'п': 'п', 'р': 'о',
        'с': 'н', 'т': 'м', 'у': 'л', 'ф': 'к', 'х': 'й', 'ц': 'и', 'ч': 'з', 'ш': 'ж', 'щ': 'ё',
        'ъ': 'е', 'ы': 'д', 'ь': 'г', 'э': 'в', 'ю': 'б', 'я': 'а'}


def encrypt(text):
    new = ""
    for s in text:
        if s.isalpha():
            if s.isupper():
                if 65 <= ord(s) <= 90:
                    new += D[s]
                else:
                    new += D_ru[s]
            else:
                if 97 <= ord(s) <= 122:
                    new += d[s]
                else:
                    new += d_ru[s]
        else:
            new += s
    return new


in_text = input("Введите текст для шифрования Атбаш: \n")
final_text = encrypt(in_text)
print("Зашифрованный: ", final_text, "\nОбратная расшифровка: ", encrypt(final_text))

# ----------------------------------------------------------------------------

# Таблица шифрования:
#     1 2 3 4 5 6 7 8 9 0
#     с е н о в а л
#     -------------------
# 8 | б г д ё ж з и й к м
# 9 | п р т у ф х ц ч ш щ
# 0 | ъ ы ь э ю я ∙ /

d_mark = {'а': '6', 'б': '81', 'в': '5', 'г': '82', 'д': '83', 'е': '2', 'ё': '84',
          'ж': '85', 'з': '86', 'и': '87', 'й': '88', 'к': '89', 'л': '7', 'м': '80',
          'н': '3', 'о': '4', 'п': '91', 'р': '92', 'с': '1', 'т': '93', 'у': '94',
          'ф': '95', 'х': '96', 'ц': '97', 'ч': '98', 'ш': '99', 'щ': '90', 'ъ': '01',
          'ы': '02', 'ь': '03', 'э': '04', 'ю': '05', 'я': '06', '.': '07', '/': '08'}


def mark_encrypt(text):
    new = ""
    # удаляем пробелы и знаки препинания, кроме точки
    import re
    text = re.sub("[ ]+", "/", text)
    text = re.sub("[^\w./]", "", text)
    for s in text:
        if s.isalpha() or s == '.' or s == '/':
            try:
                new += d_mark[s]
            except:
                print("Некорректная исходная строка")
                return
        else:
            new += s
    # разбиваем результат на блоки по 5 символов
    i = 0
    res = ''
    while i < len(new):
        res += new[i:i + 5] + ' '
        i += 5
    res += new[i:]
    return res


def get_key(value):
    for k in list(d_mark.keys()):
        if d_mark[k] == value:
            return k
    return None


def decryption(res_text):
    res_text = res_text.replace(' ', '')
    source_text = ''
    temp_s = ''
    for s in res_text:
        if temp_s == '':
            f = get_key(s)
            if f:
                source_text += get_key(s)
            else:
                temp_s += s
        else:
            temp_s += s
            if get_key(temp_s):
                source_text += get_key(temp_s)
            temp_s = ''
    source_text = source_text.replace('/', ' ')
    return source_text


in_text_mark = input("\nВведите строку для шифрования шифром Марк (маленькими русскими буквами)\n")
print("\nЗашифрованный: ")
res_mark_text = mark_encrypt(in_text_mark)
if res_mark_text:
    print(res_mark_text)
print("\n****** Внимание! ****** \nПри использовании в строке чисел - результат расшифровки не верен")
print("***********************")
print("\nРасшифровка: ")
if res_mark_text:
    print(decryption(res_mark_text))
else:
    print("Некорректная исходная строка")