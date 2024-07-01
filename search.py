# search.py

from Node import Node

class Sent:
    def __init__(self, book_code, page, paragraph, sentence_no, sentence):
        self.book_code = book_code
        self.page = page
        self.paragraph = paragraph
        self.sentence_no = sentence_no
        self.sentence = sentence

class SearchEngine:
    def __init__(self):
        self.l = []

    def insert_sentence(self, book_code, page, paragraph, sentence_no, sentence):
        sentence = sentence.lower()
        s = Sent(book_code, page, paragraph, sentence_no, sentence)
        self.l.append(s)

    def fill(self, str_):
        n = len(str_)
        lps = [0]
        len_ = 0
        i = 1
        while i < n:
            if str_[i] == str_[len_]:
                len_ += 1
                lps.append(len_)
                i += 1
            else:
                if len_ == 0:
                    lps.append(0)
                    i += 1
                else:
                    len_ = lps[len_ - 1]
        return lps

    def kmp(self, s, pat, temp, count):
        str_ = s.sentence
        n = len(str_)
        m = len(pat)
        lps = self.fill(pat)
        i = 0
        j = 0
        while i < n:
            if str_[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    temp.book_code = s.book_code
                    temp.page = s.page
                    temp.paragraph = s.paragraph
                    temp.sentence_no = s.sentence_no
                    temp.offset = i - j
                    temp.right = Node()
                    temp.right.left = temp
                    temp = temp.right
                    temp.right = None
                    j = lps[j - 1]
                    count[0] += 1
            elif i < n and str_[i] != pat[j]:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

    def search(self, pattern):
        pattern = pattern.lower()
        head = Node()
        temp = head
        temp.left = None
        temp.right = None
        n_matches = [0]
        for s in self.l:
            self.kmp(s, pattern, temp, n_matches)
        if temp.left is not None:
            temp.left.right = None
            del temp
        else:
            return None, 0
        return head, n_matches[0]

if __name__ == "__main__":
    search_engine = SearchEngine()
    search_engine.insert_sentence(1, 1, 1, 1, "This is an example sentence.")

    results, n_matches = search_engine.search("s")

    if n_matches > 0:
        print(f"Number of matches found: {n_matches}")
        print("Matching results:")

        temp = results
        while temp is not None:
            print(f"Book Code: {temp.book_code}, Page: {temp.page}, "
                  f"Paragraph: {temp.paragraph}, Sentence No: {temp.sentence_no}, "
                  f"Offset: {temp.offset}")
            temp = temp.right
    else:
        print("No matches found.")