def number_to_text(number):
    # collection of nums and corresponding text to replace it with 
    num_to_text = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
        '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
        '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
        '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty',
        '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy',
        '80': 'eighty', '90': 'ninety'
    }

    # if one of the nums in collection, replace 
    if str(number) in num_to_text:
        return num_to_text[str(number)]
    # if not its a combo, split into tens and ones to replace
    else:
        tens = str(number // 10 * 10)
        ones = str(number % 10)
        return num_to_text[tens] + ' ' + num_to_text[ones]

# gets user input and splits it into words
input_string = input("Enter a string: ")
words = input_string.split()

# checks each word to check if its a num to replace
for i in range(len(words)):
    word = words[i]
    if word.isdigit():
        words[i] = number_to_text(int(word))

# re-concatenate with the replaced word
output_string = ' '.join(words)
print("Output:")
print(output_string)
