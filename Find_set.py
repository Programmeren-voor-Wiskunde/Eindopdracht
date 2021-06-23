#Ik heb deze functie nog niet getest, want is_set bestaat geloof ik nog niet.

import copy

def possible_combinations(deck: list):
    """
    Deze functie geeft alle mogelijke combinaties van drie verschillende kaarten 
    uit een verzameling van twaalf kaarten, waarbij de volgorde niet uitmaakt.
    
    input: list of the cards in the set of twelve cards
    output: all possible combinations of three cards in this set of twelve cards.
    """
    possibilities = []
    for i in range(12):
        combination = [deck[i]]
        for j in range(i+1,12):
            combination.append(deck[j])
            for k in range(j+1,12):
                combination.append(deck[k])
                if combination not in possibilities and len(combination)==3:
                    possibilities.append(copy.copy(combination))
                    combination.pop()
            combination.pop()
    print(possibilities)
    return possibilities

def find_set(kaartendek: list):
    """
    This function finds a Set in a set of twelve cards.
    
    Input: list of twelve cards
    Output: If there is a Set, this function returns the indices of the cards
            that form a Set.
            If there isn't any Set in this set of twelve cards, the function
            return False.
    """
    Possible_combinations = possible_combinations(kaartendek)
    for combination in Possible_combinations:
        card1 = combination[0]
        card2 = combination[1]
        card3 = combination[2]
        if is_set(card1, card2, card3):
            return combination
        elif combination == Possible_combinations[-1] and is_set(card1, card2, card3)==False:
            return False