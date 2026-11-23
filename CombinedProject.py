## for workload management habits i made the functions required for each task in separate files and then combined them

# read all communications from messages.txt. There will be between zero and n lines in the file, each communication is on a separate line and you should process every messages in the file.

def OpenAndStoreMessages(filename):
    file = open(filename, "r")

    for line in file:
        line = line.strip()
        messages = []
        if line != "":
            TwoParts = line.split("|", 1)
            msg_id = TwoParts[0]
            string = TwoParts[1]
            row = []
            row.append(msg_id)
            row.append(string)
            messages.append(row)
            print(messages)

OpenAndStoreMessages("messages-20.txt")

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