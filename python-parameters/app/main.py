import sys

parameters = []
for parameter in sys.argv[1:]:
  parameters.append(parameter)
  
def main(parameters):
  if len(parameters) == 0:
    parameters = ["Anonymous"]
    
  output = "Hello,"
  for parameter in parameters:
    output += " " + parameter
  output += "!"
  return output
  
print(main(parameters))
