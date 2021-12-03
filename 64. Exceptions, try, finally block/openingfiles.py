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
"""
try:
    tab = ["a", "b"]
    file = open("test.txt", "w") # HANDLER
    file.write("SAMPLE")
    print(tab[4])
 
    file.write("SAMPLE")
finally: #WHAT SHOULD BE DONE ALWAYS 
    file.close()
    
