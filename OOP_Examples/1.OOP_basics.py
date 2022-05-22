#we can create class using "class" keyword
class User:
    # class attributes are define on the class itself and we can access as: Class_Name.anything
    active_users = 0
    
    #__init__() method calls itself any time a new isntance is created.
    def __init__(self, first_name, last_name, age):
        #self param refers to any instance that we will be creating. It refers to user1 and user2 in this particular scenario. 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        print(f"user created: {first_name} {last_name}, {age} years old")
        User.active_users += 1
        # as we know that __init__() is called everytime an instance is created so we are adding 1 to active_users each time an instance is created 
        
    #Instance mehtods: are methods inside a class that belong to the isntances of a class 
    # and we can call them through instances. we create as:
    def likes(self, thing):
        return f"I am {self.first_name} and I like {thing}."
        # again the self param here will refer to any object that we call this method through.
        
    #Class methods: are methods that belong to the class itself. we create as:  
    @classmethod
    def display_active_users(cls):
        # Automatically the class is passed into the class methods as object was automatically passed into isntance method 
        # here cls acts the same as self but self refers to instance of the class while cls refers to the class itself.
        print(f"There are currently {cls.active_users} active users.")
    
        

user1 = User("Joe", "Jack", 23) 
user2 = User("Donald", "Trump", 67)
# user1 and user2 will be automatically passed into __init__() method's self param 
# self refer to the user1/user2 instances that we are creating.
# so self.first_name means user1.first_name and then self.first_name means user2.first_name. 
# everything we manually pass into User() will be passed to the __init__() method's params.
# for example: user("Joe") will be passed into __inti__(first_name) and similarly all other params.
# we don't need the print statement in the __init__ method but it is there to illustrate that
# the params we pass into User() will be passed to the __init__() methods params.

# calling instance method through the isntances 
print(user1.likes("ice cream"))
print(user2.likes("pizza"))

# accessing the Class attribute 
print(User.active_users)

# calling class method
User.display_active_users()
