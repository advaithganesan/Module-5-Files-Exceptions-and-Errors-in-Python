  try:
      with open("output.txt", "r") as file:
          content = file.read()
          print(content)
  except FileNotFoundError:
      print("The file does not exist.")
  except IOError:
      print("An error occurred while accessing the file.")
