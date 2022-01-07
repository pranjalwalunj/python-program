class Books(object):
    def __init__(self, author, genre, name_of_book):
        self.author = author
        self.genre = genre
        self.name_of_book = name_of_book

    def book_name(self, name_of_book):
        return f'{name_of_book}'

    def what_i_do(self):
        sentence = 'i love reading'
        return sentence

    def more_info(self):
        return f'I like {self.author}, I read {self.genre} types of books, I have read {self.name_of_book}'

me = Books('Jane Austen', 'Fiction', 'Pride and Prejudice')
print(me.more_info())
