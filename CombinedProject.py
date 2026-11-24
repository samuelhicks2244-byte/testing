# CS-002 Coursework - Intelligence message analysis system
# Samuel Hicks

MESSAGES_FILE = "messages.txt"
KEYWORDS_FILE = "keywords.txt"
REPORT_FILE = "report.txt"

# read all communications from messages.txt. There will be between zero and n lines in the file, each communication is on a separate line and you should process every messages in the file.

#task 1: read and store messages
def OpenAndStoreMessages(filename):
    file = open(filename, "r")
    messages = []
    for line in file:
        line = line.strip()
        if line != "":
            twoParts = line.split("|", 1)
            messageId = twoParts[0]
            string = twoParts[1]
            row = []
            row.append(messageId)
            row.append(string)
            messages.append(row)
    file.close()
    return messages

#rule 1: if the first and last character is x then remove both
def OuterCharactersRemovalX(string):
    if len(string) >= 2 and string[0] == "x" and string[-1] == "x":
        cleanString = string[1:-1]
    else:
        cleanString = string
    return cleanString

#rule 2: if there is a space anywhere then flip each word seperately
def ReverseWordsIfContainSpaces(string):
    wordList = string.split(" ")                  # removed if here so that i could use this function easily in the advanced tasks
    reversedWordList = []
    for word in wordList:
        reversedWordList.append(word[::-1])              #:)
    return " ".join(reversedWordList)


#rule 3: remove all #
def HashtagCharactersRemoval(string):
    if "#" in string:
        cleanString = string.replace("#", "")
    else:
        cleanString = string
    return cleanString

#rule 4: if the first character is ! every other character is removed
def EveryOtherCharacterRemoval(string):
    if len(string) > 0 and string[0] == "!":
        cleanString = string[1::2]
    else:
        cleanString = string
    return cleanString

# combine the rules in the right order, i redid the if statements to make the code easier to read
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

#task 4: calculate the threat for "decodedMessage"
def CalculatingAThreatScore(decodedMessage):
    upperMessage = decodedMessage.upper()
    score = 0

    if "SECRET" in upperMessage:
        score += 10
    if "MEET" in upperMessage:
        score += 5
    if "ATTACK" in upperMessage:
        score += 15

    for character in decodedMessage:
        if character.isdigit():
            score += 3
            break           #so that only ever adds 3 once
    return score

#task 3: keyword and message comparison
#read the keyword file
def ReadKeywords(filename):
    file = open(filename, "r")
    keywords = []
    for line in file:
        line = line.strip()
        if line != "":
            keywords.append(line.upper())
    file.close()
    return keywords

#compare the keywords with the file to see if they are in there
def FindKeywords(decodedMessage, keywords):
    upperMessage = decodedMessage.upper()
    keywordsFound = []
    for keyword in keywords:
        if keyword in upperMessage:
            keywordsFound.append(keyword)
    return keywordsFound

#task 5: write the report to report.txt
def WriteReport(lockedInMessages, keywords):
    file = open(REPORT_FILE, "w")

    file.write("INTELLIGENCE REPORT\n")
    file.write("-------------------\n")

    for row in lockedInMessages:
        messageId = row[0]
        decodedMessage = row[1]
        keywordsFound = row[2]
        score = row[3]
        keywordText = ", ".join(keywordsFound)

        file.write("Message ID: " + messageId + "\n")
        file.write("Decoded message: " + decodedMessage + "\n")
        file.write("Keywords found: " + keywordText + "\n")
        file.write("Threat score: " + str(score) + "\n\n")

    #task 6: calc and write the summary values
    highestScore = 0
    keywordTotals = {}
    communicationNetwork = {}
    for keyword in keywords:
        keywordTotals[keyword] = 0
        communicationNetwork[keyword] = []

    for row in lockedInMessages:
        if row[3] > highestScore:
            highestScore = row[3]
        for keyword in row[2]:
            keywordTotals[keyword] = keywordTotals[keyword] + 1
            communicationNetwork[keyword].append(row[0])

    file.write("SUMMARY\n")
    file.write("-------------------\n")
    file.write("Total Messages: " + str(len(lockedInMessages)) + "\n")
    file.write("Highest Threat Score: " + str(highestScore) + "\n\n")
    file.write("Keyword Totals\n")
    for keyword in keywords:
        file.write(keyword + ": " + str(keywordTotals[keyword]) + "\n")

    #advanced task 2: communication network
    file.write("\n")
    file.write("Communication Network\n")
    file.write("-------------------\n")
    for keyword in keywords:
        if len(communicationNetwork[keyword]) > 0:
            file.write(keyword + "\n")
            for messageId in communicationNetwork[keyword]:
                file.write("  -> " + messageId + "\n")
            file.write("\n")
    file.close()

#x function for advanced task 3
def EncodeWithOuterX(message):
    return "x" + message + "x"


#advanced task 3: get a message from the user
def EncodeNewMessage():
    message = input("Enter a message: ")

    print("")
    print("Encoding Methods")
    print("1 - Reverse each word")
    print("2 - Add # noise characters")
    print("3 - Add x to beginning and end")
    print("4 - Create a ! encoded message")
    choice = input("Choose an option: ")

    if choice == "1":
        encodedMessage = ReverseWordsIfContainSpaces(message)
    elif choice == "3":
        encodedMessage = EncodeWithOuterX(message)
    else:
        print("Option not avaliable")
        return

    print("")
    print("Original Message:")
    print(message)
    print("")
    print("Encoded Message:")
    print(encodedMessage)


def Main():
    keywords = ReadKeywords(KEYWORDS_FILE)
    messages = OpenAndStoreMessages(MESSAGES_FILE)

    lockedInMessages = []
    for row in messages:
        messageId = row[0]
        encodedMessage = row[1]

        decodedMessage = DecodeMessage(encodedMessage)
        keywordsFound = FindKeywords(decodedMessage, keywords)
        score = CalculatingAThreatScore(decodedMessage)

        lockedInMessages.append([messageId, decodedMessage, keywordsFound, score])

    WriteReport(lockedInMessages, keywords)

    EncodeNewMessage()

Main()

