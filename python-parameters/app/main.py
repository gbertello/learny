import sys

parameters = []
for parameter in sys.argv[1:]:
  parameters.append(parameter)

if len(parameters) == 0:
  parameters = ["Anonymous"]
  
def main(parameter):
  output = "Hello,"
  for parameter in parameters:
    output += " " + parameter
  output += "!"
  return output
  
print(main(parameters))
