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
    file.close()
    return messages
