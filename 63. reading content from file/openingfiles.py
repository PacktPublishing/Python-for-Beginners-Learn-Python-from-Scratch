"""
FILE - name of location that stores pernamently data

RAM - temporary data storage 

Operations you can do on a file:
1) opening
2) writing/reading
3) closing

basic modes(ways) of opening files:
r - R ead  - default
w - W rite - if the file existed (will be removed), if not will be created
a - A ppend (adding new content at the end)

extension is simply saying TEXT that is there only to
            make sure other programs know what is inside the
            type of file for example txt suggest there is text inside


EXCEPTION - an exceptional (unusal) situation in program that makes
            your program suddenly stop working

read
readline
readlines

splitlines
"""

with open("namesurnames.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line, end='')

    
