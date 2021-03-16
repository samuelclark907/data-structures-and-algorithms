from linked_list import LinkedList, Node

class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self._bucket = size * [None]

    def __str__(self):
        return self._bucket

    def _hash(self,key):
        total = 0
        for char in key:
            total += ord(char)
        primed = total * 7
        index = primed % self.size
        return index

    def set(self, key, value):
        hashed_key_index = self._hash(key)
        if not self._bucket[hashed_key_index]:
            self._bucket[hashed_key_index] = LinkedList()
        
        self._bucket[hashed_key_index].add((key, value))


    def get(self, requested_key):
        hashed_key_index = self._hash(requested_key)
        buck = self._bucket[hashed_key_index]
        if buck is None:
            return 'Nothing here my friend'
        while buck.head is not None:
            current = buck.head
            if current.data[0] == requested_key:
                return current.data[1]
            current = current.next   

            


    def contains(self, requested_key):
        hashed_key_index = self._hash(requested_key)
        buck = self._bucket[hashed_key_index]
        found = False
        if buck is None:
            return found
        while buck.head is not None:
            current = buck.head
            if current.data[0] == requested_key:
                found = True
                return found
            current = current.next
        return found
            

if __name__ == "__main__":
    hashy = HashTable()
    hashy.set('bird', '1')
    hashy.set('bidr', '3')
    hashy.set('cat', 'dog')
    # print(hashy.get('dog'))
    # print(hashy.__dict__)
    print(hashy.get('bidr'))
    print(hashy.contains('bidrdas'))
    print(hashy.get('cat'))