# pseudokod
# l?s in rad f?r rad
# kolla f?rsta bokstaven, avg?r vad den inneb?r
# s?tt in passande XML kod
# g? f?rbi f?rsta |
# stoppa in tecknen innanf?r ?ppnande XML-tag
# kolla om tecknet ?r | eller tomt
# om | slut taggen
# om tomt slut taggen och taggen ovanf?r
# Alternativ l?sning: stoppa allt i variabler tills dags att printa/returna
# stoppa in en counter f?r att avg?ra var </family> ska stoppas in i fall tele inte alltid finns med
# stopp in en counter f?r att avg?ra var </person> ska stoppas in ifall <family> inte alltid finns med

my_file = open("input.txt", "r")
my_file_2 = open("output.txt", "w")
# print my_file.read()

# word = "T|0768-101802|08-101802"
letter = " "

print "<people>"
my_file_2.write("<people>" + "\n")
for line in my_file:
    word = line
    if word[0] == "P":
        letter = " "
        print "     <person>"
        my_file_2.write("     <person>" + "\n")
        word_2 = word[2:]
        # print word_2
        numberOfSplChar= word_2.rfind("|")
        # print numberOfSplChar
        word_3 = word_2[(numberOfSplChar+1):]
        word_2 = word_2[:numberOfSplChar]
        # print word_2
        # print word_3
        print "         <firstname>%s</firstname>" % word_2
        person_print = "         <firstname>%s</firstname>" % word_2 + "\n"
        my_file_2.write(person_print)
        print "         <lastname>%s</lastname>".rstrip("\n") % word_3
        person_print = "         <lastname>%s</lastname>".rstrip("\n") % word_3 + "\n"
        my_file_2.write(person_print)
    elif word[0] == "T" and letter != "F":
        print "     <telephone>"
        my_file_2.write("         <telephone>" + "\n")
        word_2 = word[2:]
        # print word_2
        numberOfSplChar= word_2.rfind("|")
        # print numberOfSplChar
        word_3 = word_2[(numberOfSplChar+1):]
        word_2 = word_2[:numberOfSplChar]
        # print word_2
        # print word_3
        print("         <mobile>%s</mobile>" % word_2)
        telephone_print = "             <mobile>%s</mobile>" % word_2 + "\n"
        my_file_2.write(telephone_print)
        print("         <home>%s</home>" % word_3)
        telephone_print = "             <home>%s</home>" % word_3 + "\n"
        my_file_2.write(telephone_print)
        print "     </telephone>"
        my_file_2.write("         </telephone>" + "\n")
    elif word[0] == "A" and letter != "F":
        # print letter
        print "     <address>"
        my_file_2.write("         <address>" + "\n")
        word_2 = word[2:]
        countOfSplChar = word_2.count("|")
        numberOfSplChar = word_2.find("|")
        # print numberOfSplChar
        word_3 = word_2[(numberOfSplChar+1):]
        word_2 = word_2[:numberOfSplChar]
        # print word_2
        # print word_3
        numberOfSplChar = word_3.find("|")
        # print numberOfSplChar
        if countOfSplChar>1:
            word_4 = word_3[(numberOfSplChar+1):]
            word_3 = word_3[:numberOfSplChar]
        # print word_2
        # print word_3
        # print word_4
        print "        <street>%s</street>" % word_2
        address_print = "             <street>%s</street>" % word_2 + "\n"
        my_file_2.write(address_print)
        print "        <city>%s</city>" % word_3
        address_print = str("             <city>%s</city>" % word_3) + "\n"
        my_file_2.write(address_print)
        if countOfSplChar>1:
            print "        <postalcode>%s</postalcode>" % word_4
            address_print = "             <postalcode>%s</postalcode>" % word_4 + "\n"
            my_file_2.write(address_print)
        print "     </address>"
        my_file_2.write("         </address>" + "\n")
    elif word[0] == "F":
        letter = "F"
        print "     <family>"
        my_file_2.write("         <family>" + "\n")
        word_2 = word[2:]
        # print word_2
        numberOfSplChar= word_2.rfind("|")
        # print numberOfSplChar
        word_3 = word_2[(numberOfSplChar+1):]
        word_2 = word_2[:numberOfSplChar]
        # print word_2
        # print word_3
        print("         <name> %s </name>" % word_2)
        family_print = "             <name>%s</name>" % word_2 + "\n"
        my_file_2.write(family_print)
        print("                 <born> %s </born>" % word_3)
        family_print = "                <born>%s</born>" % word_3 + "\n"
        my_file_2.write(family_print)
    elif word[0] == "A" and letter == "F":
        # print letter
        print "                     <address>"
        my_file_2.write("                <address>" + "\n")
        word_2 = word[2:]
        countOfSplChar = word_2.count("|")
        numberOfSplChar = word_2.find("|")
        # print numberOfSplChar
        word_3 = word_2[(numberOfSplChar+1):]
        word_2 = word_2[:numberOfSplChar]
        # print word_2
        # print word_3
        numberOfSplChar = word_3.find("|")
        # print numberOfSplChar
        if countOfSplChar:
            word_4 = word_3[(numberOfSplChar+1):]
            word_3 = word_3[:numberOfSplChar]
        # print word_2
        # print word_3
        # print word_4
        print("                 <street>%s</street>" % word_2)
        address_print = "             <street>%s</street>" % word_2 + "\n"
        my_file_2.write(address_print)
        print("                 <city>%s</city>" % word_3)
        address_print = "             <street>%s</street>" % word_3 + "\n"
        my_file_2.write(address_print)
        if countOfSplChar:
            print("                 <postalcode>%s</postalcode>" % word_4)
            address_print = "             <street>%s</street>" % word_4 + "\n"
            my_file_2.write(address_print)
        print "             </address>"
    elif word[0] == "T" and letter == "F":
        print "             <telephone>"
        my_file_2.write("             <telephone>" + "\n")
        word_2 = word[2:]
        # print word_2
        numberOfSplChar= word_2.rfind("|")
        # print numberOfSplChar
        word_3 = word_2[(numberOfSplChar+1):]
        word_2 = word_2[:numberOfSplChar]
        # print word_2
        # print word_3
        print("                 <mobile> %s </mobile>" % word_2)
        telephone_print = "                 <mobile> %s </mobile>" % word_2 + "\n"
        my_file_2.write(telephone_print)
        print("                 <home> %s </home>" % word_3)
        telephone_print = "                 <home> %s </home>" % word_2 + "\n"
        my_file_2.write(telephone_print)
        print "             </telephone>"
        my_file_2.write("             </telephone>" + "\n")
my_file.close()
my_file_2.close()