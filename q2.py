def surviving_ships(ships):
    if len(ships)<=1:
        return ships
    elif len(ships)==2:
        if ships[0]>0 and ships[1]<0:
            if abs(ships[0])>abs(ships[1]):
                return [ships[0]] 
            elif abs(ships[0])<abs(ships[1]): 
                return [ships[1]]
            else:
                 return []    
        else:
            return ships
    elif len(ships)>2:
        while len(ships)>2 and ships[0]>0 and ships[1]<0:
            if abs(ships[0])<abs(ships[1]):
                ships.pop(0)
            elif abs(ships[0])>abs(ships[1]):
                ships.pop(1)
            else:
                ships=ships[2:]
        if len(ships)==1:
            return ships       
        ships= [ships[0]]+surviving_ships(ships[1:]) 
        if len(ships)==1:
            return ships     
        if ships[0]*ships[1]>0:
            return ships
        else:
            if ships[0]<0 and ships[1]>0:
                return ships
            else:    
                return surviving_ships(ships)                   
if __name__=="__main__":
    print(surviving_ships([6,3,-5]))                 
    print(surviving_ships([8,-8]))                   
