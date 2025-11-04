class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips 
        self.pockets = pockets

    def showDetails(self):
        print(f"The details of your Products are {self.material}, {self.zips}, {self.pockets}")

Reebok = Factory("leather","5","4")
Nike = Factory("canvas","3","2")
Reebok.showDetails()
Nike.showDetails()