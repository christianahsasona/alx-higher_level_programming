<h1> 0x06. Python - Classes and Objects </h1>
 A class is a user-defined blueprint or prototype from which objects are created. Class can be considered as a user-defined data type. Generally, a class contains data members known as attributes of the class and member functions that are used to modify the attributes of the class.
 Example of Class Definition:
<code> 
 class ClassName:
     #your statements
</code>
<h2> Creating a Python Class</h2>
 The class keyword indicayes that you are creating a class followed by the name of the class.
 For Example:
 Let's create a class Dog
<code>
class Dog:
    sound "bark"
</code>
'/c/Users/OLUWATOSIN/Desktop/Microsoft Office Groove 2007.lnk'<hr />
<h2> Object of Python Class </h2>
 An onject is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values.
 An objest consists of:
- State: It represents the properties/attributes of an object. Example: Color, Age, Breed
- Behaviour: It represents response of an object to other objects. Example: Bark, Sleep,Eat
- Identity: It gives a unique name to an object and it enables one object to interact with other objects. Example: Name
<h2>Example of Python Class and Object </h2>
 Creating an object in python involves instantiating a class to create a new instance of that class. This process is referred to as object instantiation.
 <h2> Python3 </h2>
<code>
# Python3 program to
# demonstrate instantiating
# a class
class Dog:
 
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
 
 
# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
</code>

 <h2> Output: </h2>
<code>
mammal
I'm a mammal
I'm a dog
</code>
<a href="https://www.tutorialspoint.com/python/python_classes_objects.htm" style="decoration:none"> for further reading and understanding of Python Classes and Objects</a>
[^1] Author:@christianahsasona
