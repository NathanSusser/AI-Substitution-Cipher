import sys
sys.setrecursionlimit(1500)

from collections import deque
import string
from bfs import BFS
from dfs import DFS
from ids import IDS


def task4(algorithm, message_filename, dictionary_filename, threshold, letters, debug):
    with open(message_filename, 'r') as f:
        content = f.read()
    with open(dictionary_filename, 'r') as d:
        dictionary = {word.strip().lower() for word in d} # create a dictionary by stripping words and putting into lowercase
    ops = get_operators(letters, content) # get the possible actions
    final_string = ""
    if algorithm == "b":
       bfs = BFS(content, dictionary, ops, threshold)
       bfs.search()
       expanded = bfs.get_expanded()
       solution = bfs.get_solution()
       key = bfs.get_solution_key()
       path_cost = bfs.get_solution_pc()
       num_nodes_expanded = len(expanded)
       max_fringe_size = bfs.get_max_fringe()
       max_depth = bfs.get_max_depth()
       first_few = ""
       if len(expanded) > 10:
           for i in range(10):
                if i == 9:
                    first_few += "\n" + expanded[i][0]
                else:
                    first_few += "\n" + expanded[i][0] + "\n"
       else:
            for i in range(len(expanded)):
                if i == len(expanded)-1:
                    first_few += "\n" + expanded[i][0]
                else:
                    first_few += "\n" + expanded[i][0] + "\n"
       if solution == "No solution found.":
            final_string = f"{solution}\n\nNum nodes expanded: {num_nodes_expanded}\nMax fringe size: {max_fringe_size}\nMax depth: {max_depth}\n\nFirst few expanded states:{first_few}"
       else:
            final_string = f"Solution: {solution}\n\nKey: {key}\nPath Cost: {path_cost}\n\nNum nodes expanded: {num_nodes_expanded}\nMax fringe size: {max_fringe_size}\nMax depth: {max_depth}\n\nFirst few expanded states:{first_few}"
    if algorithm == "d":
       dfs = DFS(content, dictionary, ops, threshold)
       dfs.search()
       expanded = dfs.get_expanded()
       solution = dfs.get_solution()
       key = dfs.get_solution_key()
       path_cost = dfs.get_solution_pc()
       num_nodes_expanded = len(expanded)
       max_fringe_size = dfs.get_max_fringe()
       max_depth = dfs.get_max_depth()
       first_few = ""
       if len(expanded) > 10:
           for i in range(10):
                if i == 9:
                    first_few += "\n" + expanded[i][0]
                else:
                    first_few += "\n" + expanded[i][0] + "\n"
       else:
            for i in range(len(expanded)):
                if i == len(expanded)-1:
                    first_few += "\n" + expanded[i][0]
                else:
                    first_few += "\n" + expanded[i][0] + "\n"
       if debug == "y":
            if solution == "No solution found.":
                    final_string = f"{solution}\n\nNum nodes expanded: {num_nodes_expanded}\nMax fringe size: {max_fringe_size}\nMax depth: {max_depth}\n\nFirst few expanded states:{first_few}"
            else:
                    final_string = f"Solution: {solution}\n\nKey: {key}\nPath Cost: {path_cost}\n\nNum nodes expanded: {num_nodes_expanded}\nMax fringe size: {max_fringe_size}\nMax depth: {max_depth}\n\nFirst few expanded states:{first_few}"
        else:
           if solution == "No solution found.":
                    final_string = f"{solution}\n\nNum nodes expanded: {num_nodes_expanded}\nMax fringe size: {max_fringe_size}\nMax depth: {max_depth}"
            else:
                    final_string = f"Solution: {solution}\n\nKey: {key}\nPath Cost: {path_cost}\n\nNum nodes expanded: {num_nodes_expanded}\nMax fringe size: {max_fringe_size}\nMax depth: {max_depth}"
    if algorithm == "i":
       ids = IDS(content, dictionary, ops, threshold)
       ids.search()
       expanded = ids.get_expanded()
       solution = ids.get_solution()
       key = ids.get_solution_key()
       path_cost = ids.get_solution_pc()
       num_nodes_expanded = len(expanded)
       max_fringe_size = ids.get_max_fringe()
       max_depth = ids.get_max_depth()
       first_few = ""
       if len(expanded) > 10:
           for i in range(10):
                if i == 9:
                    first_few += "\n" + expanded[i][0]
                else:
                    first_few += "\n" + expanded[i][0] + "\n"
       else:
            for i in range(len(expanded)):
                if i == len(expanded)-1:
                    first_few += "\n" + expanded[i][0]
                else:
                    first_few += "\n" + expanded[i][0] + "\n"
       if solution == "No solution found.":
            final_string = f"{solution}\n\nNum nodes expanded: {num_nodes_expanded}\nMax fringe size: {max_fringe_size}\nMax depth: {max_depth}\n\nFirst few expanded states:{first_few}"
       else:
            final_string = f"Solution: {solution}\n\nKey: {key}\nPath Cost: {path_cost}\n\nNum nodes expanded: {num_nodes_expanded}\nMax fringe size: {max_fringe_size}\nMax depth: {max_depth}\n\nFirst few expanded states:{first_few}"
    return final_string

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




if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task4 function
    print(task4('d', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('b', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('i', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))