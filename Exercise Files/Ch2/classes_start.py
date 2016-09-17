#
# Example file for working with classes
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


class MyClass():
    def method1(self):
        print "MyClass method1"
    def method2(self,someString):
        print "MyClass method2"
        
class AnotherClass(MyClass):
    def method3(self):
        MyClass.method1(self)
        print "AnotherClass method3"
    def method2(self):
        print "AnotherClass method2"
        
def main():
    obj = MyClass()
    obj.method1()
    obj.method2("someString")
    
    obj1 = AnotherClass()
    obj1.method1()
    obj1.method2()
    obj1.method3()
    
    
  
if __name__ == "__main__":
  main()
