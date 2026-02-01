def Readfile():
    data = [""] * 45
    index = 0
    Path = r"C:\Users\Wolke\Downloads\11_9618_41_Confidential Source Files November 2024\Source files\Data.txt"
    try:
        file = open(Path, "r")
        for line in file:
            if index < 45:
                data[index] = line.strip()
                index += 1
        file.close()
    except:
        print("File not found!")
    return data