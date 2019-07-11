def find_moves(checkers, dice1, dice2):
    ############# Inputs Control #############
    if dice1<1 or dice1>6 or dice2<1 or dice2>6:
        return "ERROR! Please check the inputs. (Dices)"
    for k in checkers.keys():
        if checkers[k]<0 or k<1 or k>24:
            return "ERROR! Please check the inputs. (Checkers)"
    if dice1 == dice2:
        print("WARNING! Only 2 moves calculated (Equal dices 4 moves not supported)\n")
    
    ##### Defining Some Necessary Lists ######
    importants = [5, 6, 7, 8, 17, 18, 19, 20]
    lots = []
    result = []

    ######## Initial Score Calculation #######
    score1=0
    for k in checkers.keys():
        if checkers[k]==1:
            score1-=1
        if checkers[k]==2:
            if k in importants:
                score1+=2
            else:
                score1+=1
        if checkers[k]>2:
            lots.append(k)

    ########## Make Possible Moves ###########
    for i in range(2):
        if i==1:
            if dice1 == dice2:
                break
            dice1,dice2 = dice2,dice1
        for key1 in checkers.keys():
            if checkers[key1]<1:
                continue
            location1 = key1+dice1
            if location1>24:
                break
            for key2 in checkers.keys():
                if key1==key2 and checkers[key1]==1 or checkers[key2]<1:
                    continue
                location2 = key2+dice2
                if location2>24:
                    break
                myCheckers = checkers.copy()
                if location1 in myCheckers:
                    myCheckers[location1]+=1
                else:
                    myCheckers[location1]=1
                myCheckers[key1]-=1
                if location2 in myCheckers:
                    myCheckers[location2]+=1
                else:
                    myCheckers[location2]=1
                myCheckers[key2]-=1
        
        ######## Final Score Calculation #########
                score2=0
                for k in myCheckers.keys():
                    if myCheckers[k]==1:
                        score2-=1
                    if myCheckers[k]==2 and k not in lots:
                        if k in importants:
                            score2+=2
                        else:
                            score2+=1
                score = score2-score1

        ########## Prepare Result List ###########
                if score>0:
                    result.append(((key1,location1),(key2,location2),score))
    return result
    
checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
print(find_moves(checkers,6,1))

# Alperen Cubuk