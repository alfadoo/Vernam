import secrets

print("Welcome to the Vernam Encryption panel")

mainMessage = input("Please enter the text you would like to encrypt. ")

locks_list = []
key_list= []

for Word in mainMessage.split():
    for letter in Word:
        letter_bit = format(ord(letter),"08b")
        key_bit = format(secrets.randbelow(256),"08b")

        locks_bit = format(int(letter_bit, 2) ^ int(key_bit, 2), "08b")

        locks_list.append(locks_bit)
        key_list.append(key_bit)

        print(letter, letter_bit, key_bit, "->", locks_bit)


print("Şifreli:", " ".join(locks_list))
print("Anahtar:", " ".join(key_list))



