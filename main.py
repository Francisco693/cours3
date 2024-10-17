name = "Jean"
age = 30
activities = ["tennis","athle"]
preference = "python"
Job = "prof"

sentence = f"""
Presentation:
    -My name : {name}
    -My age : {age}
    -My activities : {activities}
""".upper()
  
print(sentence)

if name == "jean":
    print("Yes cest bien Jean")

new_sentence = f"{True if name == "jean" else False}"    
print(new_sentence)