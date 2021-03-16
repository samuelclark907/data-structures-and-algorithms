from hashtable import HashTable
from linked_list import LinkedList, Node
import re

def repeated_word(bigstring):
    split_string = bigstring.split()
    # print(split_string)
    hashy = HashTable()
    for word in split_string:
        reg = re.sub(r'[^\w\s]','',word)
        lowerword = reg.lower()
        

        if hashy.contains(lowerword):  
            return lowerword
        else:
            hashy.set(lowerword, lowerword)
    return "No matches"
            

        




if __name__ == "__main__":
    print(repeated_word('I was always I alive always .'))
    
