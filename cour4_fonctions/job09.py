def Moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

note1 = int(input("Entre la premiere note:"))
note2 = int(input("Entre la premiere note:"))
note3 = int(input("Entre la premiere note:"))

moyenne_etudiant = moyenne(note1, note2, note3)

if 15 <= moyenne_etudiant <= 20:
    print("Mention TB")
elif 10 <= moyenne_etudiant < 15:
    print("Mention B")
elif 8 <= moyenne_etudiant < 11:
    print("Mention AB")
elif 0 <= moyenne_etudiant < 8: 
    print("Moyenne mauvaise")