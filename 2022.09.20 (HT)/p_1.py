def pvt(s):
    for j in range(2, (len(s) // 2) + 1):
        for i in range(len(s) + 1 - j):
            chek = s[i:i + j]
            if s.count(chek) > 1:
                s = s.replace(chek, '.')
                toch = (s.count(chek)) * '.'
                s = s.replace(toch, '')
                for j in range(s.count('.')-1):
                    s = s.replace(".", "", 1)
                s = s.replace('.', chek)
    return s


a = "знаменоносец \nверхненемецкий \nлермонтововед \nлилововатый \nминералология \nтрагикокомедия \nбелолобый \nмононом \nдикообраз \nгладкокожий \nрозововолосый \nфилология \nстипепендия \nпараллелепипед \nминскский \nшолохововедение \nгаплологияодиннад"


with open("haplology.txt", mode="w") as hap:
    hap.writelines(a)

with open("haplology.txt", mode="r") as hp:
    b = hp.readlines()

for num, wrd in enumerate(b):
    if pvt(wrd) != -1:
        print(pvt(wrd))
