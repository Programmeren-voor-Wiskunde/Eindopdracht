
import copy

def mogelijke_combinaties(kaartendek: list):
    """
    Deze functie geeft alle mogelijke combinaties van drie verschillende kaarten 
    uit een verzameling van twaalf kaarten, waarbij de volgorde niet uitmaakt.

    """
    mogelijkheden = []
    for i in range(12):
        combinatie = [kaartendek[i]]
        for j in range(i+1,12):
            combinatie.append(kaartendek[j])
            for k in range(j+1,12):
                combinatie.append(kaartendek[k])
                if combinatie not in mogelijkheden and len(combinatie)==3:
                    mogelijkheden.append(copy.copy(combinatie))
                    combinatie.pop()
            combinatie.pop()
    print(mogelijkheden)
    return mogelijkheden

mogelijke_combinaties()