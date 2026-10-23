text = "  pendidikan   matematika  "
teks = text.strip()
while "  " in teks:
    teks = teks.replace("  ", " ")
teks = teks.title()
print(teks)