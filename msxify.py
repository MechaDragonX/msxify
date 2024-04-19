import sys

diacritics = {
    'が':  'か\\r゛',
    'ぎ':  'き\\r゛',
    'ぐ':  'く\\r゛',
    'げ':  'け\\r゛',
    'ご':  'こ\\r゛',
    'ざ':  'さ\\r゛',
    'じ':  'し\\r゛',
    'ず':  'す\\r゛',
    'ぜ':  'せ\\r゛',
    'ぞ':  'そ\\r゛',
    'だ':  'た\\r゛',
    'ぢ':  'ち\\r゛',
    'づ':  'つ\\r゛',
    'で':  'て\\r゛',
    'ど':  'と\\r゛',
    'ば':  'は\\r゛',
    'び':  'ひ\\r゛',
    'ぶ':  'ふ\\r゛',
    'べ':  'へ\\r゛',
    'ぼ':  'ほ\\r゜',
    'ぱ':  'は\\r゜',
    'ぴ':  'ひ\\r゜',
    'ぷ':  'ふ\\r゜',
    'ぺ':  'へ\\r゜',
    'ぽ':  'ほ\\r゜',
}

input = sys.argv[1]
output = ''

i = 0
while i < len(input):
    if input[i] in diacritics.keys():
        output += diacritics[input[i]]
    else:
        output += input[i]
    if i != len(input) - 1:
        output += '\\r'
    i += 1

print(output)
