## for workload management habits i made the functions required for each task in separate files and then combined them after

MESSAGES_FILE = "messages-20.txt"
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
            TwoParts = line.split("|", 1)
            msg_id = TwoParts[0]
            string = TwoParts[1]
            row = []
            row.append(msg_id)
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
    if " " in string:
        wordList = string.split(" ")
        reversedWordList = []
        for word in wordList:
            reversedWordList.append(word[::-1])
        cleanString = " ".join(reversedWordList)
    else:
        cleanString = string
    return cleanString

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

# combine the rules in the right order and use if statements again for easier code reading
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

#task 3: keyword analysis
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

#search the decoded message with the keywords from file
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
    for keyword in keywords:
        keywordTotals[keyword] = 0

    for row in lockedInMessages:
        if row[3] > highestScore:
            highestScore = row[3]
        for keyword in row[2]:
            keywordTotals[keyword] = keywordTotals[keyword] + 1

    file.write("SUMMARY\n")
    file.write("-------------------\n")
    file.write("Total Messages: " + str(len(lockedInMessages)) + "\n")
    file.write("Highest Threat Score: " + str(highestScore) + "\n\n")
    file.write("Keyword Totals\n")
    for keyword in keywords:
        file.write(keyword + ": " + str(keywordTotals[keyword]) + "\n")

    file.close()


#runs the whole analysis: 
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


Main()

