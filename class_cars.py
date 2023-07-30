class car:
    def __init__(self, name, model, year):
        self.name = str(name)
        self.model = str(model)
        self.year = int(year)

    def __del__(self):
        return self.name + " model" + self.model + "year"+str(self.year)
    def bmw(self):
        print("this is bmw " , str(self.name) , " this model is " +str( self.model) , " it's made in " , int(self.year))
    def benz(self):
        print("this is benz " + str(self.name) + " this model is " + str(self.model) + " it's made in " , int(self.year) )