def encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
        if i == len(decoded_string)-1:
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in encoded_string:
        if i.isdigit():
            char_amount += i
        else:
            decoded_string += str(i * int(char_amount))
            char_amount = ''
    return decoded_string


with open('decode.txt', 'w') as data:
    data.write('sssssssssssssssssqqqqqqqqqqqqqqqqqDDDDDDDDDDDDDDDDDDDD')

with open('decode.txt', 'r') as data:
    string = data.readline()

with open('decode.txt', 'r') as file:
    decoded_string = file.read()

with open('encode.txt', 'w') as file:
    file.write(encode(decoded_string))

with open('encode.txt', 'r') as file:
    encoded_string = file.read()

with open('decode2.txt', 'w') as data:
    data.write(decode(encoded_string))


