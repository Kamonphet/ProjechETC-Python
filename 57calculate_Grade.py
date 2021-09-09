try:
    # fw=open("scoregrade.txt","a",encoding="utf-8")
    # while True :
    #     studentID=input("ป้อนรหัสนักเรียน :")
    #     if studentID == "exit" :
    #         break
    #     score=input("ป้อนคะแนนนักเรียน :")
    #     fw.writelines(studentID+"\t"+score+"\n")
    # fw.close()

    fr = open("scoregrade.txt", "r", encoding="utf-8")
    fw = open("Grade.txt", "w", encoding="utf-8")
    grade = None
    for line in fr.readlines():
        score = line[-4:].strip()
        studentID = line[:-4].strip()
        score = int(score)
        if score >= 90:
            grade = "A"
        elif score >= 85 and score < 90:
            grade = "B+"
        elif score >= 80 and score < 85:
            grade = "B"
        elif score >= 75 and score < 80:
            grade = "C+"
        elif score >= 70 and score < 75:
            grade = "C"
        elif score >= 65 and score < 70:
            grade = "D+"
        elif score >= 60 and score < 65:
            grade = "D"
        else:
            grade = "E"
        print("รหัส =>", studentID, "คะแนน =>", score, "เกรด =>", grade)
        fw.writelines("รหัสนักเรียน =>" + studentID + "\t" +
                      "คะแนน =>" + str(score) + "\t"+"เกรด =>" + grade + "\n")
except Exception as e:
    print(e)
