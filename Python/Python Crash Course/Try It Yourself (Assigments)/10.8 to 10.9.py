# 10.8 to 10.9

files = ["cats.txt", 'dogs.txt']
# the file path is OK if the print is inside the try/except block

for file in files:
    print("\nReading file " + file + ':')
    # the for loop is necessary to work with each value inside the list
    try:
        with open(file) as f_obj:
            contents = f_obj.read()
            print(contents)
    except FileNotFoundError:
        pass
    # the pass statement tells python to do nothing but keep going
