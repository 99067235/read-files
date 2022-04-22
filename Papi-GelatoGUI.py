import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import messagebox
import yaml
from yaml.loader import SafeLoader, BaseLoader, FullLoader
with open('C:/Users/Jurrian/Documents/read-files/settings.yml', 'r') as file:
    prijzen = yaml.safe_load(file)



lijstMetToppings = ["sr", "slagroom", "sp", "sprinkels", "cs", "caramelsaus"]
bakje = 0
hoorntje = 0
aantalBolletjes = 0
toppingKosten = 0.00
aantalToppings = 0
my_formatter = "{0:.2f}"
def bolletjesBesteld():
    global soortVerpakking, bakje, hoorntje
    if answerSpin1.get() <= 3 and answerSpin1.get() != 0:
        info1.set("Wilt u uw bestelling in een hoorntje of in een bakje?")
        spin1.grid_forget()
        radio1.grid()
        radio2.grid()
        radio1.configure(text="Hoorntje", value="H")
        radio2.configure(text="Bakje", value="B")
        startButton.wait_variable(radioAnswer)
        if radioAnswer.get() == "H":
            soortVerpakking = "H"
            hoorntje += 1
            litersOfBolletjesBesteld("bolletje")
        elif radioAnswer.get() == "B":
            soortVerpakking = "B"
            bakje += 1
            litersOfBolletjesBesteld("bolletje")
    elif answerSpin1.get() >3:
        soortVerpakking = "B"
        bakje += 1
        info1.set(f"Dan krijgt u {answerSpin1.get()} bolletjes in een bakje.")
        litersOfBolletjesBesteld("bolletje")

def checkSmaak():
    if radioAnswer.get() == "A":
        pass
    elif radioAnswer.get() == "C":
        pass
    elif radioAnswer.get() == "V":
        pass
    else:
        messagebox.showinfo("INFO", "Kies aub een optie")
        if soortPersoon == "P":
            litersOfBolletjesBesteld("bolletje")
        else:
            litersOfBolletjesBesteld("liter")

def bonZakelijk():
        total = my_formatter.format(answerSpin2.get()*prijzen['liter'])
        btwZakelijk = my_formatter.format(round(float(total)) / 100 * prijzen['btw'])
        bonLabel = tkinter.Label(window, text=f"""Bedankt en tot ziens!\n---------[Papi Gelato]---------
Liter:  {answerSpin2.get()} X €{prijzen['liter']} = € {total}
-------------------------------
Totaal: {total}
BTW ({prijzen['btw']}%): € {btwZakelijk}""")
        bonLabel.grid()

def topping():
    global toppingKosten, radio4, aantalToppings
    info1.set(value="Welke topping wilt u?")
    radio1.configure(text="Slagroom", value="SR")
    radio2.configure(text="Sprinkels", value="SP")
    radio3.configure(text="Caramelsaus", value="CS")
    radio4 = ttk.Radiobutton(window, text="G", variable=radioAnswer, value="G")
    radio4.grid()
    startButton.wait_variable(radioAnswer)
    if radioAnswer.get() == "SR":
        aantalToppings += 1
        toppingKosten += prijzen['toppings']['slagroom']
    elif radioAnswer.get() == "SP":
        aantalToppings += 1
        toppingKosten += (prijzen['toppings']['sprinkels']*int(aantalBolletjes))
    elif radioAnswer.get() == "CS":
        aantalToppings += 1
        if soortVerpakking == "B":
            toppingKosten += prijzen['toppings']['caramel']['bakje']
        elif soortVerpakking == "H":
            toppingKosten += prijzen['toppings']['caramel']['hoorentje']
    elif radioAnswer.get() == "G":
        pass

