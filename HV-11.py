"""
Hometask 11. generators

Task description:
write generator function that has as input some range value and chunk_size
 produces output as lists with len == chunk size
 Example:
 Call:  chunk_generator(range(11), chunk_size=3) ->
 Output:  [0, 1, 2]
          [3, 4, 5]
          [6, 7, 8]
          [9, 10]
"""


def chunk_generator(input_range, chunk_size):
    input_range = list(input_range)
    for i in range(0, len(input_range), chunk_size):
        yield input_range[i:i + chunk_size]


input_range = range(11)
chunk_size = 3

for chunk in chunk_generator(input_range, chunk_size):
    print(chunk)
