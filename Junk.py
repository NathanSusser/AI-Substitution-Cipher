def succession(key, index, lst):
  if len(key) == 0:
    return lst
  if index >= len(key):
    key = key[1:]
  else:
    if key[0] != key[1 + index] and key[0] > key[1 + index]:
      lst.append(key[0], key[1 + index])
      succession(key, index + 1, lst)
    else:
        succession(key, index + 1, lst)





    key = []
    for l in lst_letters:
      if l in content or l.lower() in content:
        key.append(l)





def task2(filename, letters):
    with open(filename, 'r') as f:
        content = f.read()
    key = list(set(letters))
    key.sort()
    lst = []
    keys = succession(key, 0, lst, content)
    print(keys)
    message = list(content)
    
    return ''

def succession(key, index, lst, content):
    if index == len(key):
        return lst
    else:
        return suc_helper(key, index, lst, content)

def suc_helper(key, index, lst, content):
    lst_help = lst.copy()  # Use copy to prevent modifying the original list
    for j in range(index + 1, len(key)):
        if key[index] < key[j] and ((key[index] in content or key[index].lower() in content) and (key[j] in content or key[j].lower() in content)):
            print([key[index], key[j]])
            lst_help.append([key[index], key[j]])
            print(lst_help)
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


def get_max_depth(expanded):
    max_depth = expanded[0][2]
    for node in expanded:
        if node[2] > max_depth:
            max_depth = node[2]
    return max_depth

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task2 function
    print(task2('spain.txt', 'ABE'))
    print(task2('ai.txt', 'XZ'))
    print(task2('cabs.txt', 'ABZD'))















from collections import deque
import string

def task4(algorithm, message_filename, dictionary_filename, threshold, letters, debug):
    with open(message_filename, 'r') as f:
        content = f.read()
    with open(dictionary_filename, 'r') as d:
        dictionary = {word.strip().lower() for word in d} # create a dictionary by stripping words and putting into lowercase
    ops = get_operators(letters, content) # get the possible actions
    expanded = []
    fringe = deque()
    fringe.append((content, [], 0))
    if algorithm == "b":
       bfs(content, dictionary, ops, threshold, expanded, fringe)
    return ''
#breadth first search    
def bfs(message, dictionary, ops, threshold, expanded, fringe):
    expanded.append(message) # add the message to expanded
    if len(expanded) == 1000: # if 1000 nodes looked at
       return 
    else:
        curr_node = message
        if check_percentage(curr_node, dictionary) >= threshold: # check against threshold
          return 
        node_neighbors = find_neighbors_bfs(ops, curr_node)
        for n in node_neighbors:
          fringe.append(n)
        return bfs(fringe.popleft(), dictionary, ops, threshold, expanded, fringe)

def find_neighbors_bfs(ops, message, keys, depth):
    neighbors = []
    for k in ops: # loop through all operators
      dec = task1(k, message)
      neighbors.append(dec)
    return neighbors

def ids(message, dictionary, ops, threshold, expanded, fringe):
    expanded.append(message)
    if len(expanded) == 1000:
       return 
    else:
        curr_node = message
        if check_percentage(curr_node, dictionary) >= threshold:
          return 
        node_neighbors = find_neighbors_bfs(ops, curr_node)
        for n in node_neighbors:
          fringe.append(n)
        return bfs(fringe.popleft(), dictionary, ops, threshold, expanded, fringe)

def find_neighbors_ids(ops, message):
    neighbors = []
    for k in ops: # loop through all operators
      dec = task1(k, message)
      neighbors.append(dec)
    return neighbors  

def get_operators(letters, message):
    key = list(set(letters)) # get a list of unique letters
    key.sort() # sort the letters
    lst = []
    keys = succession(key, 0, lst, message) # recursive function to create operators (pairs of the letters)
    return keys

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
    mess_lst = list(message)
    decrypt_lst = decode(lst_key, mess_lst)
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

def check_percentage(message, dictionary):
    message = remove_punctuation(message).split() # remove punctuation, and split along white space
    count_correct = 0
    for word in message:
      if word in dictionary or word.lower() in dictionary: # count number of words in the dictionary
        count_correct += 1
    if len(message) > 0:
        t_percentage = (count_correct / len(message)) * 100
    else:
        t_percentage = 0
    return t_percentage


def remove_punctuation(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task4 function
    print(task4('d', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('b', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('i', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))






    # Breadth First Search
    def search(self):
        self.check_fringe()
        message = self.fringe.popleft()
        self.expanded.append(message) # add the message to expanded
        self.update_max_depth(message[2])
        print(self.max_depth)
        print(len(self.expanded))
        if len(self.expanded) == 1000: # if 1000 nodes looked at
            self.solution = "No solution found."
            return 
        else:
            curr_node = message
            if self.check_percentage(curr_node[0]) >= self.threshold: # check against threshold
                self.solution = curr_node[0]
                self.solution_key = ''.join(''.join(inner) for inner in curr_node[1])
                self.path_cost = curr_node[2]
                return 
            node_neighbors = self.find_neighbors(curr_node[0], curr_node[1], curr_node[2])
            for n in reversed(node_neighbors):
                self.fringe.appendleft(n)
            return self.search()