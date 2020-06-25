# common words

books = ["plain_text_files/Highland_Legends.txt", "plain_text_files/Robin_Hood.txt",
         "plain_text_files/The Machinery of the Universe.txt"]

for book in books:
    with open(book) as file:
        content = file.read()
        spl = content.split()
        spl.count('the')

# .split().lower().count(the)
