#this is a simple multiplayer ipl auction game


if __name__ == '__main__':
    print("The rules of the auction are as follows:")
    print("Each player has 25500 rupees at the start of the auction and are required to buy maximum 33 players")
    print("The categories of base price are: 500,250 and 100")
    print("Each time to bid on any player minimum of 50 rupees has to be spent")
    print("Each player will be assigned a rating(max 20) which will be used to calculate the winner of the auction")
    print("The ipl teams will not know the player rating before the ipl auction comes to an end")
    print("The average rating of players bought by each team will be considered to decide the winner of the auction")
    print("Remember that each player will enter the auction only once and it is better to have more number of players in the squad")
    print("Enter y if you want to bid")
    print("Enter n if you dont want to buy")

    batsman={"Steve Smith":250,"Kane Williamson":250,"S Lad":100,"A Finch":250,"S Dhawan":500,"Murali Vijay":100,"Virat Singh":100,"A Rahane":250,"Nitish Rana":250,"J Roy":100,"Rinku Singh":100,"Virat Kohli":500,"S Gill":100,"Suresh Raina":500,"Gurkeerat Singh":100,"Devdutt Padikkal":100,"Ambati Rayudu":250,"Faf Duplesis":250,"Kedar Jadhav":100,"Ruturaj Gaikwad":100,
        "E Morgan":250,"S Hetmyer":100,"M pandey":250,"David Miller":100,"Shashank Singh":100,"R Tripathi":100,"D Warner":500,"Shreyas Iyer":250,"Sarfraz Khan":100,"Manddep Singh":100,"P Shaw":100,"Priyam Garg":100,
            "Anmoolpreet Singh":100,"M Vohra":100,"Mayank Agarwal":100,"Rohit Sharma":500,"Karun Nair":100,"Chris Gayle":500,"Suryakumar Yadav":250,"Chris Lynn":250,"Saurabh Tiwary":100, }

    all_rounders={"M Nabi":100,"Ben Stokes":100,"Chris Green":100,"M Marsh":250,"Harshal Patel":100,"A Samad":100,"Axar Patel":100,"Vijay Shankar":100,"Shivam Dube":100,"Ravindra Jadeja":500,"Chris Woakes":250,"P Negi":100,"W Sundar":100,"C Morris":250,"Shane Watson":250,"Karn Sharma":100,"I Udana":100,"Dwayne Bravo":250,"Sam Curran":100,"Mitchell Santner":100,
                 "K Gowtham":100,"J Suchith":100,"Sanjay Yadav":100,"Fabian Allen":100,"James Neesham":100,"Deepak Hooda":100,"M Ali":250,"Pavan Deshpande":100,"Abhishek Sharma":100,"Andre Russell":500,"B Sandeep":100,"Keemo Paul":100,"K Nagarkoti":100,"Lalit Yadav":100,
            "Harpreet Brar":100,"D Nalkande" :100,"Glenn Maxwell" :250,"Chris Jordan":100,"Anukul Roy":100,"Tajinder Singh":100,"Jayant Yadav":100,"Krunal Pandya":100,"Hardik Pandya":250,"K Pollard":250,"Sherfane Rutherford":100,"PBR Singh":100,
               "Riyan Parag":100,"M Lomror":100,"Shreyas Gopal":100,"Yashasvi Jaiswal":100,"A Joshi":100,"Rahul Tewatia":100 }

    wkb={"KL Rahul":500,"Jos Buttler":250,"Robin Utthappa":250," DeKock":250,"W Saha":100,"P patel":100,"MS Dhoni":500,"AB Devillers":500,"N Jagadeeshan":"100","Rishabh Pant":250,"J Phillipe":100,"Dinesh Kathik":250,"Nikhil Naik":100,
         "Tom Banton":100,"A Tare":100,"Sanju Samson":100,"Anuj Rawat":100,"Ishan Kishan":100,"Jonny Bairstow":250,"Alex Carey":100,"S Goswami":100,"Nicholas Pooran":250,"Prabhsimran Singh":100,
         }

    bowlers={"Jofra Archer":250,"Amit Mishra":250,"Mohammed Shami":250,"Mohit Sharma":100,"Sandeep Sharma":100,"Shabhaz Nadeem":100,"Harry Gurney":100,"Billy Stanlake":100,"R Ashwin":500,"K Rabada":500,"M Siddarth":100,"Avesh Khan":100,"Lungi Ngidi":100,"Y Chahal":500,"Monu Kumar":100,"Ishant Sharma":100,"Prasidh Krishna":100,"Shabhaz Ahmed":100,"Lockie Ferguson":250,"M Siraj":100,"U Yadav":250,"KM Asif":100,"Harbhajan Singh":250,"N Saini":250,"Shardul Thakur":100,"Deepak Chahar":250,"Imran Tahir":250,
            "T Natarajan":100,"Khaleel Ahmed":100,"Siddarth Kaul":100,"Varun Chakravarthi":100,"Bhuvneshwar Kumar":250,"B Thampi":100,"S Lamichhane":100, "Kane Richarson":100,"T Deshpande":100,"S Warrier":100,"Kuldeep Yadav":250,"Dale Steyn":500,"Pat Cummins":500,"Piyush Chawla":250,"Josh Hazelwood":200,"S Mavi":100,"R Sai Kishore":100,
             "Rahul Chahar":100,"Andrew Tye":100,"M Mccleneghan":100,"Jasprit Bumrah":500,"Ankit Rajpoot":100,"Lasith Malinga":500,"Dhawal Kulkarni":100,"Trent Boult":200,
             "N Coulternile":100,"Moisin Khan":100,"Tom Curran":100,"D Deshmukh":100,"Sheldon Cottrel":100,"Mayank Markande":100,"Arshdeep Singh":100,"Ishan Porel":100,"Ravi Bishnoi":100,"Hardus Viljoen":100,
             "Mujeeb Rahman":100,"M Ashwin":100,"Varun Aaron":100,"Jaydev Unadkat":100,"Oshane Thomas":100,"Karthik Tyagi":100,"Akash Singh":100}




    batsman_rate = {"Steve Smith":17.5, "Kane Williamson":18, "S Lad":7, "A Finch":15.5, "S Dhawan": 15,
               "Murali Vijay": 12.5, "Virat Singh": 7, "A Rahane":14, "Nitish Rana": 16.5, "J Roy":11,
               "Rinku Singh": 6, "Virat Kohli": 20, "S Gill": 15, "Suresh Raina":17.5, "Gurkeerat Singh": 11,
               "Devdutt Padikkal": 10, "Ambati Rayudu": 16, "Faf Duplesis": 17, "Kedar Jadhav": 11.5,
               "Ruturaj Gaikwad": 9,
               "E Morgan": 14, "S Hetmyer": 14.5, "M pandey": 17, "David Miller":13.5, "Shashank Singh": 5,
               "R Tripathi": 11, "D Warner": 20, "Shreyas Iyer": 17, "Sarfraz Khan": 10, "Mandeep Singh": 13.5,
               "P Shaw": 14.5, "Priyam Garg": 7,
               "Anmoolpreet Singh": 9, "M Vohra": 10, "Mayank Agarwal": 13.5, "Rohit Sharma": 19, "Karun Nair": 12.5,
               "Chris Gayle": 18.5, "Suryakumar Yadav":16.5, "Chris Lynn": 16, "Saurabh Tiwary": 11, }

    all_rounders_rate = {"M Nabi": 17, "Ben Stokes": 19.5, "Chris Green": 9, "M Marsh": 12.5, "Harshal Patel": 11,
                    "A Samad": 5, "Axar Patel":12.5, "Vijay Shankar": 13.5, "Shivam Dube": 14.5, "Ravindra Jadeja": 19.5,
                    "Chris Woakes": 13, "P Negi": 12, "W Sundar": 12.5, "C Morris":17, "Shane Watson": 18,
                    "Karn Sharma": 12, "I Udana": 10, "Dwayne Bravo":19.5, "Sam Curran": 16, "Mitchell Santner": 12,
                    "K Gowtham": 15, "J Suchith": 10, "Sanjay Yadav": 4, "Fabian Allen": 10, "James Neesham": 15,
                    "Deepak Hooda": 13, "M Ali": 17.5, "Pavan Deshpande": 7, "Abhishek Sharma": 11,
                    "Andre Russell": 20, "B Sandeep": 4, "Keemo Paul": 13.5, "K Nagarkoti": 11, "Lalit Yadav": 7,
                    "Harpreet Brar": 5, "D Nalkande": 5, "Glenn Maxwell":18, "Chris Jordan": 17,
                    "Anukul Roy": 13, "Tajinder Singh": 7, "Jayant Yadav": 10, "Krunal Pandya": 16,
                    "Hardik Pandya": 19, "K Pollard": 19.5, "Sherfane Rutherford":13, "PBR Singh": 5,
                    "Riyan Parag": 15, "M Lomror": 11, "Shreyas Gopal": 15, "Yashasvi Jaiswal": 14, "A Joshi": 9,
                    "Rahul Tewatia": 12}

    wkb_rate = {"KL Rahul": 20, "Jos Buttler": 20, "Robin Utthappa": 14, " DeKock": 19.5, "W Saha": 13, "P patel": 13.5,
           "MS Dhoni": 20, "AB Devillers":20, "N Jagadeeshan":12, "Rishabh Pant": 18, "J Phillipe": 14,
           "Dinesh Kathik": 18.5, "Nikhil Naik": 8,
           "Tom Banton": 15, "A Tare": 11, "Sanju Samson": 17, "Anuj Rawat": 8, "Ishan Kishan": 17.5,
           "Jonny Bairstow": 19, "Alex Carey": 17, "S Goswami": 10, "Nicholas Pooran": 19, "Prabhsimran Singh": 10,
           }

    bowlers_rate = {"Jofra Archer": 20, "Amit Mishra": 16, "Mohammed Shami": 19, "Mohit Sharma": 14,
               "Sandeep Sharma": 15, "Shabhaz Nadeem": 12, "Harry Gurney": 11, "Billy Stanlake": 13,
               "R Ashwin": 18, "K Rabada": 20, "M Siddarth": 7, "Avesh Khan": 11, "Lungi Ngidi": 14,
               "Y Chahal": 20, "Monu Kumar": 6, "Ishant Sharma": 14, "Prasidh Krishna": 16, "Shabhaz Ahmed":10,
               "Lockie Ferguson": 14, "M Siraj": 11, "U Yadav": 15, "KM Asif": 9, "Harbhajan Singh": 17.5,
               "N Saini": 18.5, "Shardul Thakur": 15, "Deepak Chahar": 19, "Imran Tahir": 19.5,
               "T Natarajan": 11, "Khaleel Ahmed": 13, "Siddarth Kaul": 15, "Varun Chakravarthi": 10,
               "Bhuvneshwar Kumar": 18.5, "B Thampi": 10, "S Lamichhane": 17, "Kane Richarson": 14,
               "T Deshpande": 8, "S Warrier": 11, "Kuldeep Yadav": 18.5, "Dale Steyn":16.5, "Pat Cummins": 19,
               "Piyush Chawla": 19, "Josh Hazelwood": 15, "S Mavi": 12, "R Sai Kishore": 10,
               "Rahul Chahar": 16.5, "Andrew Tye": 15, "M Mccleneghan": 15.5, "Jasprit Bumrah": 20,
               "Ankit Rajpoot": 17.5, "Lasith Malinga": 18, "Dhawal Kulkarni": 17, "Trent Boult": 18.5,
               "N Coulternile": 18, "Moisin Khan": 9, "Tom Curran": 15, "D Deshmukh": 8, "Sheldon Cottrel": 17,
               "Mayank Markande": 16, "Arshdeep Singh": 10, "Ishan Porel": 14, "Ravi Bishnoi": 17.5,
               "Hardus Viljoen": 11,
               "Mujeeb Rahman": 18, "M Ashwin": 15, "Varun Aaron": 14, "Jaydev Unadkat": 16, "Oshane Thomas": 15,
               "Karthik Tyagi": 11, "Akash Singh": 10}

    print("The ipl auction begins")
    t1=input("enter 1st user's ipl team name")
    money1=25500
    t2=input("enter 2nd user's ipl team name")
    money2=25500
    bid1=0
    bid2=0

    print("The first set of players is batsman")
    batting();


