class Item:
    def __init__(self,weight,value):
        self.value = value
        self.weight = weight

def fractionalKnapsack(items,W):
    totalValue = 0
    items.sort(key= lambda x:(x.value/x.weight),reverse=True)
    for item in items:
        if item.weight<W:
            W-=item.weight
            totalValue+=item.value
        else:
            totalValue+=(W/item.weight)*item.value
            break

    return totalValue


print(fractionalKnapsack([Item(1, 200),
                          Item(3, 240),
                          Item(2, 140),
                          Item(5, 150)], 6))