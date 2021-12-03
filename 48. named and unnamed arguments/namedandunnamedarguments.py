"""
    Named(keyword) and unnamed (positional) arguments
    
    keyword - key=value 
    positional - where the sequence (position) matters
"""

def greet(name, message="Hello", seperator=" "):
    print(message, name, sep=seperator)

#print("sample", "sample2", "sample3", ',')    

greet("Arkadiusz", seperator="\n")
