def caesar_cipher(text, shift):
  result = ""
  for char in text:
    if char.isupper():
      result += chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
      result += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      result += char
  return result

print("THANK YOU FOR USING SNBHOWMIK'S ENCRYPTION AND DECRYPTION TOOL")
option=int(input("Press 1 for Encryption and 2 for Decryption:"))
if option==1:
  text= input("Input message you want to encrypt:")
  shift = int(input("Enter the shift value:"))
  encrypted_text = caesar_cipher(text, shift)
  print("The encrypted text is:",encrypted_text)

elif option==2:
  text= input("Input message you want to decrypt:")
  shift = int(input("Enter the shift value:"))
  decrypted_text = caesar_cipher(text, -shift)
  print("The decrypted text is:",decrypted_text)

else:
  exit