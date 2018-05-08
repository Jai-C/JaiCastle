## Converts dates from the French revolution format
## Author Jai Castle et al.

import calendar
import random
startOfNewCalendar = 654781

def enterInput():
    sentence = 0
    print("\n"+"Please enter a date on the French Revolution calendar between 14/1/2 and 11/4/14")
    while (sentence != 1):
        Date = str(input("Please enter your date (dd mm yy): "))
        Data = Date.split('/')
        
        year = int(Data[2])
        month = int(Data[1]) 
        day = int(Data[0])

        if (month > 12):
            sentence = 0
        else:
            if (day > 30):
                sentence = 0
            else:
                if ((year) > 2) and (year < 14):
                    sentence = 1

                elif (year == 2):
                    if (month > 1):
                        sentence = 1
                    elif (month == 1):
                        if (day >= 14):
                            sentence = 1
                        else:
                            sentence = 0
                    else:
                        sentence = 0
                        
                elif (year == 14):
                    if (month < 4):
                        sentence = 1
                    elif (month == 4):
                        if (day <= 11):
                            sentence = 1
                        else:
                            sentence = 0
                    else:
                        sentence = 0            
                else:
                    sentence = 0
        if sentence == 0:
            print("Invalid input. Please enter a date on the French Revolution calendar between \n14/1/2 and 11/4/14.")
        
    
    return day, month, year

def romanNumerals(number):
    result = ''
    nextAddition = ''
    tens = number // 10
    result = result + 'X' * tens
    number  = number - tens*10
    if number == 9:
        result = 'IX'
        number = 0
        if number >= 5:
            result = result + 'V'
            number = number - 5

        if number == 4:
            result = result+ 'IV'
        else:
            result = result + 'I'*number

    
    return result

def calcFrenchDays(days,months,years):
    daysForYears = 0
    offset = 0
    years = years - 1
    
    if years >= 11:
            daysForYears = 4018
            offset = 11
    elif years >= 3:
            daysForYears = 1096
            offset = 3
    elif years > 7:
            daysForYears = 2557
            offset = 7
    
    total = days + (months-1) * 30 + daysForYears + (years-offset) * 365
    return total - 1



def yearsPassed(days):
    days = days
    years = 0
    total = 0
    last_year_Leap = False
    while total < days:
            if calendar.isleap(years) is True:
                    daysInYear  = 366
                    last_year_Leap = True
            else:
                    daysInYear = 365
                    last_year_Leap = False
            total = total + daysInYear
            if total <= days:
                    years = years + 1
    Complete_years_days = total - daysInYear #Total number of days, which were in COMPLETED years
    monthDay = days - Complete_years_days

    if last_year_Leap == False:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
    else:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]


    for i in range(len(months)+1):
        if monthDay > 0:
            monthDay = monthDay - months[i]
        else:
            break
            

    monthDay = monthDay + months[i-1]
    monthNumber = i
    if monthNumber is 12 and monthDay is 31:
        years = years - 1
    
    return monthDay , monthNumber , years 

def displayGregorian(data):
    day = int(data[0]); month = int(data[1]); year = int(data[2])

    if day in [2,22]:
        suffix = 'nd'
    elif day in [1,21,31]:
        suffix = 'st'
    elif day in [3,23]:
        suffix = 'rd'
    else:
        suffix = 'th'

    day = str(day)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = months[month-1]

    print("\n", day + suffix,  month, year, "\n")

def displayFrench(data):
    day = int(data[0]); month = int(data[1]); year = int(data[2])

    day = str(day)
    months = ['Vendemiare an', 'Brumaire an' , 'Frimaire an', 'Nivose an' , 'Pluviose an' , 'Ventose an' , 'Germinal an', 'Floreal an', 'Prairial an', 'Messidor an' , 'Thermidor an', 'Fructidor an']
    month = months[month-1]
    year = romanNumerals(year)
    print("\n" , day,  month, year)

quotesFrench = [
"À chaque oiseau son nid est beau.",
"À goupil endormi rien ne tombe en la gueule.",
"À mauvais ouvrier point de bon outil.",
"Celui qui n'est pas avec moi est contre moi.",
"Celui qui est lent à manger est lent à travailler.",
"C'est en forgeant qu'on devient forgeron.",
"Coucher de poule et lever de corbeau écartent l'homme du tombeau.",
"Il y a serpent caché sous des fleurs.",
"La parole est l'ombre du fait.",
"Les rats quittent le navire qui coule.",
"Les plaisanteries les plus courtes sont les meilleures.",
"Qui court deux lièvres à la fois, n'en prend aucun.",
"A vaincre sans péril, on triomphe sans gloire.",
"Chat échaudé craint l’eau froide.",
"Le temps est un grand maître, dit-on, le malheur est qu’il tue ses élèves.",
"Il faut casser le noyau pour avoir l’amande.",
"Qui craint de souffrir, il souffre déjà de ce qu’il craint.",
"Choisissez votre femme par l’oreille bien plus que par les yeux.",
"La vérité vaut bien qu’on passe quelques années sans la trouver.",
"La parfaite valeur est de faire sans témoin ce qu’on serait capable de faire devant tout le monde.",
"Il faut bonne mémoire après qu’on a menti.",
"Je crains l’homme de un seul livre.",
"Chacun voit midi à sa porte",
"Il n'y a pas de fumée sans feu",
"Tous pour un, un pour tous",
"Il vaut mieux faire que dire",
"Un malheur ne vient jamais seul",
"Il faut réfléchir avant d'agir",
"Rien ne sert de courir, il faut partir à point"
    ]

quotesEnglish = [
"The bird loves her own nest.",
"A closed mouth catches no flies.",
"A bad craftsman blames his tools.",
"He who is not with me is against me.",
"Quick at meat, quick at work.",
"Practice makes perfect.",
"Early to bed and early to rise makes a man healthy, wealthy, and wise.",
"Look before you leap, for snakes among sweet flowers do creep.",
"Deeds are fruits, words are but leaves.",
"Rats desert a sinking ship.",
"Brevity is the soul of wit.",
"You must not run after two hares at the same time.",
"To win without risk is a triumph without glory.",
"A scalded cat fears cold water.",
"We say that time is a great teacher. It’s too bad that it also kills all its students.",
"It is necessary to break the shell to have the almond.",
"He who fears suffering is already suffering that which he fears.",
"Choose a wife rather by your ear than your eye.",
"Truth is more valuable if it takes you a few years to find it.",
"True valour is to do in secrecy what you could just have easily done before others.",
"A liar should have a good memory.",
"Fear the man of one book.",
"Everyone sees noon at his own door",
"Where there's smoke there's fire",
"All for one, one for all",
"Doing is better than saying",
"Misfortune never arrives alone",
"One must reflect before acting",
"There's no sense in running; you just have to leave on time"
    ]

def quote():
    number = random.randint(0, len(quotesFrench)-1)
    print("French quote of the day:  ")
    print(quotesFrench[number])
    print("("+quotesEnglish[number]+")\n")

doAnother = True
while doAnother is True:
    Input = enterInput()
    days = Input[0]
    months = Input[1]
    years = Input[2]
    FrenchDays = calcFrenchDays(days, months, years)
    displayFrench(Input)
    displayGregorian(yearsPassed(int(FrenchDays) + startOfNewCalendar))
    quote()
    TorF = input("Do you want to enter another date? (Enter Y or N)    ")
    if TorF is 'T':
        doAnother = True
    else:
        doAnother = False
