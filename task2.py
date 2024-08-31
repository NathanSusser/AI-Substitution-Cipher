def task2(filename, letters):
    with open(filename, 'r') as f:
        content = f.read()
    key = list(set(letters)) # get a list of unique letters
    key.sort() # sort the letters
    lst = []
    keys = succession(key, 0, lst, content) # recursive function to create operators (pairs of the letters)
    message = list(content)
    decoded = ""
    counter = 0
    for k in keys: # loop through all operators
      counter += 1
      dec = task1(k, message.copy()) # decode
      if counter == len(keys): # weird shit for the output
        decoded += "\n" + dec
      else:
        decoded += "\n" + dec + "\n" 
    return str(len(keys)) + decoded

def succession(key, index, lst, content): # recursive function to create operators, loops through each letter in key and performs suc_helper
    if index == len(key):
        return lst
    else:
        return suc_helper(key, index, lst, content)

def suc_helper(key, index, lst, content):
    lst_help = lst.copy() # don't alter original list
    for j in range(index + 1, len(key)): # loop through rest of letters
        # make sure that first letter in alphabet is first and that at least on letter in the message
        if key[index] < key[j] and ((key[index] in content or key[index].lower() in content) or (key[j] in content or key[j].lower() in content)):
            lst_help.append([key[index], key[j]])
    return succession(key, index + 1, lst_help, content)
      

def task1(key, message):
    lst_key = list(key)
    decrypt_lst = decode(lst_key, message)
    report = ''.join(decrypt_lst)
    return report

def decode(key, message):
   for i in range(len(key)-1, -1, -1):
      if i % 2 == 1:
        message = letter_switch(key[i], key[i-1], message)
   return message

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
    # Example function calls below, you can add your own to test the task2 function
    print(task2('spain.txt', 'ABE'))
    print(task2('ai.txt', 'XZ'))
    print(task2('cabs.txt', 'ABZD'))