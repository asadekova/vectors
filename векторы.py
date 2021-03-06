#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

class Vector:
    
 
    def timeit(method): #я не придумала какой декоратор можно сделать поэтому пусть будет такой. его можно применить к любому методу, но я ограничилась одним
        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            delta = (te - ts) * 1000
            print(f'{method.__name__} выполнялся {delta:2.2f} ms')
            return result
        return timed
       
    
    def __init__(self, *args): #инициализация класса
        assert all(type(arg) in (int, float) for arg in args) #учим программу ругаться, если мы вводим не int и float
        self.args = args 
        self.args = list(self.args) #класс нам создал кортеж, а для удобства работы мы переводм его в изменяемый список
    
   
    @timeit 
    def __eq__(self, other): #равенство векторов
        if self.args == other.args:
            return True
        else:
            return False
    
    
    def __add__(self,other): #сложение векторов
        res = []
        if len(self.args) == len(other.args):
            for i in range(len(self.args)):
                res.append(self.args[i] + other.args[i])
            return Vector((*res))
        else:
            return False
        
    def __sub__(self,other): #вычитание векторов
        res = []
        if len(self.args) == len(other.args):
            for i in range(len(self.args)):
                res.append(self.args[i] - other.args[i])
            return Vector((*res))
        else:
            return False
        

    def __mul__(self,other): #скалярное произведение двух векторов
        if isinstance(other, Vector):
            res = 0
            if len(self.args) == len(other.args):
                for i in range(len(self.args)):
                    res = res + (self.args[i] * other.args[i])
                return res
            else:
                return False
        elif (isinstance(other, int) or isinstance(other, float)): #умножение на число
            res = []
            for i in range(len(self.args)):
                res.append(self.args[i]*other)
            return Vector(*res)
        
    def __rmul__(self,other): #говорим, что у нас * коммутативная (необходимо только если операция * не определена для одного из классов)
        if (isinstance(other, int) or isinstance(other, float)):
            res = []
            for i in range(len(self.args)):
                res.append(self.args[i]*other)
            return Vector(*res)
    
    
    def __abs__(self): #модуль вектора
        return((self*self)**0.5)
          
    def angle(self,other): #косинус угла между двумя векторами
        return((self*other)/((abs(self))*(abs(other))))
    
    
    @classmethod #а это сойдёт за декоратор?)0)00))
    def __from_string__(cls, string): #чтобы можно было читать как вектор строку с запятыми: 1, 2, 4
        read = []
        for elem in string.split(', '):
             read.append(int(elem))
        return Vector(*read)
        
        
    
    def __str__(self): #вывод в формате строки
        return str(self.args)
    
    def __repr__(self):
        return repr(self.args)
    
    def __iter__(self): #итератор
        i = 0
        while i < len(self.args):
            yield self.args[i]
            i += 1

    
    
if __name__ == '__main__': #код теста
    a = Vector(1,1,2,4,4,5,6)
    b = Vector(2,2,1,3,3,8,1)
    c = Vector(1,1,2)
    
    for args in b: #проверка итерируемости класса векторов
        print(args)
        
    print('a, b, c:', repr(a), repr(b), repr(c)) 
    print('addition commutativity test, a+b=b+a:', repr(a+b), repr(b+a))
    print('addition length equality test a+c=False:', a+c)
    print('subtraction test, a-b, b-a:', repr(a-b), repr(b-a))
    print('subtraction length equality test a-c=False:', a-c)
    print('scalar multiplication commutativity test, a*b=b*a:', a*b, b*a)
    print('scalar multiplication length equality test a*c=False:', a*c)
    print('multiplication by number commutativity test, a*3=3*a:', repr(a*3), repr(3*a))
    print('module test:', abs(a), abs(b), abs(c))
    print('angle test, a^b=b^a:', a.angle(b), b.angle(a))
    assert Vector.__from_string__("3, 45, 5") == Vector(3, 45, 5)

