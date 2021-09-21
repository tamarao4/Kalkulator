"""    Implemeniranje steka na osnovu liste    """
 
 
# klasa - za izuzetke Steka
class StackError(Exception):
    pass
 
# implementacija steka
class Stack(object):
    
    def __init__(self):             #kosnstrukot
        self._data = []
        
    def __len__(self):              #br. el. na steku
        return len(self._data)
    
    def is_empty(self):             # da le je stek prazan
        return len(self._data) == 0
    
    def push(self, e):              # dodavanje el. na stek
        # e je novi el.
        self._data.append(e)
        
    def top(self):                  # vraca el na vrh steka
        if self.is_empty():
            raise  StackError("Stek je prazan.")
        return self._data[-1]
    
    def pop(self):                  # izbacuje el. sa vrha
        if self.is_empty():
            raise StackError("Stek je pazan.")
        return self._data.pop()
    
    
if __name__ == "__main__":
    s = Stack()
    s.push(2)
    print (len(s))
    s.push(5)
    
    print (s.is_empty())
    print (s.top())
    s.pop()
    
    print (s.is_empty())
    s.pop()
    
    print (s.is_empty())
    
