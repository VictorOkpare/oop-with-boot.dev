import json


class Professions:
    professions = []
    
    def __init__(self):
        self.profession = []
        
        
    def Add_profession(self, name, profession_type, experience  ):
         self.profession = {
            "name": name,
            "profession_type": profession_type,
            "experience": experience
        }
         Professions.professions.append(self.profession)  
         
    def log_professions(self):
     print("Here are the professionals we have in our data base")
     for profession in Professions.professions:
        print(f"{profession['name']} - {profession['profession_type']} - {profession['experience']} years of experience")
         
prof1 = Professions()
while True:
    name = input("Enter your name or type 'done' to exit: ")
    if name.lower() == 'done':
        break
    profession_type = input("Enter profession type: ")
    experience = int(input("Enter experience: "))
    prof1.Add_profession(name, profession_type, experience)

prof1.log_professions()

#saved the data in a JSON file
data = [profession for profession in Professions.professions]
with open('prof1.json', 'w') as f:
    json.dump(data, f, indent=4)




# print(Professions.professions)
       
       
        
        