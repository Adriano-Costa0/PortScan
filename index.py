import sys
from scanMany import scanTargets
from helpers.getInterval import getInterval
from helpers.isValidInterval import isValid

if len(sys.argv) < 2:
  print("- There are not enough parameters")
  exit() 

host = sys.argv[1]

try:
  if (sys.argv[2]):
    expression = sys.argv[2]
except:
    expression = '1-1024'

if not(isValid(expression)):
  print("- invalid interval")

interval = getInterval(expression)

scanTargets(host, interval)



