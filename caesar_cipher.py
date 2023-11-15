Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encryption(text, o):
  rotation = ""
  # tell about the number of letter in text
  for letter_number in text:
    if (Alphabet.find(letter_number) == -1):
      rotation += letter_number
      # difirent situation with the number of letter in text
    else:
      rotation += (Alphabet[(Alphabet.find(letter_number) + o) % len(Alphabet)])
  return rotation

def decryption(text, o):
  rotation = ""
  for letter_number in text:
    if (Alphabet.find(letter_number) == -1):
      rotation += letter_number
    else:
      rotation += (Alphabet[(Alphabet.find(letter_number) - o) % len(Alphabet)])
  return rotation

word = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(word))

if mode == 1:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encryption(text, rotation))
elif mode == 2:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decryption(text, rotation))
elif mode == 3:
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
