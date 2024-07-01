# node.py

class Node:
    def __init__(self, b_code=0, pg=0, para=0, s_no=0, off=0):
        self.left = None
        self.right = None
        self.book_code = b_code
        self.page = pg
        self.paragraph = para
        self.sentence_no = s_no
        self.offset = off