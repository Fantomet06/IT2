with open("./kode-med-mening/penger.txt", "r") as file:
    data = file.read()

navn = ["femmere", "femmer", "femkroner", "femkrone", "tiere", "tier", "tikroner", "tikrone", "femtilapper", "femtilapp", "tohundrelapper", "femhundrelapper", "tusenlapper","hundrelapper","tohundrelapp","femhundrelapp","tusenlapp", "hundrelapp", "kroner", "kr", "krone"]
tall = [5, 5, 5, 5, 10, 10, 10, 10, 50, 50, 200, 500, 1000, 100, 200, 500, 1000, 100, 1, 1, 1]

for i in navn:
    data = data.replace(i, str(tall[navn.index(i)]))



with open("./kode-med-mening/penger.txt", "w") as file:
    file.write(data)


with open("./kode-med-mening/penger.txt", "r") as file:
    data = file.read()

navn = ["en", "to", "tre", "fire", "fem", "seks", "syv", "åtte", "ni", "ti"]
tall = [1,2,3,4,5,6,7,8,9,10]

for i in navn:
    data = data.replace(i, str(tall[navn.index(i)]))
    
with open("./kode-med-mening/penger.txt", "w") as file:
    file.write(data)