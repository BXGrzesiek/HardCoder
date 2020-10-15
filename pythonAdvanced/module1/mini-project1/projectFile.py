from zipfile import ZipFile
import urllib.request, os, sys, csv
import matplotlib.pyplot as plt
import pandas as pd

def getFile():
    #   downlowad file from url
    #url = 'https://prezydent20200628.pkw.gov.pl/prezydent20200628/data/1/csv/wyniki_gl_na_kand_po_wojewodztwach_csv.zip'
    url = 'https://prezydent20200628.pkw.gov.pl/prezydent20200628/data/1/csv/wyniki_gl_na_kand_po_wojewodztwach_proc_csv.zip'
    urllib.request.urlretrieve(url, 'file.zip')

def extractFile():    
    #   extract file from zip
    with ZipFile('file.zip', 'r') as zipObj:
        zipObj.extractall()

def renameFile():
    #   rename file 
    files = list(os.listdir(os.getcwd()))
    filename = files[2]
    os.rename(filename, "wyniki_proc.csv")


votes = []
candidates = ["Robert BIEDROŃ", 
            "Krzysztof BOSAK", 
            "Andrzej Sebastian DUDA", 
            "Szymon Franciszek HOŁOWNIA",
            "Marek JAKUBIAK",
            "Władysław Marcin KOSINIAK-KAMYSZ",
            "Mirosław Mariusz PIOTROWSKI",
            "Paweł Jan TANAJNO",
            "Rafał Kazimierz TRZASKOWSKI",
            "Waldemar Włodzimierz WITKOWSKI",
            "Stanisław Józef ŻÓŁTEK"
            ]
# candidates1 = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
votes_sum = 0
votes_percent = []
df = pd.read_csv("file.csv", usecols = candidates, sep=r';')

for x in candidates:
    votes.append(sum(df[x]))
print(votes)

votes_sum = sum(votes)
print(votes_sum)

# plt.pie(votes, labels=candidates, shadow = True, autopct='%.0f %%')     # percent as integer
# plt.axis('equal')                                                       # if not equal then pie more like elipse than circle
# plt.show()

# plt.bar(candidates, votes)
# plt.xticks(candidates)
# plt.yticks(votes)
# plt.show()

# for i in votes:
#     votes_percent.append(votes[i]/votes_sum)

explode = [0.05 for i in candidates]                     
# explode[candidates.index("Andrzej Sebastian DUDA")] = 0.1        

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

ax.pie(votes, 
        autopct='%.2f %%', 
        explode = explode, 
        startangle=90, 
        labeldistance=1.05, 
        pctdistance=0.85)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()
#plt.legend(candidates, title='Candidates', loc = "center right")
plt.show()








# with open('results.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     next(csvreader)
#     for row in csvreader:
#         # do stuff with rows...
