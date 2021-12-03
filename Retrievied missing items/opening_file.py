
def read_content_of_file(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
         print("File not found, give a proper path")

nameOfFile = input("Give me the name of file: ")

fileContent = read_content_of_file(nameOfFile)



