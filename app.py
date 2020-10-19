print("Title of program: Post-exam bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "disappointed":
      feelings_list.append("bored")
      encouragement_list.append("positivity is the way to go, keep trying")
      counter += 1
    if each_word == "relaxing":
      feelings_list.append("relaxing")
      encouragement_list.append("remember to stay healthy too")
      counter += 1
    if each_word == "contented":
      feelings_list.append("contented")
      encouragement_list.append("good job, give yourself a pat on your shoulder")
      counter += 1
 if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("go and meet up with your friends to hang out")
      counter += 1
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
