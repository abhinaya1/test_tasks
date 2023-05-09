def convert_to_word(number):
    word_mapping = {
        10: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred'
    }

    if number in word_mapping:
        return word_mapping[number]
    elif number < 10 or number > 90 or number % 10 == 0:
        return ''

    tens = number // 10 * 10
    units = number % 10

    return f"{word_mapping[tens]}-{convert_to_word(units)}"

for num in range(101):
    if num % 10 == 0:
        print(convert_to_word(num))
    else:
        print(num)
