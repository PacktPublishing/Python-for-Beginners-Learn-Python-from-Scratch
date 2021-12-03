"""
basic modes(ways) of opening files:
r - R ead  - default
w - W rite - if the file existed (will be removed), if not will be created
a - A ppend (adding new content at the end)

additional file opening modes:
r+ - allows to read and write

file.write and file.read


w+ - allows to write and read
the difference between r+ and w+ is that it's gonna
remove existing file if there was no file then
it's gonna create a new file

a+ - "endless" mode of appending and reading
ATTENTION! 
write function will ALWAYS append text
even if you change the pointer using "seek"

if file doesn't exist - it creates it


"""


with open("namesurnames.txt", "a+", encoding="UTF-8") as file:
    file.write("Something at the end")
    file.seek(0)
    print(file.readline())
    print(file.tell())
    file.write("aaaaa")
    
