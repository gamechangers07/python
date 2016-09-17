#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time
from datetime import datetime

def main():
  today = date.today()
  print today.weekday()
  
  print datetime.now()
  print datetime.time(datetime.now())
  print datetime.date(datetime.now())

  # weekday returns 0 (monday) through 6 (sunday)
  wd = date.weekday(today)  
  
  # Days start at 0 for Monday 
  days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  print "Today is day number %d testing"  %wd
  print "Which is a " + days[wd]


if __name__ == "__main__":
  main();
  