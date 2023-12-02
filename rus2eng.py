import sys

eng_qwerty = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
eng_qwerty += eng_qwerty.upper()
ru_qwerty = "йцукенгшщзхъфывапролджэячсмитьбю."
ru_qwerty += ru_qwerty.upper()

rus2eng = {k: v for k, v in zip(ru_qwerty, eng_qwerty)}

lines = []
for line in sys.stdin:
    for c in line:
        append_char = c
        if c in rus2eng:
            append_char = rus2eng[c]
        lines.append(append_char)
print("".join(lines))
