import sys
numVal = 0.1
taxVal = 0.1
if len(sys.argv) != 3:
  raise ValueError("Invalid Arguments Error!")
else:
  try:
    numVal = float(sys.argv[1])
    taxVal = float(sys.argv[2])
    print(f"With tax of {str(taxVal)}, {str(numVal)} will turn into {str(numVal * taxVal)}.")
  except:
    raise ValueError("Invalid Arguments Error!")
