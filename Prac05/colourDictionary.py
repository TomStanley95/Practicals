__author__ = 'Tom Stanley'
HEX_COLORS_DICTIONARY = {"Aliceblue": "#f0f8ff", "Blue": "#0000ff", "Cyan": "#00ffff", "Gold": "#ffd700",
                         "Gray": "#bebebe", "Green": "#00ff00", "Hotpink": "#ff69b4", "Purple": "#a020f0",
                         "Red": "#ff0000", "Yellow": "#ffff00"}

# print(HEX_COLORS_DICTIONARY)

color = input("Enter color:").lower().capitalize().strip().replace(" ", "")
# print(color)

while color != "":
    if color in HEX_COLORS_DICTIONARY:
        print(" The Hex code for {} is {}".format(color, HEX_COLORS_DICTIONARY[color]))
    else:
        print("Invalid color name")
    color = input("Enter color:").lower().capitalize().strip().replace(" ", "")
