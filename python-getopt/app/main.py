import getopt
import sys

def usage():
  print("""Usage:
  
Supported arguments: 
  * -h, --help: Help
  * list of parameters
  
Example: python-getopt -c""")

arguments = []
for argument in sys.argv[1:]:
  arguments.append(argument)
    

def main(arguments):
  try:
    options, parameters = getopt.getopt(sys.argv[1:], 'h', ["help"])
  except getopt.GetoptError as err:
    usage()
    sys.exit(1)

  for option, value in options:
    if option == "-h":
      usage()
      sys.exit(0)
    else:
      usage()
      sys.exit(1)

  if len(parameters) == 0:
    parameters = ["Anonymous"]

  output = "Hello,"
  for parameter in parameters:
    output += " " + parameter
  output += "!"
  return output
  
print(main(arguments))
