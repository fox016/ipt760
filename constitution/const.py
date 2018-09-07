import random

# Return contents of file as single string
def read_file(filename):
    contents = ""
    with open(filename, 'r') as text:
        contents += text.read()
    return contents

# Return text of single amendment
def get_amendment(text, num):
    if num < 1 or num > 27:
        raise ValueError("num must be 1-27")
    name = "Amendment " + str(num)
    next_name = "Amendment " + str(num+1)
    return text[text.find(name)+len(name):text.find(next_name)].replace("\n", " ").strip()

# Return dictionary of words to list of next words
def get_next_word_map(text):
    next_word_map = {}
    words = text.split()
    for i in range(len(words)-1):
        word = words[i]
        if word in next_word_map:
            next_word_map[word].append(words[i+1])
        else:
            next_word_map[word] = [words[i+1]]
    return next_word_map

# Return random string created by word map
def generate_random_text(next_word_map, length=100):
    text = ""
    #word = random.choice(next_word_map.keys())
    word = "The"
    word_count = 0
    while word_count < length:
        text += word + " "
        word_count+=1
        if word in next_word_map:
            word = random.choice(next_word_map[word])
        else:
            print("Key not found: " + word)
            word = random.choice(next_word_map.keys())
    return text

# Main script
if __name__ == "__main__":
    const = read_file("us_constitution.txt")
    amendments = map(lambda x: get_amendment(const, x), range(1,28))
    next_word_map = get_next_word_map(" ".join(amendments))
    random_text = generate_random_text(next_word_map, 200)
    print(random_text)
