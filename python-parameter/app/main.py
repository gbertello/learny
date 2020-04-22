import sys

parameter = ""
if len(sys.argv) > 1:
  parameter = sys.argv[1]
  
def main(parameter):
  if parameter == "":
    parameter = "Anonymous"
  output = "Hello, " + parameter + "!"
  return output
  
print(main(parameter))
