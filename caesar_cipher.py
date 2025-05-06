from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "encode":
        original_text = list(original_text)
        for number in range(len(original_text)):
            if original_text[number] in alphabet:
                new_index = (alphabet.index(original_text[number]) + shift_amount) % 26
                original_text[number] = alphabet[new_index]
        original_text = ''.join(original_text)
        print(original_text)
    elif encode_or_decode == "decode":
        original_text = list(original_text)
        for number in range(len(original_text)):
            if original_text[number] in alphabet:
                new_index = (alphabet.index(original_text[number]) - shift_amount) % 26
                original_text[number] = alphabet[new_index]
        original_text = ''.join(original_text)
        print(original_text)

working = True

while working:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    answer = input("Do you want to finish the game?(Y/N)\n").lower()
    if answer == 'y':
        working = False
    elif answer == 'n':
        working = True
