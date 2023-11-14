def countWords(sentence):
    tences = sentence.split()
    totalWords = len(tences)
    
    uniqueWords = set(tences)
    totalUnique = len(uniqueWords)
    
    duplicateWords = [word for word in uniqueWords if tences.count(word) > 1]
    
    print(f"มีคำรวมทั้งหมด {totalWords} คำ")
    print(f"มีคำที่ซ้ำกันรวม {len(duplicateWords)} คำ คือ {' '.join(duplicateWords)}")
    
    for word in duplicateWords:
        count = tences.count(word)
        print(f"คำว่า {word} ซ้ำกัน {count} ครั้ง")

try:
    inputSentence = input("ป้อนประโยค: ")
    countWords(inputSentence)
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")