def bonParticulier():
    global bonLabel1, bonLabel2, bakjeLabel, hoorntjeLabel, toppingLabel,totalLabel
    total = my_formatter.format(aantalBolletjes*prijzen['bolletjes'] + (aantalToppings * toppingKosten) + (hoorntje * prijzen['hoorentjes']) + (bakje * 0.75))
    formattedToppings = my_formatter.format(aantalToppings * toppingKosten)

    prijsBolletjes = my_formatter.format(aantalBolletjes*prijzen['bolletjes'])
    bonLabel1 = tkinter.Label(window, text=f"Bedankt en tot ziens!\n---------[Papi Gelato]---------")
    bonLabel1.grid()
    if bakje > 0:
        bakjeLabel = tkinter.Label(window, text=f"Bakje: {bakje} X €{prijzen['bakjes']} = {bakje * prijzen['bakjes']}")
        bakjeLabel.grid()
    if hoorntje > 0:
        hoorntjeLabel = tkinter.Label(window, text=f"Hoorntje: {hoorntje} X €{prijzen['hoorentjes']} = {hoorntje * prijzen['hoorentjes']}")
        hoorntjeLabel.grid()
    bonLabel2 = tkinter.Label(window, text=f"""Bolletjes: {aantalBolletjes} X €{prijzen['bolletjes']} = € {prijsBolletjes}""")
    bonLabel2.grid()
    if aantalToppings > 0:
        toppingLabel = tkinter.Label(window, text=f"Topping: {aantalToppings} X {my_formatter.format(toppingKosten)} € {formattedToppings}") 
        toppingLabel.grid()
    totalLabel = tkinter.Label(window, text=f"""-------------------------------
    Totaal: {total}""")
    totalLabel.grid()
        
def destroy():
    window.destroy()


def litersOfBolletjesBesteld(soort):
    global aantalBolletjes, nogEenKeer, bestelButton
    if soortPersoon == "P":
        soortSpin = answerSpin1
    elif soortPersoon == "Z":
        soortSpin = answerSpin2
    aantalBolletjes += int(spin1.get())
    if answerSpin2.get() != 0 or answerSpin1.get() != 0:
        aantalLoops = 0
        for aantalLoops in range(soortSpin.get()):
            startButton.grid_forget()
            spin2.grid_forget()
            spin1.grid_forget()
            radioAnswer.set("")
            info1.set(f"Welke smaak wilt u voor {soort} {aantalLoops+1}?")
            if aantalLoops == 0:
                radio1.configure(text="Aardbei", value="A")
                radio2.configure(text="Chocolade", value="C")
                radio3.configure(text="Vanille", value="V")
                radio1.grid()
                radio2.grid()
                radio3.grid()
            startButton.wait_variable(radioAnswer)
            checkSmaak()
        spin2.grid_forget()
        startButton.grid_forget()
        if soortPersoon == "P":
            topping()
        try:
            radio1.grid_forget()
            radio2.grid_forget()
            radio3.grid_forget()
            radio4.grid_forget()
            infoLabel1.grid_forget()
        except:
            pass
        if soortPersoon == "Z":
            bonZakelijk()
        else:
            bonParticulier()
        if soortPersoon == "P":
            nogEenKeer = ttk.Button(window, text="opnieuw bestellen", command=windowAanmaken)
            nogEenKeer.grid()
        bestelButton = ttk.Button(window, text="Bestellen", command=destroy)
        bestelButton.grid()
def aantal():
    global soortPersoon
    radio1.grid_forget()
    radio2.grid_forget()
    if radioAnswer.get() == "P":
        soortPersoon = "P"
        info1.set("Hoeveel bolletjes wilt u bestellen?")
        spin1.grid()
        bolletjesBesteld()
    elif radioAnswer.get() == "Z":
        soortPersoon = "Z"
        info1.set("Hoeveel liter wilt u bestellen?")
        spin2.grid()
        litersOfBolletjesBesteld("liter")
    else:
        messagebox.showinfo("INFO", "Kies a.u.b. een optie.")

