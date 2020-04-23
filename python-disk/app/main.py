import getopt
import os
import sys

def usage():
  print("""Usage:
  
Supported arguments: 
  * -h, --help for help
  * -v: Specify volume to be used
  
Example: python-disk""")

if not os.path.exists("/mnt/disk"):
  print("Specify volume")
  sys.exit(1)

arguments = []
for argument in sys.argv[1:]:
  arguments.append(argument)
    

def main(arguments):
  try:
    options, parameters = getopt.getopt(sys.argv[1:], 'hv:', ["help"])
  except getopt.GetoptError as err:
    usage()
    sys.exit(1)
  
  for option, value in options:
    if option == "-h":
      usage()
      sys.exit(0)
    elif option == "-v":
      continue
    else:
      usage()
      sys.exit(1)
  
  n = len(os.listdir("/mnt/disk"))
  output = "There are %s file(s)" % n
    
  return output
  
print(main(arguments))
