from collections import deque
import string

class IDS:
    def __init__(self, message, dictionary, ops, threshold):
        self.message = message
        self.expanded = []
        self.fringe = deque()
        self.fringe.append((message, [], 0))
        self.ops = ops
        self.dictionary = dictionary
        self.threshold = threshold
        self.max_fringe = len(self.fringe)
        self.max_depth = 0
        self.solution = ""
        self.solution_key = ""
        self.path_cost = 0
    
    # Iteratative Depht First Search
    def search(self):
        mc = self.message
        for i in range(1000):
            self.fringe = deque()
            self.fringe.append((mc, [], 0))
            self.search_dfs(i)
            if self.solution != "":
                return

    def search_dfs(self, depth):
        self.check_fringe()
        if len(self.fringe) == 0:
            return
        message = self.fringe.popleft()
        self.expanded.append(message) # add the message to expanded
        self.update_max_depth(message[2])
        if len(self.expanded) == 1000: # if 1000 nodes looked at
            curr_node = message
            node_neighbors = self.find_neighbors(curr_node[0], curr_node[1], curr_node[2])
            for n in reversed(node_neighbors):
                if n[2] <= depth:
                    self.fringe.appendleft(n)
            self.check_fringe()
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
                if n[2] <= depth:
                    self.fringe.appendleft(n)
            return self.search_dfs(depth)

    def find_neighbors(self, message, keys, depth):
        neighbors = []
        for k in self.ops: # loop through all operators
            keys_curr = keys.copy()
            dec = self.task1(k, message)
            keys_curr.append(k)
            neighbors.append((dec, keys_curr, depth + 1))
        return neighbors
    
    def task1(self, key, message):
        lst_key = list(key)
        mess_lst = list(message)
        decrypt_lst = self.decode(lst_key, mess_lst)
        report = ''.join(decrypt_lst)
        return report

    def decode(self, key, message):
        for i in range(len(key)-1, -1, -1):
            if i % 2 == 1:
                message = self.letter_switch(key[i], key[i-1], message)
        return message

    def letter_switch(self, letter1, letter2, message):
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

    def check_percentage(self, message):
        message = self.remove_punctuation(message).split() # remove punctuation, and split along white space
        count_correct = 0
        for word in message:
            if word in self.dictionary or word.lower() in self.dictionary: # count number of words in the dictionary
                count_correct += 1
        if len(message) > 0:
            t_percentage = (count_correct / len(message)) * 100
        else:
            t_percentage = 0
        return t_percentage

    def remove_punctuation(self, text):
        for punctuation in string.punctuation:
            text = text.replace(punctuation, '')
        return text
    
    def get_expanded(self):
        return self.expanded.copy()
    
    def check_fringe(self):
        if len(self.fringe) > self.max_fringe:
            self.max_fringe = len(self.fringe)

    def get_max_fringe(self):
        mf = self.max_fringe
        return mf
    
    def get_solution(self):
        decrypted = self.solution
        return decrypted
    
    def get_solution_key(self):
        decryption_key = self.solution_key
        return decryption_key
    
    def get_solution_pc(self):
        decryption_pc = self.path_cost
        return decryption_pc
    
    def update_max_depth(self, depth):
        if depth > self.max_depth:
            self.max_depth = depth

    def get_max_depth(self):
        md = self.max_depth
        return md