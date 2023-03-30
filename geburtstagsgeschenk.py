print("Hallo Michael, herzlich willkommen zu deinem kleinen Geburtstagsspiel")
alter = input("Wie alt wirst du heute?")
print("Ah,", alter, "das wusste ich natürlich😅. Ich wünsche dir alles Gute.🥳")
begin = input("Hast du Lust auf eine kleine Motorradtour?(j/n)")
if begin == "j":
    print("Okay dann lass uns starten!😉")
    print("Stelle dir vor du fährst mit deiner Honda durch Rumänien. Hohe Berge, ein leichter Windzug, strahlende Sonne.\nDas perfekte Wetter zum Motorrad fahren.")
    adventure1 = input("Doch plötzlich wird der Himmel grau und es beginnt zu regnen.💦 Was tust du?\n "
                       "Weiterfahren um in dem nahegelegen Haus Unterschlupf zu suchen(a) oder anhalten und dich im Wald unterstellen(b) ")
    if adventure1 == "a":
        print("Du fährst weiter und klingelst an dem Haus. Du wirst sehr gastfreundlich empfangen.")
        print("Als der Regen vorbei ist fährst du weiter. Nach einer Weile begegnet dir plötzlich ein Bär.🐻 Was tust du nun?")
        adventure2 = input("Schnell wegfahren(a) oder du schreist laut und wedelst wild mit den Armen(b)")
        if adventure2 == "a":
            print("Du fährst zu schnell, fällst dabei hin und verletzt dich. Du hast verloren")
        if adventure2 == "b":
            print("Der Bär ist verängstigt von deinen lauten Schreien und haut ab. Du kannst nun weiterfahren.")
            adventure3 = input("Doch plötzlich fährst du über einen Nagel und dein Reifen bekommt ein Loch. Was tust du? \n "
                               "Weiterfahren/schieben und auf eine Werkstatt hoffen.(a) oder den Reifen mit Panzertape flicken(b)")
            if adventure3 == "a":
                print("Du hast Glück, denn in der Nähe befindet sich eine Werkstatt die den Reifen flickt.")
                adventure4 = input("Doch schon kommt das nächste Problem auf, denn dein Zutrinken wird alle und du hast starken Durst \n"
                                   "Was tust du? Das Wasser aus der nahegelegenen Quelle trinken(a) oder denen vorbeifahrenden Autofahrer anhalten und um etwas Zutrinken bitten(b).")
                if adventure4 == "a":
                    print("Leider war die Quelle doch nicht so sauber wie du dachtest und fanden sich einige Schmutzpartikel darin. Du hast verloren.")
                if adventure4 == "b":
                    print("Der Autofahrer gibt dir freundlicherweise eine Flasche Wasser und du kannst deinen Durst stillen. \n"
                          "Der restliche Tag verläuft reibungslos und du kommst am Abend müde, aber zufrieden in deine Unterkunft. Herlichen Glückwunsch!")
            if adventure3 == "b":
                print("Leider hält deine Konstruktion nicht und der Reifen verliert schleichend an Luft. Du hast verloren.")
    if adventure1 == "b":
        print("Deine Entscheidung entpuppte sich als nicht so schlau, denn das Gewitter verstärkte sich und auch Blitze kamen vom Himmel. \n Du hast verloren.")
if begin == "n":
    print("Schade, dann ist das Programm jetzt beendet😭")