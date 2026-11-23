def CalculatingAThreatScore(string):
    upperString = string.upper()

    score = 0
    threatWordTotal = 0

    if "SECRET" in upperString:
        score += 10
        threatWordTotal += 1
    if "MEET" in upperString:
        score += 5
        threatWordTotal += 1
    if "ATTACK" in upperString:
        score += 15
        threatWordTotal += 1
    for character in string:
        if character.isdigit():
            score += 3
            break                        #makes sure 3 isnt added mutltiple times
    return score, threatWordTotal