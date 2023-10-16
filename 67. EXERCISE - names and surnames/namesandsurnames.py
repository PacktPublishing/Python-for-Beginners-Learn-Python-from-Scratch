"""
EXERCISE:

Load names and surnames from a file called:
namesurnames.txt

1) split values. The result should be a list of tuples:
[
 ("Arkadiusz", "Włodarczyk"),
 ("Some", "Guy"),
 ("Another", "AnotherMan")
]

2) save names to a file called names.txt
3) save surnames to a file called surnames.txt


"""
namesurnames = []

with open("namesurnames.txt", "r", encoding="UTF-8") as file:
    for line in file:
        namesurnames.append(tuple(line.replace("\n", "").split(" ")))

with open("names.txt", "w", encoding="UTF-8") as file:
    for item in namesurnames:
        file.write(item[0] + "\n")
        
with open("surnames.txt", "w", encoding="UTF-8") as file:
    for item in namesurnames:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")

