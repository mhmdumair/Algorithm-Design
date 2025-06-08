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


# print(fractionalKnapsack([Item(3, 5),
#                           Item(5, 8),
#                           Item(2, 3),
#                           Item(4, 6),
#                           Item(6, 9),
#                           Item(7, 10),
#                           Item(5, 7),
#                           Item(3, 4)
#                           ], 15))

def knapsackZeroOne(items,W):
    items.sort(key = lambda x : (x.value/x.weight),reverse =True)
    w = 0
    value = 0
    for item in items:
        if item.weight < W:
            value+=item.value
            w+=item.weight
            W-= item.weight
    print([(x.weight,x.value) for x in items])
    print("Value",value)
    print("Weight",w)



knapsackZeroOne([Item(3, 5),
                          Item(5, 8),
                          Item(2, 3),
                          Item(4, 6),
                          Item(6, 9),
                          Item(7, 10),
                          Item(5, 7),
                          Item(3, 4)
                          ], 15)