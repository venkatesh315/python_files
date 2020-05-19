

# this is a simple multiplayer ipl auction game

from const import batsman,bowlers,all_rounders,wkb,batsman_rate,bowlers_rate,all_rounders_rate,wkb_rate
print("The ipl auction begins !!!")
team1 = input("enter 1st user's ipl team name  ")

team2 = input("enter 2nd user's ipl team name  ")

total_amount = {team1: 30000, team2: 30000}


def auction(player, rate, bid1, bid2, t1, t2, m1, m2, current_bid, current_bid1, current_bid2, t1_players, t2_players):
    import sys

    p = player
    r = rate
    b1 = bid1
    b2 = bid2
    t1 = team1
    t2 = team2

    cb1 = current_bid1
    cb2 = current_bid2

    print("Does", t1, "wants to bid?")

    while True:
        try:
            ch1 = input("enter the valid choice(y,n)")
        except  ValueError:
            print("you have to enter the correct character")
            continue

        if ch1.lower() not in ['y', 'n']:
            print("Not an appropriate choice")
            continue
        else:
            ch1 = ch1.lower()
            break
    while True:
        if (ch1 == 'y'):
            try:
                b1 = int(input("enter the bid amount(minimum 50)"))
            except ValueError:
                print("enter only integer data")
                continue

            if (b1 < 50 or b1 > 30000):
                print("You have entered bid amount less than 50 or greater than 30000")
                continue

            else:
                break
        else:
            break

    print("Does", t2, "wants to bid?")
    while True:
        try:
            ch2 = input("enter the valid choice(y,n)  ")
        except  ValueError:
            print("you have entered a wrong choice")
            continue

        if ch2.lower() not in ['y', 'n']:
            print("Not an appropriate choice")
            continue
        else:
            ch2 = ch2.lower()
            break
    while True:
        if (ch2 == 'y'):

            try:
                b2 = int(input("enter the bid amount (minimum 50)  "))

            except ValueError:
                print("enter only integer data")
                continue

            if (b2 < 50 or b2 > 30000):
                print("You have entered bid amount less than 50 or greater than 30000  ")
                continue

            else:
                break
        else:
            break

    if (ch1 == 'y' and ch2 == 'y'):
        if (m1 >= 0 and m2 >= 0):

            print("amount bid by", t1, "for", p, "is", b1)
            if (current_bid == 0):
                current_bid = current_bid + r + b1
            else:
                current_bid = current_bid + b1
            cb1 = current_bid
            m1 = total_amount[t1] - current_bid
            print("current bid for", p, "is", current_bid)
            print("money left for", t1, "is", m1)
            print("amount bid by", t2, "for", p, "is", b2)
            current_bid = current_bid + b2
            cb2 = current_bid
            m2 = total_amount[t2] - current_bid
            print("cuurent bid for", p, "is", current_bid)
            print("money left for", t2, "is", m2)

            auction(p, r, b1, b2, t1, t2, m1, m2, current_bid, cb1, cb2, t1_players, t2_players)

    elif (m1 < 0 and m2 < 0):
        print("Both teams have spent more than 30000 and are disqualified")
        print("Auction ends in a tie")
        sys.exit()

    elif m1 < 0:
        print(t1, " has spent more than 30000 and is disqualified")
        print(t2, "wins the auction")
        sys.exit()
    elif m2 < 0:
        print(t2, " has spent more than 30000 and is disqualified")
        print(t1, "wins the auction")
        sys.exit()





    elif (ch1 == 'y' and ch2 == 'n'):
        if (b2 == 0):
            current_bid = current_bid + r + b1
            print(" current bid amount is Rs ", current_bid)

            m1 = total_amount[t1] - current_bid

            if (m1 < 0):
                print(t1, "has spent more than 30000 and is disqualified")
                print(t2, "wins the auction")
                sys.exit()
            else:

                print(p, " sold to", t1, "at Rs ", current_bid)

                print("money left for ", t1, " is Rs ", m1)
                total_amount[t1] -= current_bid

                t1_players.append(p)
                print(t1_players)
                print("\n")
                print("------------------------------------------------------------------------")
                print("\n")


        else:
            current_bid = current_bid + b1
            print("current bid amount is Rs ", current_bid)

            m1 = total_amount[t1] - current_bid
            if (m1 < 0):
                print(t1, "has spent more than 30000 and is disqualified")
                print(t2, "wins the auction")
                sys.exit()
            else:
                print(p, "sold to", t1, "at Rs ", current_bid)
                total_amount[t1] -= current_bid

                print("money left for ", t1, " is Rs ", m1)

                m2 = m2 + cb2
                print("money left for ", t2, " is Rs ", m2)
                t1_players.append(p)
                print(t1_players)
                print("\n")
                print("------------------------------------------------------------------------")
                print("\n")



    elif (ch1 == 'n' and ch2 == 'n'):
        if (b1 == 0 and b2 == 0):
            print(p, " is unsold")
            print("\n")
            print("------------------------------------------------------------------------")
            print("\n")

        else:

            print("current bid amount is Rs ", current_bid)

            print(p, "sold to", t2, "at Rs ", current_bid)

            print("money left for ", t2, " is Rs ", m2)
            total_amount[t2] -= current_bid

            m1 = m1 + cb1
            print("money left for ", t1, " is Rs ", m1)
            t2_players.append(p)
            print(t2_players)
            print("\n")
            print("------------------------------------------------------------------------")
            print("\n")



    elif (ch1 == 'n' and ch2 == 'y'):

        if (b1 == 0 and b2 != 0):

            current_bid = current_bid + r + b2
            m2 = total_amount[t2] - current_bid
            if (m2 < 0):

                print(t2, " has spent more than 30000 and is disqualified")
                print(t1, " wins the auction")
                sys.exit()

            else:

                print(p, " sold to ", t2, "at Rs ", current_bid)
                total_amount[t2] -= current_bid

                print("money left for ", t2, "is Rs ", m2)
                t2_players.append(p)
                print(t2_players)
                print("\n")
                print("------------------------------------------------------------------------")
                print("\n")



        else:

            print("current bid amount is Rs ", current_bid)
            m2 = total_amount[t2] - current_bid
            if (m2 < 0):
                print(t2, " has spent more than 30000 and is disqualified")
                print(t1, " wins the auction")
                sys.exit()
            else:
                print(p, "sold to", t2, "at Rs ", current_bid)
                total_amount[t2] -= current_bid

                print("money left for ", t2, " is Rs ", m2)

                m1 = m1 + cb1
                print("money left for ", t1, " is Rs ", m1)
                t2_players.append(p)
                print(t2_players)
                print("\n")
                print("------------------------------------------------------------------------")
                print("\n")
    return m1, m2


