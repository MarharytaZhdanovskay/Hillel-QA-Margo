"""
Hometask 09. read_write_files

Task description:
write script that will read "input.txt" file
and find there all characters from english alphabet
collect these characters and their positions in file
after info collected this info as text write to "output.txt" file
in such format
 ####################
 <first found letter> -> pos1
 <next_letter> -> pos2
 <next_letter -> pos3
 etc

"""


def find_alphabet_chars(i_file, o_file):
    with open(i_file, 'r') as file:
        content = file.read()

    alphabet_chars = []
    for pos, char in enumerate(content):
        if char.isalpha() and char.isascii():
            alphabet_chars.append((char, pos + 1))

    with open(o_file, 'w') as out_file:
        out_file.write("####################\n")
        for char, pos in alphabet_chars:
            out_file.write(f"{char} -> pos{pos}\n")


i_file = "../input.txt"
o_file = "../output.txt"
find_alphabet_chars(i_file, o_file)