def ParOfZakCheck():
    global radio1, radio2, radio3
    info1.set("Bent u particulier of zakelijk?")
    radio1 = ttk.Radiobutton(window, text="Particulier", variable=radioAnswer, value="P")
    radio1.grid()
    radio2 = ttk.Radiobutton(window, text="Zakelijk", variable=radioAnswer, value="Z")
    radio2.grid()
    radio3 = ttk.Radiobutton(window, text="", variable=radioAnswer, value="")
    radio3.grid()
    radio3.grid_forget()
    startButton.config(text="Volgende",command=aantal)
    startButton.grid(column=0, row=4)

def windowAanmaken():
    global info1, radioAnswer, startButton, spin1, spin2, infoLabel1, answerSpin1, answerSpin2, window
    try:
        window.destroy()
    except:
        pass
    window = tk.Tk()
    info1 = tkinter.StringVar(value="Welkom bij Papi Gelato. Druk op de knop om uw epische bestelling te kiezen.")
    infoLabel1 = tkinter.Label(window, textvariable=info1)
    infoLabel1.grid()
    radioAnswer = tkinter.StringVar()
    startButton = ttk.Button(window, text="Start", command=ParOfZakCheck)
    startButton.grid()
    answerSpin1 = tkinter.IntVar()
    spin1 = ttk.Spinbox(window, from_=1, to=8, textvariable=answerSpin1)
    spin1.grid()
    spin1.grid_forget()
    answerSpin2 = tkinter.IntVar()
    spin2 = ttk.Spinbox(window, from_=1, to=float("inf"), textvariable=answerSpin2)
    spin2.grid_forget()
    window.mainloop()

windowAanmaken()
################################################################# NORMALE CODE #################################################################
# e = 0
# i = 0

# literprijs = 9.80
# prijsBolletjes = 0.95
# prijsHorrentjes = 1.25
# prijsBakje = 0.75
# hoorntje = 0
# bakje = 0
# totaalBolletjes = 0
# toppingKosten = 0.00
# aantalToppings = 0
# lijstMetToppings = ["sr", "slagroom", "sp", "sprinkels", "cs", "caramelsaus"]
# kostenBakje = 0
# kostenHoorntje = 0
# kostenToppings = 0
# kostenBolletjes = 0
# HoeveelLiter = 0
# smaak = ""
# antwoord3 = ""
# Btw = 6
# btwprijs = 0
# lijstmetBesteldeSmaken = []
# gekozenbakje = False
# a = True

# def sorry():
#     print("Sorry, zulke grote bakken hebben we niet")
    

# def snapNiet():
#     print("Sorry, dat is geen optie die we aanbieden...")



# def topping(bolletjes):
#     global aantalToppings
#     global toppingKosten
#     global antwoord3
#     toppingKeuze = input("Wat voor topping wilt u: G) Geen, SR) Slagroom, SP) Sprinkels of CS) Caramel Saus? ").lower()
#     if toppingKeuze == "g":
#         print("")
        
#     elif toppingKeuze in lijstMetToppings:
#         aantalToppings += 1

#         if toppingKeuze == "sr" or toppingKeuze == "slagroom":
#             toppingKosten += 0.50

#         elif toppingKeuze == "sp" or toppingKeuze == "sprinkels":
#             toppingKosten += (0.30 * bolletjes)

#         elif toppingKeuze == "cs" or toppingKeuze == "caramelsaus":
#             if antwoord3 == "B":
#                 toppingKosten += 0.90

#             elif antwoord3 == "A":
#                 toppingKosten += 0.60
#         else:
#             snapNiet()
#     else:
#         snapNiet()
#         topping(bolletjes)

