text = "ku ku ku kur "
word_index = 0
word_count = 0
for i in range(len(text)):
    if text[i] == " ":
        if word_index == 4:
            word_count += 1
        word_index = 1
        continue
    
    word_index+=1

if word_index == 4:
    word_count += 1

print(word_count)