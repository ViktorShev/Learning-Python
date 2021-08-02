class TestMethod:
    x = 1 
    b = 2
    
    def __init__(self):
        pass
        
    @classmethod
    def suma(cls):
        return(print(cls.x + cls.b))
    
    @staticmethod
    def suma1():
        return(print(cls.x + cls.b))
    