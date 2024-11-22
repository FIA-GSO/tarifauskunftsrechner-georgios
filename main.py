preis_erwachsene = 5.0
preis_kinder = 2.5
preis_premium = 3.0
preis_basis = 4.0
preis_ohne_museumclub_mitglied = 5.0
preis_zwischen_14_und_17 = 3.5
print ("Deutsch / English")
sprache = input()
if sprache == "Deutsch":   
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())
    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
    elif 14 <= alter_gast < 18:
        print(" ### Eintritt Zwischen 14 und 17 Jahren ### ")
        print(" Preis: ", preis_zwischen_14_und_17, " Euro ")
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input()
        if antwort_rabatt == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            print(" Preis: ", preis_premium, " Euro ")
            print("Ein Wein Glass für 0,75€ mitbestellen? (Ja/Nein)")
            antwort_wein = input()
            if antwort_wein == "Ja":
                preis_premium += 0.75
                print("Der Preis hat sich zu ", preis_premium, " Euro geändert")
            else: print("Der Preis hat sich nicht geändert")
        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(" Preis: ", preis_basis, " Euro ")
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            print(" Preis: ", preis_erwachsene, " Euro ")
    print(" ### Möchten sie erneut bestellen (ja/Nein)###")
    erneut_bestellen = input()
    
    if erneut_bestellen == "Ja":
        print("### Starten sie das Program erneut ###")
        print("Viel Spaß!")
    else:
        print("Viel Spaß!")
elif sprache == "English": 
    print("### Fare Information Calculator Museum XXX ###")
    print("Hello, please enter your age.")
    alter_gast = int(input())
    if alter_gast < 14:
        print("### Child Admission ###")
        print("Price: ", preis_kinder, " Euro")
    elif 14 <= alter_gast < 18:
        print("### Admission for Ages 14 to 17 ###")
        print("Price: ", preis_zwischen_14_und_17, " Euro")
    else:
        print("Are you a member of the Duisburg Museum Club? (Proof required)")
        print("If you are a Premium member, type 'p'.")
        print("If you are a Basic member, type 'b'.")
        print("If you are not a member, press any other key.")
        antwort_rabatt = input()
        if antwort_rabatt == "p":
            print("### Premium Member Admission ###")
            print("Price: ", preis_premium, " Euro")
            print("Would you like to add a glass of wine for 0.75€? (Yes/No)")
            antwort_wein = input()
            if antwort_wein == "Yes":
                preis_premium += 0.75
                print("The price has been updated to ", preis_premium, " Euro")
            else:
                print("The price remains unchanged")
        elif antwort_rabatt == "b":
            print("### Basic Member Admission ###")
            print("Price: ", preis_basis, " Euro")
        else:
            print("### Adult Admission (Full Price) ###")
            print("Price: ", preis_erwachsene, " Euro")
    print("### Would you like to order again? (Yes/No) ###")
    erneut_bestellen = input()
    if erneut_bestellen == "Yes":
        print("### Please restart the program ###")
        print("Enjoy your visit!")
    else:
        print("Enjoy your visit!")
