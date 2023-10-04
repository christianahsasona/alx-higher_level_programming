<h1> 0x08. Python - More Classes and Objects </h1>
<h2> Class Attributes </h2>
 Instance attributes are owned by the specific instances of a class. That is, for two different instances, the instance attributes are usually different
 In the following interactive Python session, we can see that the class attribute "a" is the same for all instances, in our examples "x" and "y". Besides this, we see that we can access a class attribute via an instance or via the class name:
<code>
class A:
    a = "I am a class attribute!"
x = A()
y = A()
x.a
</code>
<code>
OUTPUT:
'I am a class attribute!'
y.a
</code>
<hr />
<h2> Properties vs. Getters and Setters </h2>
 Getters(also known as 'accessors') and setters (aka. 'mutators') are used in many object oriented programming languages to ensure the principle of data encapsulation. 
<code>
class OurClass:
    def __init__(self, a):
        self.OurAtt = a
    @property
    def OurAtt(self):
        return self.__OurAtt
    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val
x = OurClass(10)
print(x.OurAtt)
</code>
<code>
OUTPUT:
10
</code>
 Christianahsasona || ALX &copy; 2023
