class LeafElement: 
    
    def __init__(self, *args): 
        '''Takes the first positional argument and assigns to member variable "position".'''
        self.position = args[0]
    
    def showDetails(self): 
        '''Prints the position of the child element.'''
        print("\t", end="")
        print(self.position)
        

class CompositeElement: 
  
    def __init__(self, *args):
        '''Takes the first positional argument and assigns to member 
         variable "position". Initializes a list of children elements.'''
        self.position = args[0]
        self.children = []
        
  
    def add(self, child): 
        '''Adds the supplied child element to the list of children 
         elements "children".'''
        self.children.append(child)
        
  
    def remove(self, child): 
        '''Removes the supplied child element from the list of 
        children elements "children".'''
        self.children.remove(child)
  
    def showDetails(self): 
        '''Prints the details of the component element first. Then, 
        iterates over each of its children, prints their details by 
        calling their showDetails() method.'''
        print(self.position)
        for child in self.children:
            print("\t", end = "")
            child.showDetails()


topLevelMenu = CompositeElement("GeneralManager")
subMenuItem1 = CompositeElement("Manager1")
subMenuItem2 = CompositeElement("Manager2")
subMenuItem11 = LeafElement("Developer11")
subMenuItem12 = LeafElement("Developer12")
subMenuItem21 = LeafElement("Developer21")
subMenuItem22 = LeafElement("Developer22")
subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)
subMenuItem2.add(subMenuItem21)
subMenuItem2.add(subMenuItem22)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2) 
topLevelMenu.showDetails()
