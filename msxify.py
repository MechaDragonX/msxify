import sys

diacritics = {
    'ガ':  'カ\\r゛',
    'ギ':  'キ\\r゛',
    'グ':  'ク\\r゛',
    'ゲ':  'ケ\\r゛',
    'ゴ':  'コ\\r゛',
    'ザ':  'サ\\r゛',
    'ジ':  'シ\\r゛',
    'ズ':  'ス\\r゛',
    'ゼ':  'セ\\r゛',
    'ゾ':  'ソ\\r゛',
    'ダ':  'タ\\r゛',
    'ヂ':  'チ\\r゛',
    'ヅ':  'ツ\\r゛',
    'デ':  'テ\\r゛',
    'ド':  'ト\\r゛',
    'バ':  'ハ\\r゛',
    'ビ':  'ヒ\\r゛',
    'ブ':  'フ\\r゛',
    'ベ':  'ヘ\\r゛',
    'ボ':  'ホ\\r゜',
    'パ':  'ハ\\r゜',
    'ピ':  'ヒ\\r゜',
    'プ':  'フ\\r゜',
    'ペ':  'ヘ\\r゜',
    'ポ':  'ホ\\r゜',
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