# def bonParticulier():
#     global kostenBakje
#     global kostenToppings
#     global kostenHoorntje
#     global kostenBolletjes
#     global i
#     global e
#     my_formatter = "{0:.2f}"
#     print("Bedankt en tot ziens!")
#     print("---------[Papi Gelato]---------")
#     #formatteren kosten bolletjes
#     kostenBolletjes = float(totaalBolletjes * prijsBolletjes)
#     formatted_PrijsBolletjes = float(totaalBolletjes) * prijsBolletjes
#     bonPrijsBolletjes = my_formatter.format(formatted_PrijsBolletjes)
#     print("Bolletjes:   "  ,  totaalBolletjes, "X",  prijsBolletjes,  "= €",   bonPrijsBolletjes)
#     #formatteren kosten hoorntje
#     kostenHoorntje = hoorntje * prijsHorrentjes
#     BonprijsHoorntje = my_formatter.format(kostenHoorntje)
#     if hoorntje >= 1:
#         print("Horrentjes:  ",  hoorntje, "X",  prijsHorrentjes, "= €",   BonprijsHoorntje)
#     #formatteren kosten bakje
#     kostenBakje = bakje * prijsBakje
#     BonprijsBakje = my_formatter.format(kostenBakje)
#     if bakje >= 1:
#         print("Bakje:       "     ,  bakje, "X",  prijsBakje,      "= €",   BonprijsBakje)
#     #formatteren prijs toppings
#     BonPrijsToppings = my_formatter.format(toppingKosten)
#     if aantalToppings >= 1:
#         kostenToppings = float(aantalToppings) * toppingKosten
#         print("Topping:     "   ,  aantalToppings, "X", toppingKosten, "= €", BonPrijsToppings)
#     print("             ---------------- +")
#     formatted_total = kostenBolletjes + kostenHoorntje + kostenBakje + kostenToppings
#     total = my_formatter.format(formatted_total)
#     print("Totaal       = €",total)
#     exit()

# def bonZakelijk():
#     global HoeveelLiter
#     global i
#     my_formatter = "{0:.2f}"
#     prijs = HoeveelLiterkeuze * literprijs
#     #formatteren totaal
#     formatted_prijsZakelijk = my_formatter.format(prijs)
#     #formatteren btw
#     berekeningBtw = prijs / 106 * 6
#     print("Bedankt en tot ziens!")
#     print("---------[Papi Gelato]---------")
#     print("Liter:  ", HoeveelLiterkeuze, "X €",literprijs, " = €", formatted_prijsZakelijk)
#     print("             ---------------- +")
#     print("Totaal               = €", formatted_prijsZakelijk)
#     print("BTW (6%)             = €", my_formatter.format(berekeningBtw))
#     exit()

# def bakjeGekozen(bolletjes):
#     global bakje
#     bakje += 1
#     topping(bolletjes)
#     antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
#     if antwoord4 == "Y":
#         print("")
#         aantalbolletjes()
#     elif antwoord4 == "N":
#         bonParticulier()
#         exit()
#     else:
#         sorry()
#         bakjeGekozen(bolletjes)

# def hoorntjeMeerbestellen(bolletjes):
#     antwoord4 = input("Hier is uw hoorntje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
#     if antwoord4 == "Y":
#         print("")
#         aantalbolletjes()
#     elif antwoord4 == "N":
#         bonParticulier()
#     else:
#         snapNiet()
#         hoorntjeMeerbestellen(bolletjes)

# def keuzeVerpakking(bolletjes):
#     global hoorntje
#     global antwoord3
#     global bakje
#     antwoord3 = input("Wilt u deze "+ str(bolletjes) +" bolletje(s) in A) een hoorntje of B) een bakje? ").upper()
#     if antwoord3 == "A":
#         hoorntje += 1
#         topping(bolletjes)
#         hoorntjeMeerbestellen(bolletjes)
#     elif antwoord3 == "B":
#         bakjeGekozen(bolletjes)
#     else:
#         snapNiet()
#         keuzeVerpakking(bolletjes)

# def welkeSmaak(bolletjes):
#     roundsLoop = 1
#     while roundsLoop != bolletjes + 1:
#         print("Welke smaak wilt u voor bolletje nummer", str(roundsLoop), "A) Aardbei, C) Chocolade, of V) Vanille?")
#         smaak = input("Vul hier uw antwoord in: " ).upper()
#         if smaak == "A" or smaak == "C" or smaak == "M" or smaak == "V":
#             roundsLoop += 1
#         else:
#             snapNiet()
#     keuzeVerpakking(bolletjes)