class Auction:
    def __init__(self,player,base_price):
        self.player=player
        self.base_price=base_price
        self.unsold = []
    def bidding_t1(self):


        if bid1 == 0 and bid2 == 0:
            print("Does", t1, "wants to bid?")

            while True:
                try:
                    ch1 = input("enter the valid choice(y,n)")
                except  ValueError:
                    print("you have entered a wrong choice")
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
                        bid1 = int(input("enter the bid amount(minimum 50"))
                    except ValueError:
                        print("enter only integer data")
                        continue

                    if (bid1 < 50):
                        print("You have entered bid amount less than 50")
                        continue

                    else:
                        break
            if ch1 == 'n':
                bidding_t2();
            else:





    def bidding_t2(self):
        if(bid1 == 0 and bid2 == 0):
                print("Does", t2, "wants to bid?")

            while True:
                    try:
                        ch2 = input("enter the valid choice(y,n)")
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
                                bid2 = int(input("enter the bid amount(minimum 50"))
                            except ValueError:
                                print("enter only integer data")
                                continue

                            if (bid1 < 50):
                                print("You have entered bid amount less than 50")
                                continue

                            else:
                                break
            if(ch2 == 'n'):
                print(player,"is unsold")
                unsold.append(player)




for i in batsman:
    obj1=Auction(i,batsman[i])

for i in bowlers:
    obj2=Auction(i,bowlers[i])
for i in wkb:
    obj3=Auction(i,wkb[i])

for i in all_rounders:
    obj4=Auction(i,all_rounders[i])





