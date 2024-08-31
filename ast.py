from collections import deque
import string
import math

class AST:
    def __init__(self, message, dictionary, ops, threshold):
        self.message = message
        self.expanded = []
        self.fringe = deque()
        self.fringe.append((message, [], 0, self.task5(message, False)))
        self.ops = ops
        self.dictionary = dictionary
        self.threshold = threshold
        self.max_fringe = len(self.fringe)
        self.max_depth = 0
        self.solution = ""
        self.solution_key = ""
        self.path_cost = 0
    
    # Uniform Cost Search
    def search(self):
        self.check_fringe()
        message = self.fringe.popleft()
        self.expanded.append(message) # add the message to expanded
        self.update_max_depth(message[2])
        if len(self.expanded) == 1000: # if 1000 nodes looked at
            curr_node = message
            node_neighbors = self.find_neighbors(curr_node[0], curr_node[1], curr_node[2])
            for n in node_neighbors:
                self.fringe.append(n)
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
            for n in node_neighbors:
                self.fringe.append(n)
            self.sort_fringe()
            return self.search()

    def find_neighbors(self, message, keys, depth):
        neighbors = []
        for k in self.ops: # loop through all operators
            keys_curr = keys.copy()
            dec = self.task1(k, message)
            keys_curr.append(k)
            if self.check_percentage(dec) >= self.threshold:
                goal = True
            else:
                goal = False
            neighbors.append((dec, keys_curr, depth + 1, self.task5(dec, goal)))
        return neighbors
    
    def sort_fringe(self):
        self.fringe = deque(sorted(self.fringe, key=lambda x: x[2] + x[3]))
        return
    
    def task5(self, message, is_goal):
        if is_goal:
            return 0
        else:
            letter_count = {}
            comp = "ETAONS"
            for letters in comp:
                letter_count[letters] = 0
            for letter in message:
                if letter.upper() in comp:
                    letter_count[letter.upper()] = letter_count.get(letter.upper(), 0) + 1
            sorted_letters = sorted(letter_count, key=lambda x: (-letter_count[x], x))
            count = 0
            for i in range(len(sorted_letters)):
                if sorted_letters[i] != comp[i]:
                    count += 1
            hur = count/2
            score = math.ceil(hur)
            return score
    
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
        message_list = list(message)  # Convert the string to a list to make it mutable
        for i in range(len(message_list)):
            if message_list[i] == letter1:
                message_list[i] = letter2
            elif message_list[i] == letter1low:
                message_list[i] = letter2low
            elif message_list[i] == letter2:
                message_list[i] = letter1
            elif message_list[i] == letter2low:
                message_list[i] = letter1low
        return ''.join(message_list)  # Convert the list back to a string

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