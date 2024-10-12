#https://www.codingame.com/ide/puzzle/unary

def encode_message(message):
    binary_message = ''
    for char in message:
        # ord(char) gets the ASCII code and we convert it to a 7-bit binary string
        binary_message += format(ord(char), '07b')

    # Now, we'll traverse each bit in the binary message to convert it
    encoded_message = []
    i = 0

    # Traverse the entire binary string
    while i < len(binary_message):
        # Get the current bit (either '0' or '1')
        current_bit = binary_message[i]
        # Count how many consecutive bits are the same
        count = 1
        while i + 1 < len(binary_message) and binary_message[i + 1] == current_bit:
            count += 1
            i += 1

        # If the bit is '1', append "0" followed by that many zeros
        if current_bit == '1':
            encoded_message.append('0 ' + '0' * count)
        # If the bit is '0', append "00" followed by that many zeros
        else:
            encoded_message.append('00 ' + '0' * count)

        # Move to the next bit
        i += 1

    # Return the encoded blocks joined by spaces
    return ' '.join(encoded_message)

# Ask the user for the input message to encode
message = input()

# Encode the message
encoded_message = encode_message(message)

# Output the encoded result
print(encoded_message)
