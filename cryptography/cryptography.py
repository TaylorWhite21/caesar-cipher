def encrypt(plain, key):
  
  encrypted_text = ''
  # Traverses the text
  for i in range(len(plain)):
    char = plain[i]
    
    if not char.isalnum():
      encrypted_text += char
      continue
      
    if char == ' ':
      encrypted_text += ' '
      
    # Checks if letter is upper case and adds it to the returning string
    elif (char.isupper()):
      encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
      
    # Checks if letter is lower case and adds it to the returning string
    else:
      encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
      
  return encrypted_text
  
def decrypt(encrypted, key):
  return encrypt(encrypted, -key)
  
def crack(to_crack):
  letter_list = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  encrypted_upper = to_crack.upper()
  letter_frequency = {}
  
  for letter in letter_list:
    letter_frequency[letter] = 0
  
  for letter in encrypted_upper:
    if letter in letter_list:
      letter_frequency[letter] += 1
      
  key = sorted(letter_frequency.values())[-2]
  
  cracked = decrypt(to_crack, key)
  
  return cracked
  
