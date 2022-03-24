# Bounding methods (class method) : which is present inside class and 
#eligible to access global variable and not a local variable which is appeared 
#inside the class

# Un-bounding methods (Static method) : which is present inside 
# class and not eligible to access global variable and local variable which 
# is appeared inside the class

# What are the differences between Classmethod and StaticMehtod?
# Class Method    Static Method
# The class method takes cls (class) as first argument.   The static method does not take any specific parameter.
# Class method can access and modify the class state. Static Method cannot access or modify the class state.
# The class method takes the class as parameter to know about the state of that class.    Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters.
# @classmethod decorator is used here.    @staticmethod decorator is used here.

# The Static methods are used to do some utility tasks, and class methods are used for factory methods. The factory methods can return class objects for different use cases.

class abc:
    outOne = 1  # Class variable - can able to access this variable using any of the instance.
    outTwo = 2  # class variable
    def __init__(self,val1,val2):
        self.val1 = val1  # Instance variable - Can able to access only using the specific instance
        self.val2 = val2  # Instance variable

    def newFactor(self):
        print "inside new factor"
# Bound methods
    @classmethod
    def classmethod(ref,sep):
        print "Inside method now"
        print ref.outOne
# Unbound method (Cannot call class abc's global variable inside static method)
    @staticmethod
    def smalA():
        print "Terms and conditions"

class xyz(abc):
    def __init__(self):
        pass

obj = abc(10,234)
obj.classmethod(8)
obj.smalA()
print dir(obj)
print(obj.outOne)
print obj.val1
print "Document:",abc.__doc__
print "Dict:",abc.__dict__
print "Module:",abc.__module__
print "Base:",abc.__base__
print "Name:",abc.__name__

print getattr(abc,"new_world","Not present")
print setattr(abc,"file","newname")
print obj.file
print setattr(abc,"id","termOne")
print obj.id
print issubclass(xyz, abc)



