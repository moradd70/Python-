#Classes & Objects

class Person:
    __name = ''
    __email = ''
    
    
    def __init__(self, name, email):  #constructor
        self.__name = name
        self.__email = email
        
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
        
    def set_email(self, email):
        self.__email = email
        
    def get_email(self):
        return self.__email  
    
#brad = Person('Brad Luck', 'brad@gamil.com' )
#brad.set_name('Brad Luck')
#brad.set_email('brad@gamil.com') 

class Customer(Person):
    __balance = 0   # Property of a class
    
    def __init__(self, name, email, balance):  # constructor
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email) # function to inherit form another class
        
    def set_balance(self, balance):
        self.__balance = balance 
        
    def get_balance(self):
        return self.__balance 
    
    def toString(self): 
        return'{} has a balance of {} and can be contacted at {}'.format(self.__name, self.__balance, self.__email)
 
John = Customer ('John Doe', 'Jdoe@yahoo.com', '$250')
 
   
print(John.toString())   
     
    
            