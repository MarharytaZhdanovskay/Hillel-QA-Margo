# Підраховує кількість голосних літер у тексті


def count_vowels(text):
    vowels = 'AEIOUaeiou'
    vowel_counts = {vowel: 0 for vowel in vowels}
    for char in text:
        if char in vowels:
            vowel_counts[char] += 1

    return vowel_counts

# При запуску цього коду з використанням наданого тексту,
# він виведе кількість голосних літер у форматі таблиці,
# з окремими підрахунками для голосних літер у нижньому і верхньому регістрах.


def print_vowel_counts(vowel_counts):
    print("-" * 25)
    print(f"| {'vowel':^10} | {'count':^8} |")
    print("-" * 25)
    for vowel, count in vowel_counts.items():
        print(f"| {vowel:^10}| {count:^10.0f}|")
    print("-" * 25)


poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

vowel_counts = count_vowels(poem_text)
print_vowel_counts(vowel_counts)

print(' ' * 20)


def modify_text(text):
    vowels = {
        'A': 'À', 'a': 'à',
        'E': 'É', 'e': 'é',
        'I': 'Í', 'i': 'í',
        'O': 'Ó', 'o': 'ó',
        'U': 'Ú', 'u': 'ú'
    }

    modified_text = ""
    for char in text:
        if char in vowels:
            modified_text += vowels[char]
        else:
            modified_text += char

    return modified_text


modified_poem_text = modify_text(poem_text)
print(modified_poem_text)
