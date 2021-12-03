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

tell - tells, where is the file indicator (file position of last operation)
seek - seeks the indicator and changes its place to the value we want

JPG

"""

with open("namesurnames.txt", "a", encoding="UTF-8") as file:
    file.write("Arkadiusz Marx")
   
    

    
