# in the task spec it says to put all these rules into 1 function, il do this after creating the logic for them all

## if a message starts and ends with the character x, remove both characters

def OuterCharactersRemovalX(string):
    if len(string) >= 2 and string[0]:
        cleanString = string[1:-1]
    else:
        cleanString = string
    return cleanString

## If a message contains any space " ", then each word within the message must be reversed individually

def ReverseWordsIfContainSpaces(string):
    if " " in string:
        wordList = string.split(" ")
        reversedWordList = []
        for word in wordList:
            reversedWordList.append(word[::-1])
        cleanString = " ".join(reversedWordList)
    else:
        cleanString = string
    return cleanString

# bit clunky but works

## Some messages contain random # characters that should be removed

def HashtagCharactersRemoval(string):
    if "#" in string:
        cleanString = string.replace("#", "")
    else:
        cleanString = string
    return cleanString

## Messages beginning with ! use an alternative encoding method where every other character should be removed

def EveryOtherCharacterRemoval(string):
    if string[0] == "!":
        cleanString = string[1::2]                                                 # WE DID THIS IN LAB 6 :))))
    else:
        cleanString = string
    return cleanString