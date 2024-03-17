from __future__ import annotations

class Node:
    def __init__(self, x):
        self.x = x
        self.next = None

class List:
    def __init__(self):
        self.root = None
    def __repr__(self):
        curr_item = self.root
        string = ""
        while curr_item.next is not None:
            string += str(curr_item.x) + ","
            curr_item = curr_item.next
        string += str(curr_item.x)
        return "[" + string + "]" 

    def append(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            curr_item = self.root
            while curr_item.next is not None:
                curr_item = curr_item.next 
            curr_item.next = Node(item)
    
    def len(self):
        if self.root is None:
            return 0
        else:
            i = self.root
            len = 1
            while i.next is not None:
                len += 1
                i = i.next
        return len
    
    def get(self, i: int):
        curr_item = self.root
        count = 0
        while curr_item is not None:
            if count == i:
                return curr_item.x
            count += 1
            curr_item = curr_item.next
    
    def set(self, i: int, item):
        curr_item = self.root
        pos = 0 
        while curr_item is not None:
            if pos == i:
                curr_item.x = item

            curr_item = curr_item.next
            pos += 1

    def concat(self, l: List):
        curr_l_item = l.root
        while curr_l_item is not None:
            self.append(curr_l_item.x)
            curr_l_item = curr_l_item.next
                
if __name__ == "__main__":
    list = List()
    list.append(5)
    list.append(4)
    list.append("Hello")
    print(list)
    list2 = List()
    list2.append("Hi")
    list2.append(15)
    list.concat(list2)
    print(list)
    list2.set(1, "Changed")
    print(list)