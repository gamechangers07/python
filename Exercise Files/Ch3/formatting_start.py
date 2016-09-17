#
# Example file for formatting time and date output
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import datetime

def main():
    now = datetime.now()
    print now.strftime("%y")
    print now.strftime("%c")
    print now.strftime("%X")
    print now.strftime("%x")

if __name__ == "__main__":
  main();
  

