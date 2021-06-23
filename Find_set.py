import copy

class Kaart:
    """
    Represents a card of the game Set"
    
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


def possible_combinations(set_of_twelve: list):
    """
    This function returns all the possible combinations of three different cards 
    from a set of twelve cards, in which the order of the cards doesn't matter.
    
    input: list of the cards in the set of twelve cards
    output: all possible combinations of three cards in this set of twelve cards.

    """
    possibilities = []
    for i in range(12):
        combination = [set_of_twelve[i]]
        for j in range(i+1,12):
            combination.append(set_of_twelve[j])
            for k in range(j+1,12):
                combination.append(set_of_twelve[k])
                if combination not in possibilities and len(combination)==3:
                    possibilities.append(copy.copy(combination))
                    combination.pop()
            combination.pop()
    return possibilities

def find_set(set_of_twelve: list):
    """
    This function finds a Set in a set of twelve cards.
    
    Input: list of twelve cards
    Output: If there is a Set, this function returns a list with the indices 
            of the cards that form a Set.
            If there isn't any Set in this set of twelve cards, the function
            return False.
    """
    Possible_combinations = possible_combinations(set_of_twelve)
    for combination in Possible_combinations:
        card1 = combination[0]
        card2 = combination[1]
        card3 = combination[2]
        if card1.is_set(card2, card3):
            return combination
        elif combination == Possible_combinations[-1] and card1.is_set(card2, card3)==False:
            return False

a0 = Kaart(1,0,1,2)
a1 = Kaart(1,2,0,2)
a2 = Kaart(2,1,0,1)
a3 = Kaart(2,1,2,2)
a4 = Kaart(0,0,0,2)
a5 = Kaart(0,2,0,1)
a6 = Kaart(1,1,1,1)
a7 = Kaart(2,2,0,2)
a8 = Kaart(1,0,1,2)
a9 = Kaart(1,0,0,2)
a10 = Kaart(2,0,2,0)
a11 = Kaart(2,0,2,1)
Set_of_Twelve = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11]

print(find_set(Set_of_Twelve)[0])
print(find_set(Set_of_Twelve)[1])
print(find_set(Set_of_Twelve)[2])

print(len(possible_combinations(list(range(12)))))