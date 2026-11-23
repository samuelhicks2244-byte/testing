digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def CalculatingAThreatScore(string):
    score = 0
    threatWordTotal = 0
    if "SECRET" in string:
        score += 10
        threatWordTotal += 1
    elif "MEET" in string:
        score += 5
        threatWordTotal += 1
    elif "ATTACK" in string:
        score += 15
        threatWordTotal += 1
    for digit in digits:
        if digit in string:
            score += 3
    print("There are", threatWordTotal, "threat words in this string and its threat score is", score)

CalculatingAThreatScore("xRENDEZVOUS0600SAFEHOUSEx")
CalculatingAThreatScore("xMEETATBRIDGE0800x")
CalculatingAThreatScore("xATTACKATBRIDGE0800x")
CalculatingAThreatScore("xSECRETATBRIDGE0800x")
CalculatingAThreatScore("xSECRETATBRIDGEATTACK0800x")
CalculatingAThreatScore("NON-EVIL-MESSAGE")