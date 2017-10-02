
#example word find puzzle
l = [
'nllabaqgirlxhezcfabqlvtdgzten',
'imbvtlopemituymtxxgametmwibeh',
'goonenetjwxkyszaztozlfzgkbrpv',
'awyuhwqpbugeviflgqesclnineele',
'mssnevesntwoucvgojwniygrztxnm',
'enufpxicqqhomeballufdxbltyfjo',
'puknxxjmjtkflkorvctcbrifhovjh',
'hlrvxfvtdshbeoywgkwwfeofrbxkj',
'oymvilwghjbgnteotkvqodrwepguw',
'mzhvvoteirfeicbekfabpflseipho',
'exejminsrgeanenueqbloojcrzthr',
'aeihvioirmsewgcuvhxudyylluwjd',
'lkognxxtitccynkniorifkufudowy',
'tmorkhothfztflezfddusorisnhce',
'ejnfqsyrwbqeblvvifxpwnpvzehwm',
'ametereydsenoxfdeighthcetvkqa',
'knweueqvprfiymoqmssyitnqmestg',
'duuovcesezoyhtuggeerhtpujsmwz',
'gmftktnmlngwtbrhbbqjabftfreog',
'eiqycwhnifooonlqoowtfdgzamrzh',
'ncruofmgqtlfwyemymsixalnytujz',
'uzwlbnndivuktxpvtwsmtlbekhozp',
'fwgvjlbotevecvthefxeasxtngfnt',
'sojxdbnqxxvetdelkstbveontiyoi',
'grrilebbvgvrmfivezrxigenbenlm',
'edbspveninvhfuleighteefweeile',
'mpaonrcmdohtfyuepkndmumzoltad',
'atlgirloweumdcwordupilbozrgbz',
'grlzijfunxyemagstgfptyvchydkh'
]

words = [
'one',
'two',
'three',
'four',
'five',
'six',
'seven',
'eight',
'nine',
'ten',
'boy',
'money',
'girl',
'star',
'game',
'easy',
'dollar',
'home',
'time',
'ball',
'word',
'color',
'life',
'happy',
'fun'
]

n_row = len(l)
n_col = len(l[0])
found = 0

# to do: implement the search to find all words in the grid
for row in range(n_row):
    for col in range(n_col):
        for d_row in [-1,0,1]:
            for d_col in [-1,0,1]:
                for word in words:
                    temp_row = row
                    temp_col = col
                    for pos, char in enumerate(word):

                        if temp_row < 0 or temp_row >= n_col:
                            break
                        if temp_col < 0 or temp_col >= n_row:
                            break
                        if l[temp_row][temp_col] != char:
                            break
                        temp_row += d_row
                        temp_col += d_col
                    else:
                        found += 1
                        print word, row, col
                        
print found    

