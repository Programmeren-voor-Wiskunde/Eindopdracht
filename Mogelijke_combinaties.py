import copy

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