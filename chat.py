while True:
  name = input("Name: ")
  f = open("demofile.txt", "r")
  print(f.read())
  
  text = input("Input Text Here: ")
  
  i = open("demofile.txt", "a")
  i.write(f"{name.capitalize()}: {text}")
  i.close()
