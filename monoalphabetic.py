letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
keys = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
plainText  = str(input("Please Enter The PlainText : ")).upper()

def encrypt():
  cipher = []
  for l in plainText:
      key_number =  letters.index(l)
      
      new_letter = keys[key_number]
      
      cipher.append(new_letter)

  encrypt_text = ''.join(cipher)
  return encrypt_text


print("Cipher: ",encrypt())

def decrypt():
  
  cipher  = str(input("Please Enter The Cipher : ")).upper()
  text = []
  for l in cipher:
      letter_number =  keys.index(l)

      new_letter = letters[letter_number]

      text.append(new_letter)

  orginal_text = ''.join(text)
  return orginal_text

print("Orginal Text: ",decrypt())
