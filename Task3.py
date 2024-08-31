import string

def task3(message_filename, dictionary_filename, threshold):
    with open(message_filename, 'r') as m:
        message = remove_punctuation(m.read()).split() # remove punctuation, and split along white space
    with open(dictionary_filename, 'r') as d:
        dictionary = {word.strip().lower() for word in d} # create a dictionary by stripping words and putting into lowercase
    
    count_correct = 0
    for word in message:
      if word in dictionary or word.lower() in dictionary: # count number of words in the dictionary
        count_correct += 1
    if len(message) > 0:
        t_percentage = (count_correct / len(message)) * 100
    else:
        t_percentage = 0
    result = t_percentage >= threshold
    return f"{result}\n{t_percentage:.2f}"


def remove_punctuation(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text
if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task3 function
    print(task3('jingle_bells.txt', 'dict_xmas.txt', 90))
    print(task3('fruit_ode.txt', 'dict_fruit.txt', 80))
    print(task3('amazing_poetry.txt', 'common_words.txt', 95))
    