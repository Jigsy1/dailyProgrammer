# mapTest.py by Jigsy (https://github.com/Jigsy1) released under the Unlicense.
#
# If you've ever done /map on a large IRC server, you'll understand what this does. If you don't, see: https://i.imgur.com/2FNaI4A.png
#
# As far as I can tell, this works correctly. (Keywords: As far as I can tell.)

# define

END_OF_MAP = "End of /MAP"

# Tree

servers = {
        # "child": "parent"[,] - , isn't required for the final entry obviously.
        "angelicarogner.localhost": "towaherschel.localhost",
        "titarussell.localhost": "angelicarogner.localhost",
        "estellebright.localhost": "titarussell.localhost",
        "rennebright.localhost": "estellebright.localhost",
        "scherazardharvey.localhost": "estellebright.localhost",
        "klaudiavonauslese.localhost": "scherazardharvey.localhost",
        "saravalestein.localhost": "towaherschel.localhost",
        "milliumorion.localhost": "saravalestein.localhost",
        "altinaorion.localhost": "milliumorion.localhost",
        "fieclaussell.localhost": "saravalestein.localhost",
        "laurasarseid.localhost": "saravalestein.localhost",
        "rosine.localhost": "towaherschel.localhost",
        "asaherschel.localhost": "towaherschel.localhost",
        "priscillareisearnor.localhost": "towaherschel.localhost",
        "clairerieveldt.localhost": "priscillareisearnor.localhost",
        "alfinreisearnor.localhost": "priscillareisearnor.localhost",
        "eliseschwarzer.localhost": "alfinreisearnor.localhost",
        "luciaschwarzer.localhost": "eliseschwarzer.localhost",
        "roseliamillstein.localhost": "towaherschel.localhost",
        "vitaclotilde.localhost": "roseliamillstein.localhost",
        "emmamillstein.localhost": "roseliamillstein.localhost",
        "celinemillstein.localhost": "emmamillstein.localhost",
        "jessicaschleiden.localhost": "towaherschel.localhost",
        "noelseeker.localhost": "towaherschel.localhost",
        "sonyabaelz.localhost": "noelseeker.localhost",
        "mireille.localhost": "sonyabaelz.localhost",
        "franseeker.localhost": "noelseeker.localhost",
        "fionacraig.localhost": "towaherschel.localhost",
        "irinareinford.localhost": "towaherschel.localhost",
        "alisareinford.localhost": "irinareinford.localhost",
        "josettecapua.localhost": "alisareinford.localhost",
        "ferrisflorald.localhost": "alisareinford.localhost",
        "margaritadresden.localhost": "ferrisflorald.localhost",
        "sharonkreuger.localhost": "irinareinford.localhost",
        "arianrhod.localhost": "sharonkreuger.localhost",
        "ennea.localhost": "arianrhod.localhost",
        "duvalie.localhost": "arianrhod.localhost",
        "ines.localhost": "arianrhod.localhost",
        "shirleyorlando.localhost": "sharonkreuger.localhost",
        "aurelialeguin.localhost": "towaherschel.localhost",
        "maryaltheim.localhost": "ines.localhost",
        "junacrawford.localhost": "aurelialeguin.localhost",
        "musseegret.localhost": "towaherschel.localhost",
        "tioplato.localhost": "towaherschel.localhost",
        "ilyaplatiere.localhost": "tioplato.localhost",
        "rixiamao.localhost": "ilyaplatiere.localhost",
        "sullyatraid.localhost": "rixiamao.localhost",
        "cecilneues.localhost": "tioplato.localhost",
        "lucyseiland.localhost": "cecilneues.localhost",
        "keabannings.localhost": "tioplato.localhost",
        "shizukumaclaine.localhost": "keabannings.localhost",
        "gracelynn.localhost": "tioplato.localhost",
        "eliemacdowell.localhost": "tioplato.localhost",
        "mariabellcrois.localhost": "eliemacdowell.localhost",
        # A few new (randomly placed?) entries!
        "ferridaalfayed.localhost": "fieclaussell.localhost",
        "risettetwinings.localhost": "ferridaalfayed.localhost",
        "agnesclaudel.localhost": "ferridaalfayed.localhost",
        "judithranster.localhost": "mariabellcrois.localhost",
        "lucreziaisselee.localhost": "risettetwinings.localhost",
        "marielleayme.localhost": "risettetwinings.localhost",
        "yumeayme.localhost": "marielleayme.localhost"
}

# Core

def countProgeny(name):
        """Counts and returns - if available - the number of progeny for an item."""
        progeny = 0
        for child, parent in servers.items():
                if name == parent:
                        progeny += 1
        return progeny

def makePrettyString(string, position):
        """Hopefully cleans up dead branches."""
        newString = string
        newString = list(newString)
        stringLoop = 0
        while stringLoop < len(position):
                tempNumber = int(position[stringLoop])
                if tempNumber != -1:
                        # This next line below can possibly be commented out. I'm not 100% sure.
                        if string[tempNumber] != " ":
                                if string[tempNumber] != "`":
                                        newString[tempNumber] = " "
                stringLoop += 1
        newString = "".join(newString)
        return newString

def recurseMap(recursion, progeny, parentName, position):
        loop = 0
        oldProgeny = progeny
        for child, parent in servers.items():
                if parentName == parent:
                        loop += 1
                        newProgeny = countProgeny(child)
                        string = "| " * recursion
                        if newProgeny > 0:
                                # This should probably be oldProgeny(?); but if it ain't fixed, don't broke it!
                                if loop != progeny:
                                        string = string + "|"
                                else:
                                        string = string + "`"
                        else:
                                if loop < oldProgeny:
                                        string = string + "|"
                                else:
                                        string = string + "`"
                        if string.rfind("`") != -1:
                                position = position + " " + str(string.rfind("`"))
                                # "Why didn't you just make a list to start with?"
                                #       Because it didn't return the string in the manner I needed it in order to get this to work correctly.
                        tempPosition = list(position.split(" "))
                        string = makePrettyString(string, tempPosition) + "-" + child
                        print(string)
                        if progeny > 0:
                                recurseMap((recursion + 1), newProgeny, child, position)

def showMaps(ourServer):
        """Print the entire map tree from a specified starting point."""
        print(ourServer)
        recurseMap(0, countProgeny(ourServer), ourServer, "-1")
        # DO NOT REMOVE THE "-1"!
        print(END_OF_MAP)

def main():
        localServer = "towaherschel.localhost"
        # A few other test cases:
        #
        # localServer = "noelseeker.localhost"
        # localServer = "saravalestein.localhost"
        showMaps(localServer)

if __name__  == "__main__":
        main()

# EOF
