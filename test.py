import pandas as pd

excel_file = "Test.xlsx"

df = pd.read_excel(excel_file)

print(df)

print(type(df))

words = df["besede"]

##word_len = 0

##one_letter_word = []
##two_letter_word = []
##three_letter_word = []
##four_letter_word = []
##five_letter_word = []
##six_letter_word = []
##seven_letter_word = []
##eight_letter_word = []
##nine_letter_word = []
##ten_letter_word = []
##eleven_letter_word = []
##twelve_letter_word = []
##thirteen_letter_word = []
##fourteen_letter_word = []
##fifteen_letter_word = []
##other_letter_word = []
##
##for w in words:
##    try:
##        print(w)
##        word_len = len(w)
##        match word_len:
##            case 1:
##                one_letter_word.append(w)
##            case 2:
##                two_letter_word.append(w)
##            case 3:
##                three_letter_word.append(w)
##            case 4:
##                four_letter_word.append(w)
##            case 5:
##                five_letter_word.append(w)
##            case 6:
##                six_letter_word.append(w)
##            case 7:
##                seven_letter_word.append(w)
##            case 8:
##                eight_letter_word.append(w)
##            case 9:
##                nine_letter_word.append(w)
##            case 10:
##                ten_letter_word.append(w)
##            case 11:
##                eleven_letter_word.append(w)
##            case 12:
##                twelve_letter_word.append(w)
##            case 13:
##                thirteen_letter_word.append(w)
##            case 14:
##                fourteen_letter_word.append(w)
##            case 15:
##                fifteen_letter_word.append(w)
##            case _:
##                other_letter_word.append(w)
##    except :
##        four_letter_word = "null"

##a = []
##for i in range(17):
##    a.append([])
####a = [a.append([]) for i in range(16)]
##
##for w in words:
##    try:
##        a[len(w)].append(w)
##    except:
##        print("napaka")
##        print(w)

a = []
for w in words:
    try:
        if (len(a) - 1) >= len(w):
            a[len(w)].append(w)
        else:
            for i in range(len(w) - (len(a) - 1)):
                a.append([])
            a[len(w)].append(w)
    except:
        print(w)
        a[4].append("null")






print(a[5])






