class Cat:
    
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age
                
    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    def get_cat(self):
        return self.name, self.gender, self.age
        
        
