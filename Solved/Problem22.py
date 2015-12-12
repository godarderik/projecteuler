f = open("names.txt", "rU")
text  = f.read()
text = text.replace("\"", "")
text = text.split(",")
text.sort()
#we have a list with all names in alpha order

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
textValue = 0
total = 0
y = 0
while y < len(text):
    for x in text[y]:
        textValue+=letters.index(x) + 1
    textValue *= (y + 1)
    total += textValue
    textValue = 0
    y += 1
print total 



