class Profession:
    def __init__(self):
        self.list = []
        self.name = "Miracle"
        
    # A method 
    def Addprofession(self, profession):
        self.list.append(profession)
    
    def filterProfession(self, type):
        for profession in self.list:
            if profession["type"].lower() == type:
                print(profession)
            else:
                print("no result")
                
engineers = Profession()

engineers.Addprofession(
    {"type": "software_engineer",
     "name": "Miyagi Bender",
     "experience": 6
})
engineers.Addprofession(
    {"type": "Mechanical_engineer",
     "name": "Rashford Bender",
     "experience": 6
})
engineers.Addprofession(
    {"type": "chemical_engineer",
     "name": "Maguire Bender",
     "experience": 4
})
engineers.Addprofession(
    {"type": "aeronautic_engineer",
     "name": "Charlie Bender",
     "experience": 4
})



engineers.filterProfession("chemical_engineer".lower())


#Inheritance
class Engineers(Profession):
    def __init__(self):
        super().__init__()
        
  
        

        
class Doctors(Profession):
    def __init__(self, type, name, experience):
        super().__init__() 
        # self.Addprofession({"type": type, "name": name, "experience": experience})
        
    def AddDoctors(self, type, name, experience):
        self.Addprofession(
            {"type": type,
            "name": name,
            "experience": experience}
        )
    # doc = AddDoctors( "doctor", "David", 29)
 
  
doc = Doctors("Doctor", "James Oni", 20)
doc = Doctors("Nurse", "Jameeee ", 60)
doc = Doctors("Lawyers", "lanre", 15)

print(doc.list)

# doc.filterProfession("Nurse".lower())