if __name__ == '__main__':
    print("The rules of the auction are as follows:")
    print("Each player has 30000 rupees at the start of the auction and can buy any number of players")
    print("The categories of base price are: 500,250 and 100")
    print("Each time to bid on any player minimum of 50 rupees has to be spent")

    print("Each player will be assigned a rating(max 20) which will be used to calculate the winner of the auction")
    print("The ipl teams will not know the player rating before the ipl auction comes to an end")
    print("The average rating of players bought by each team will be considered to decide the winner of the auction")
    print(
        "Remember that each player will enter the auction only once and it is better to have more number of players in the squad")
    print("Enter y if you want to bid")
    print("Enter n if you dont want to buy")


    bid1 = 0
    bid2 = 0

    current_bid1 = 0
    current_bid2 = 0

    t1_players = []
    t2_players = []

    for i in batsman:
        player = i
        rate = batsman[i]

        m1 = total_amount[team1]
        m2 = total_amount[team2]
        print(m1)
        print("pai")
        current_bid = 0
        print(m2)

        print("the current auction pool is BATSMEN")
        print("The player is: ", player)
        print("The base price is: ", rate)
        m1, m2 = auction(player, rate, bid1, bid2, team1, team2, m1, m2, current_bid, current_bid1, current_bid2,
                         t1_players, t2_players)

    for j in bowlers:
        player = j
        rate = bowlers[j]

        m1 = total_amount[team1]
        m2 = total_amount[team2]
        print(m1)
        print("pai")
        current_bid = 0
        print(m2)

        print("the current auction pool is BOWLERS")
        print("The player is: ", player)
        print("The base price is: ", rate)
        m1, m2 = auction(player, rate, bid1, bid2, team1, team2, m1, m2, current_bid, current_bid1, current_bid2,
                         t1_players, t2_players)

    for k in all_rounders:
        player = k
        rate = all_rounders[k]

        m1 = total_amount[team1]
        m2 = total_amount[team2]
        print(m1)
        print("pai")
        current_bid = 0
        print(m2)

        print("the current auction pool is ALL-ROUNDERS")
        print("The player is: ", player)
        print("The base price is: ", rate)
        m1, m2 = auction(player, rate, bid1, bid2, team1, team2, m1, m2, current_bid, current_bid1, current_bid2,
                         t1_players, t2_players)

    for v in wkb:
        player = v
        rate = wkb[v]

        m1 = total_amount[team1]
        m2 = total_amount[team2]

        current_bid = 0

        print("the current auction pool is WKB")
        print("The player is: ", player)
        print("The base price is: ", rate)
        m1, m2 = auction(player, rate, bid1, bid2, team1, team2, m1, m2, current_bid, current_bid1, current_bid2,
                         t1_players, t2_players)

    rate1 = 0
    rate2 = 0
    print("PLayer list bought by  ", team1, " is :")
    print(t1_players)
    print("\n")
    print("-----------------------------------------------------")
    print("\n")
    print("Player list bought by  ", team2, " is : ")
    print(t2_players)
    print("\n")
    print("-----------------------------------------------------")
    print("\n")

    for z in t1_players:
        if z in batsman:
            rate1 += batsman_rate[z]
        elif z in bowlers:
            rate1 += bowlers_rate[z]
        elif z in all_rounders:
            rate1 += all_rounders_rate[z]
        else:
            rate1 += wkb_rate[z]

    for y in t2_players:
        if y in batsman:
            rate2 += batsman_rate[y]
        elif y in bowlers:
            rate2 += bowlers_rate[y]
        elif y in all_rounders:
            rate2 += all_rounders_rate[y]
        else:
            rate2 += wkb_rate[y]

    t1_total = len(t1_players)
    t2_total = len(t2_players)

    t1_avg = rate1 / t1_total

    t2_avg = rate2 / t2_total

    print("Total player rating of ", team1)
    print(t1_avg)
    print("Total player rating of ", team2)
    print(t2_avg)

    if t1_avg > t2_avg:

        print(team1, " WINS THE IPL AUCTION !!!")
    elif t1_avg < t2_avg:

        print(team2, " WINS THE IPL AUCTION !!!")
    else:

        print("IPL AUCTION ENDS IN A TIE")




