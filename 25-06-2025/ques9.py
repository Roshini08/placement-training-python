with open("sample.txt", "r") as f:
    lines = f.readlines()
    words = sum(len(line.split()) for line in lines)

print("Lines:", len(lines))
print("Words:", words)
