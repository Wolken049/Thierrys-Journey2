def FormatArray(data):
    output = ""
    for item in data:
        if item != "":
            output = output + item + " "
    return output