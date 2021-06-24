import random

class Kaart:
    """
    Represents a card of the game Set
    
    Attributes: color, number, filling, shape.
    Methods: init, str
    Functions: is_set
    """
    
    def __init__(self,color=0,number=0,filling=0,shape=0):
        self.color=color
        self.number=number
        self.filling=filling
        self.shape=shape
        
    def __str__(self):
        return("("+str(self.color)+","+str(self.number)+","+str(self.filling)+","+str(self.shape)+")")
        
    def is_set(self,other1,other2):
        matchings={"color": False,"number": False, "filling": False, "shape": False}
        matchings["color"]=(self.color==other1.color and other1.color==other2.color) or (self.color!=other1.color and other1.color!=other2.color and self.color!=other2.color)
        matchings["number"]=(self.number==other1.number and other1.number==other2.number) or (self.number!=other1.number and other1.number!=other2.number and self.number!=other2.number)
        matchings["filling"]=(self.filling==other1.filling and other1.filling==other2.filling) or (self.filling!=other1.filling and other1.filling!=other2.filling and self.filling!=other2.filling)
        matchings["shape"]=(self.shape==other1.shape and other1.shape==other2.shape) or (self.shape!=other1.shape and other1.shape!=other2.shape and self.shape!=other2.shape)
        for i in matchings:
            if matchings[i]==False:
                return matchings[i]
        return True

def generate_deck():
    """
    This function creates a list of all possible cards in the game Set.
    
    Output: list with 81 different Set-cards
    """
    deck = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    deck.append(Kaart(i,j,k,l))
    return deck

def create_set_of_twelve(deck):
    set_of_twelve = [0 for i in range(12)]
    for i in range(len(set_of_twelve)):
        random_card_index = random.randint(0,len(deck))
        print(random_card_index)
        set_of_twelve[i] = str(deck[random_card_index])
        del deck[random_card_index]
    print(set_of_twelve)
    return set_of_twelve