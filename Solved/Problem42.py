f = open("words.txt", "rU")
text  = f.read()
text = text.replace("\"", "")
text = text.split(",")
wordValue = 0
triangleWordCount = 0
triangles = []
z = 1
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
while z < 30:
    triangles.append(.5* z * (z + 1))
    z += 1

for y in text:
    for x in y:
        wordValue += letters.index(x) + 1
    if triangles.count(wordValue) <> 0:
        triangleWordCount += 1
    wordValue = 0
print triangleWordCount

