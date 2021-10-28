"""
Excuse my bad English, I'm french. Project started on October 24, 2021 by Arkya29.
More informations at github.com/Arkya29/DiscordFavoritesEmotesSaver.
Emotes with numbers in their name are not supported.
"""

finalStringsEnd = ']},"_version":1}'  # end of all final string

def builtinFavorites(value): # return string with favorites builtin emotes (originally on discord)
    value = value.replace(' ','') # deleting spaces
    value = value.replace(':', '"') # replacing ':' by '"'
    value = value.replace('""', '","') # replacing '""' by '","'
    return value

def moddedFavorites(value): # return string with favorites modded emotes (added on discord by somebody)
    value = value.replace('>', '","') # replacing '>' by '","'
    # Characters (with lower case and upper case) who can be in the name of an emote (numbers aren't supported) :
    a = "abcdefghijklmnopqrstuvwxyz <:_"
    a = a + a.upper()
    # Deleting the name of the emote :
    for letter in a:
        value = value.replace(letter,"")
    value = value[:-2] # deleting the two charaters '",' at the end
    return value

def finalCreated(): # return final created string, asked by the user
    # ("usageHistory" put "A,R,K,Y,A,2,9" emotes to the recent used emotes. Can be remplaced by at least 1 emote).
    beginning = '{"_state":{"usageHistory":{"a":{"totalUses":1,"recentUses":[9999999999999],"frecency":100,"score":100},"regional_indicator_r":{"totalUses":1,"recentUses":[9999999999999],"frecency":100,"score":100},"regional_indicator_k":{"totalUses":1,"recentUses":[9999999999999],"frecency":100,"score":100},"regional_indicator_y":{"totalUses":1,"recentUses":[9999999999999],"frecency":100,"score":100},"regional_indicator_a":{"totalUses":1,"recentUses":[9999999999999],"frecency":100,"score":100},"two":{"totalUses":1,"recentUses":[9999999999999],"frecency":100,"score":100},"nine":{"totalUses":1,"recentUses":[9999999999999],"frecency":100,"score":100}},"diversitySurrogate":"","favorites":['
    # if initialModdedEmotes and initialBuiltinEmotes aren't empty, separation ',"' will be put in the finalCreated string
    # if initialModdedEmotes isn't empty AND if initialModdedEmotes is empty, separation '"' will be put in the finalCreated string
    separation2 = "" # separation2 is empty by default
    if moddedFavorites(initialModdedEmotes) != "": # if initialModdedEmotes is not empty
        if builtinFavorites(initialBuiltinEmotes) != "": # if initialBuiltinEmotes is not empty
            separation2 = ',"'
        else : # if initialBuiltinEmotes is empty
            separation2 = '"'
    return beginning + builtinFavorites(initialBuiltinEmotes) + separation2 + moddedFavorites(initialModdedEmotes) + finalStringsEnd

def finalUpdated(): # return final updated string, asked by the user
    value = initialString.replace(finalStringsEnd,"") # deleting the end of the string
    # if isn't empty, change separation which will be put in the finalUpdated string (empty by default) :
    separation1 = ""
    separation2 = ""
    if builtinFavorites(initialBuiltinEmotes) != "":
        separation1 = ','
    if moddedFavorites(initialModdedEmotes) != "":
        separation2 = ',"'
    return value + separation1 + builtinFavorites(initialBuiltinEmotes) + separation2 + moddedFavorites(initialModdedEmotes) + finalStringsEnd

print("--> Please, read github.com/Arkya29/DiscordFavoritesEmotesSaver before using the program. Emotes with numbers in their name are not supported.")
choice = input("Type \"A\" to create a new list of emotes or \"B\" to add emote(s) in a existing list.")
if choice == "A" or choice == "a": # if user's choice is A
    print("------------------------------------------------")
    initialBuiltinEmotes = input("Paste all your builtin emotes (originally on discord) in one line (can be empty) :")
    initialModdedEmotes = input("Paste all your modded emotes (added on discord by somebody) in one line (can be empty) :")
    print("Paste the following line in \"CTRL + Shift + I > Application > Local Storage > https: //discord.com > EmojiStore\" key :\n")
    print(finalCreated())  # print final created string, asked by the user
elif choice == "B" or choice == "b": # if user's choice is B
    print("------------------------------------------------")
    print("Go to \"CTRL + Shift + I > Application > Local Storage > https: //discord.com\"")
    initialString = input("Paste the content of your actual \"EmojiStore\" key :")
    initialBuiltinEmotes = input("Paste your new builtin emote(s) (originally on discord) in one line (can be empty) :")
    initialModdedEmotes = input("Paste your new modded emote(s) (added on discord by somebody) in one line (can be empty) :")
    print("Paste the following line in \"CTRL + Shift + I > Application > Local Storage > https: //discord.com > EmojiStore\" key :\n")
    print(finalUpdated()) # print final updated string, asked by the user
else: # if user's choice isn't A, a, B or b
    print('Error : You need to press "A" or "B". Please, restart.')
input("\nPress \"Enter\" to close.")
