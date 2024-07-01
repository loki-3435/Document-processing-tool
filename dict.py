# dict.py

def to_lower_case(input_list):
    return [s.lower() for s in input_list]

def convert_to_lower(s):
    return s.lower()

def split_sentence(sentence):
    delimiters = ' .,:-!"\'()[]?—'';"@˙""'
    words = []
    word = ''
    for c in sentence:
        if c in delimiters:
            if word:
                words.append(word)
                word = ''
        else:
            word += c
    if word:
        words.append(word)
    return words

def hashi(id):
    return sum((ord(id[i]) * (i + 1) * (i + 2)) for i in range(len(id))) % 100000

def does_exist(id, table):
    x = hashi(id)
    return any(word.id == id for word in table[x])

class Word:
    def __init__(self, id="", count=0):
        self.id = id
        self.count = count

class Dict:
    def __init__(self):
        self.dct = [[] for _ in range(100003)]

    def insert_sentence(self, book_code, page, paragraph, sentence_no, sentence):
        l = to_lower_case(split_sentence(sentence))
        for word in l:
            x = hashi(word)
            word_exists = False
            for w in self.dct[x]:
                if w.id == word:
                    w.count += 1
                    word_exists = True
                    break
            if not word_exists:
                self.dct[x].append(Word(word, 1))

    def get_word_count(self, word):
        word = convert_to_lower(word)
        x = hashi(word)
        for w in self.dct[x]:
            if w.id == word:
                return w.count
        return 0

    def dump_dictionary(self, filename):
        with open(filename, 'w') as file:
            for bucket in self.dct:
                for word in bucket:
                    file.write(f"{word.id.lower()}, {word.count}\n")

if __name__ == "__main__":
    dict_obj = Dict()
    dict_obj.insert_sentence(1, 1, 1, 1, "VOL.1: 1884 30 NOVEMBER, 1896 1")
    
    count = dict_obj.get_word_count("test")
    if count != -1:
        print(f"Word 'test' count: {count}")
    else:
        print("Word not found in the dictionary.")

    dict_obj.dump_dictionary("output.txt")
    print("hi")