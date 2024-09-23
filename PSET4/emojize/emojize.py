import emoji

# Prints emoji
s = input("Input: ").lower()
print("Output:", emoji.emojize(s, language="alias"))
