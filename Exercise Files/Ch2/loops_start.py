#
# Example file for working with loops
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
  x = 0
  
#   while(x<5):
#       print x
#       x = x+1

#   for x in range(5,10):
#      print x  
#   # use a for loop over a collection
#   days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#   for cnt, d in enumerate(days):
#         print cnt, d       
  
  for cnt in range(5,10):
      if(cnt%2==0): 
          continue
      print cnt
  
  
if __name__ == "__main__":
  main()


