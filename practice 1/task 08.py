textToCalc = input()

sum = textToCalc.split(' + ')
if len(sum) == 2:
    print(float(sum[0]) + float(sum[1]))

sub = textToCalc.split(' - ')
if len(sub) == 2:
    print(float(sub[0]) - float(sub[1]))

mull = textToCalc.split(' * ')
if len(mull) == 2:
    print(float(mull[0]) * float(mull[1]))

div = textToCalc.split(' / ')
if len(div) == 2:
    print(float(div[0]) / float(div[1]))