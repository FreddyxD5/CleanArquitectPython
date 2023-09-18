from functools import reduce
class Calc:
    def add(self, a, b, c):
        return a+b+c
    def add_mn(self, *args):        
        return sum(args)
    def sub(self, a, b):
        return a - b    
    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x,y : x*y, args)
    
    def avg(self, numbers, ut=None, lt=None):
        if len(numbers)==0:
            return 0            
        resultado = 0
        
        if ut is not None:
            filter_list = list(filter(lambda x: x<ut, numbers))
            resultado = sum(filter_list)/len(filter_list)
        elif lt is not None:
            filter_list = list(filter(lambda x: x>lt, numbers))
            resultado= sum(filter_list)/len(filter_list)
        else:
            resultado= sum(numbers)/len(numbers)

        return resultado
            

    def div(self, a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "inf"

