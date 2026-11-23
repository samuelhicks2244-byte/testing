# in the task spec it says to put all these rules into 1 function, il do this after creating the logic for them all

## if a message starts and ends with the character x, remove both characters

def OuterCharactersRemovalX(string):
    if string[0] == "x" and string[(len(string))-1] == "x":
        cleanString = string.replace("x", "")
        print("The string was altered from", string, "to", cleanString)
    else:
        print("The string was not altered:", string)

# testing

print("")
OuterCharactersRemovalX("xTOPSECRETx")
OuterCharactersRemovalX("TOPSECRET")

## If a message contains any space " ", then each word within the message must be reversed individually

def ReverseWordsIfContainSpaces(string):
    if " " in string:
        wordList = string.split(" ")
        reversedWordList = []
        for word in wordList:
            reversedWordList.append(word[::-1])
        cleanString = " ".join(reversedWordList)
        print("The string was altered from", string, "to", cleanString)
    else:
        print("The string was not altered:", string)

# bit clunky but works

# testing

print("")
ReverseWordsIfContainSpaces("hello world")
ReverseWordsIfContainSpaces("helloworld")
ReverseWordsIfContainSpaces("olleh dlrow")
ReverseWordsIfContainSpaces("ollehdlrow")

## Some messages contain random # characters that should be removed

def HashtagCharactersRemoval(string):
    if "#" in string:
        cleanString = string.replace("#", "")
        print("The string was altered from", string, "to", cleanString)
    else:
        print("The string was not altered:", string)

# testing

print("")
HashtagCharactersRemoval("SE#CR#E#T")
HashtagCharactersRemoval("HEL###L#O")
HashtagCharactersRemoval("Y########O")

## Messages beginning with ! use an alternative encoding method where every other character should be removed

def EveryOtherCharacterRemoval(string):
    if string[0] == "!":
        cleanString = string[1::2]                                                 # WE DID THIS IN LAB 6 :))))
        print("The string was altered from", string, "to", cleanString)
    else:
        print("The string was not altered:", string)

# testing

print("")
EveryOtherCharacterRemoval("!AxBtCtDaEcFk")
EveryOtherCharacterRemoval("AxBtCtDaEcFk")
EveryOtherCharacterRemoval("!HdEdLdLdO")
EveryOtherCharacterRemoval("HdEdLdLdO")