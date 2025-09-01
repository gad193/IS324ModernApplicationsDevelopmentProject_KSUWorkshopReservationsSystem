class Animal:

    def __init__(self,n,a,t):
        self.__name= n
        self.__age = a
        self.__type = t

    def __str__(self):
        return str( self.__name)+","+str(self.__age)+","+str(self.__type)


    def set__age(self,a):
        self.__age=a

    def get__age(self):
        return self.__age

    def get__type(self):
        return self.__type