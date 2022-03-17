
def encrypt(plainText,shift):
	result = ""
	# traverse text
	for i in range(len(plainText)):
		char = plainText[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + shift - 65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + shift - 97) % 26 + 97)

	return result

def decrypt(cipher):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for key in range(len(letters)):
       translated = ''
       for symbol in cipher:
          if symbol in letters:
             num = letters.find(symbol)
             num = num - key
             if num < 0:
                num = num + len(letters)
             translated = translated + letters[num]
          else:
             translated = translated + symbol
          if translated == plainText:
              print('Hacking key #%s: %s (Done)' % (key, translated))
              return
        
       print('Hacking key #%s: %s' % (key, translated))

plainText=input("Please Enter The PlainText : ")
shift=int(input("Please Enter The Number of Shifts : "))
#plainText = "ATTACKATONCE"
#shift = 4
#cipher = 'EXXEGOEXSRGI'
print ("Text : " + plainText)
print ("Shift : " + str(shift))
print ("Cipher: " + encrypt(plainText,shift))


cipher=input("Please Enter The Cipher : ")
decrypt(cipher)