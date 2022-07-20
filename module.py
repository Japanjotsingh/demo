class Person:
    def __init__(self, name , gender):
	    
        self.name = name
        self.gender = gender
     

    def say_hi(self):
	    print('Hello, my name is', self.name)

    def gen(self):
        print('My gender is', self.gender)