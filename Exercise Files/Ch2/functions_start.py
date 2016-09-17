#
# Example file for working with functions
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

   

# define a function
def func1():
  print "I am a function"
  

# function that takes arguments
def func2(arg1, arg2):
  print arg1, " ", arg2

# function that returns a value
def cube(x):
  return x*x*x

#function with variable number of arguments  
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result
  
#function with variable number of arguments
def multi_add(*args):
  result = 0;
  for x in args:
    result = result + x
  return result  
  
  
  
  
#func1()
#print func1()
#func2(10,20)
#print func2(10,20)
#print cube(3)
#print power(x=2,num=3)
print multi_add(2,3,5,7)