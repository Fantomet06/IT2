with open("./kode-med-mening/penger.txt", "r") as f:
    text = f.read().replace("\n", "+")

with open("./kode-med-mening/penger.txt", "w") as f:
    f.write(text)
