import math

class MyService:
    def __init__(self):
        # dict
        self.func_map = {
            'floor': self.floor,
            'nroot': self.nroot,
            'reverse': self.reverse,
            'validAnagram': self.validAnagram,
            'sort': self.sort
        }
        
    def floor(self, x):
        return math.floor(x)
    
    def nroot(self, n, x):
        return x ** (1/n)
    
    def reverse(self, s):
        return s[::-1]
    
    def validAnagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)
    
    def sort(self, strArr):
        return sorted(strArr)
    
    def call_method(self, method_name, *args):
        if method_name in self.func_map:
            return self.func_map[method_name](*args)
        else:
            raise ValueError(f"Method {method_name} not found.")