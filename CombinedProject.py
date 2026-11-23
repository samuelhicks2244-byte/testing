## for workload management habits i made the functions required for each task in separate files and then combined them

# read all communications from messages.txt. There will be between zero and n lines in the file, each communication is on a separate line and you should process every messages in the file.

def OpenAndStoreMessages(filename):
    file = open(filename, "r")
    messages = []
    for line in file:
        line = line.strip()
        if line != "":
            TwoParts = line.split("|", 1)
            msg_id = TwoParts[0]
            string = TwoParts[1]
            row = []
            row.append(msg_id)
            row.append(string)
            messages.append(row)
            print(messages)
    file.close()
    return messages

# this is the functions for task 2

### to do

# it does say in the spec to put all task 2 functions together in 1 but to make avdanced task 3 easier dont do that (isolate the individual encoding functions)
# transition between task 1 and 2 by taking the messages taken from the file and putting them into the task 2 functions
# have a look at the threat score calc as task 5 and 6 require more data than what is currently being fetched
# work on the advanced tasks functions
    # most common word (this includes all words not just the keywords)
    # return the message ids alongside the keywords that are in the messages (acts as a network)
    # allow the user to enter a string and then allow them to choose an encoding method to use on there string (no file management is required in this task)
    # optimise code quality

# Rule 1: if a message starts and ends with the character x, remove both characters
def OuterCharactersRemovalX(string):
    if len(string) >= 2 and string[0] == "x" and string[-1] == "x":
        cleanString = string[1:-1]
    else:
        cleanString = string
    return cleanString

# Rule 2: if a message contains any space, each word is reversed individually
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

# Rule 3: remove random # noise characters
def HashtagCharactersRemoval(string):
    if "#" in string:
        cleanString = string.replace("#", "")
    else:
        cleanString = string
    return cleanString

# Rule 4: messages beginning with ! discard every other character
def EveryOtherCharacterRemoval(string):
    if len(string) > 0 and string[0] == "!":
        cleanString = string[1::2]
    else:
        cleanString = string
    return cleanString

def DecodeMessage(encodedMessage):
    if encodedMessage == "":
        decodedMessage = encodedMessage
    elif encodedMessage[0] == "!":
        decodedMessage = EveryOtherCharacterRemoval(encodedMessage)
    elif len(encodedMessage) >= 2 and encodedMessage[0] == "x" and encodedMessage[-1] == "x":
        decodedMessage = OuterCharactersRemovalX(encodedMessage)
    elif " " in encodedMessage:
        decodedMessage = ReverseWordsIfContainSpaces(encodedMessage)
    elif "#" in encodedMessage:
        decodedMessage = HashtagCharactersRemoval(encodedMessage)
    else:
        decodedMessage = encodedMessage
    return decodedMessage
