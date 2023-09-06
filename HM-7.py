"""
Hometask 07. integer_to_english_words

Task description:
Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Qutput: "One Hundred Twenty Three"

let's take that number always > 100 and only three digits
100 <= num <= 999

"""


def numberToWords(num):
    ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
            'Nine', 'Ten',
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
            'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
            'Seventy', 'Eighty', 'Ninety']
    hundred = 'Hundred'

    hundreds_number = num // 100
    tens_number = (num % 100) // 10
    ones_number = (num % 100) % 10

    result = ''
    if hundreds_number > 0:
        result += ones[hundreds_number] + ' ' + hundred + ' '
    if tens_number >= 2:
        result += tens[tens_number] + ' '
        if ones_number > 0:
            result += ones[ones_number] + ' '
    elif tens_number == 1:
        result += ones[10 + ones_number] + ' '
    else:
        if ones_number > 0:
            result += ones[ones_number] + ' '

    return result.strip()


num = 745
words = numberToWords(num)
print(f"Input: {num}")
print(f"Output: \"{words}\"")