# def bakjeMeerBestellen(bolletjes):
#     global antwoord3
#     global a
#     topping(bolletjes)
#     while a == True:
#         antwoord4 = input("Hier is uw bakje met "+ str(bolletjes) +" bolletje(s). Wilt u nog meer bestellen? (Y/N)").upper()
#         if antwoord4 == "Y":
#             a = False
#             print("")
#             aantalbolletjes()
#         elif antwoord4 == "N":
#             a = False
#             bonParticulier()
#             exit()
#         else:
#             snapNiet()
#             a = True

# def welkeSmaakGroot(bolletjes):
#     global bakje
#     global smaak
#     global antwoord3
#     roundsLoop = 1
#     while roundsLoop != bolletjes + 1:
#         print("Welke smaak wilt u voor bolletje nummer", str(roundsLoop), "A) Aardbei, C) Chocolade, of V) Vanille?")
#         smaak = input("Vul hier uw antwoord in: " ).upper()
#         if smaak == "A" or smaak == "C" or smaak == "M" or smaak == "V":
#             roundsLoop += 1
#         else:
#             snapNiet()
#     bakjeMeerBestellen(bolletjes)

# def aantalbolletjes():
#     global totaalBolletjes
#     global antwoord3
#     global bakje
#     global kostenBakje
#     try:
#         bolletjes = int(input("Hoeveel bolletjes wilt u? "))
#         if bolletjes <= 3 and bolletjes >= 0:
#             totaalBolletjes += bolletjes
#             welkeSmaak(bolletjes)
#         elif bolletjes > 3 and bolletjes <= 8:
#             totaalBolletjes += bolletjes
#             print("Dan krijgt u van mij een bakje met", bolletjes, "bolletjes")
#             bakje += 1
#             antwoord3 = "B"
#             welkeSmaakGroot(bolletjes)
#         elif bolletjes <= 0:
#             print("Helaas verkopen wij geen hoorntjes of bakjes met minder dan 1 bolletje.")
#             bolletjes = 0
#         elif bolletjes > 8:
#             sorry()
#             aantalbolletjes()
#             bolletjes = 0
#         else:
#             snapNiet()
#             bolletjes = 0
#     except ValueError:
#         snapNiet()
#         aantalbolletjes()


# def litersIjs():
#     global HoeveelLiterkeuze
#     roundsLoop = 1
#     HoeveelLiterkeuze = int(input("Hoeveel liter ijs wilt u bestellen? "))
#     if HoeveelLiterkeuze >= 1:
#         while roundsLoop != HoeveelLiterkeuze + 1:
#             print("Welke smaak wilt u voor liter", str(roundsLoop), "A) Aardbei, C) Chocolade, of V) Vanille?")
#             welkeSmaak = input("Vul hier uw antwoord in: ").upper()
#             if welkeSmaak == "A" or welkeSmaak == "C" or welkeSmaak == "M" or welkeSmaak == "V":
#                 roundsLoop += 1
#             else:
#                 snapNiet()
#         bonZakelijk()
#     elif HoeveelLiterkeuze <= 0:
#         print("Helaas verkopen wij geen lege bakken ijs...")
#     else:
#         snapNiet()
    
# def welkom():
#     global i
#     global antwoord3
#     print("Welkom bij Papi Gelato")
#     while i == 0:
#         particulierOfZakelijk = input("Bent u p) particulier of z) zakelijk? ").lower()
#         if particulierOfZakelijk == "p" or particulierOfZakelijk == "particulier":
#             aantalbolletjes()
#         elif particulierOfZakelijk == "z" or particulierOfZakelijk == "zakelijk":
#             litersIjs()
#         else:
#             snapNiet()

# welkom()