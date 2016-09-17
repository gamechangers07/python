#
# Example file for working with conditional statements
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
  x, y = 103, 100
  
# if(x<y):
#     str ="X is less than y"
# elif(x==y):
#     str ="X is less than y"
# else:
#      str ="X is greater than y"
# print str

  str ="X is less than y" if (x<y) else "X is greater or equal to y"
  print str
  
if __name__ == "__main__":
  main()
