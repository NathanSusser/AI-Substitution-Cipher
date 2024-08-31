def task1(key, filename, indicator):
    lst_key = list(key)  # make the letters a list
    with open (filename, 'r') as f: # open and read file
      content = f.read()
    message = list(content)
    if indicator == 'e': # either encode or decode
      encrypt_lst = encode(lst_key, message)
      report = ''.join(encrypt_lst) # put back into string
    if indicator == 'd':
       decrypt_lst = decode(lst_key, message)
       report = ''.join(decrypt_lst)
    return report

def encode(key, message):
   for i in range(len(key)): # loop through key
      if i % 2 == 0: # want every two letters starting on even
        message = letter_switch(key[i], key[i+1], message)
   return message

def decode(key, message):
   for i in range(len(key)-1, -1, -1): # loop through key in reverse
      if i % 2 == 1: # every two letters starting on odd(last letter)
        message = letter_switch(key[i], key[i-1], message)
   return message

# loop through message and swap letters
def letter_switch(letter1, letter2, message): 
   letter1low = letter1.lower()
   letter2low = letter2.lower()
   for i in range(len(message)):
      if message[i] == letter1:
        message[i] = letter2
      elif message[i] == letter1low:
        message[i] = letter2low
      elif message[i] == letter2:
        message[i] = letter1
      elif message[i] == letter2low:
        message[i] = letter1low
   return message

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task1 function
    print(task1('AE', 'spain.txt', 'd'))
    print(task1('VFSC', 'ai.txt', 'd'))
    print(task1('ABBC', 'cabs_plain.txt', 'e'))
    