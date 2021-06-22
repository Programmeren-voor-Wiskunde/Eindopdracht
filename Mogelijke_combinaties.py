
import copy

def mogelijke_combinaties():
    mogelijkheden = []
    for i in range(1,13):
        combinatie = [i]
        for j in range(i+1,13):
            combinatie.append(j)
            for k in range(j+1,13):
                combinatie.append(k)
                if combinatie not in mogelijkheden and len(combinatie)==3:
                    mogelijkheden.append(copy.copy(combinatie))
                    combinatie.pop()
            combinatie.pop()
    print(mogelijkheden)
    return mogelijkheden

mogelijke_combinaties()