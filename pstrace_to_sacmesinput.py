import pandas as pd

spreadsheet_name = "tester.xlsx"

read_file = pd.read_excel(spreadsheet_name)
title =  read_file.columns.tolist()

titleCleaned = []
titleDuplicated = []
frequencies = []
electrodeNums = {}
electrodeCount = []
for t in title:
    if "Unnamed" not in t:
        t = t.replace(" ", "") 
        attributes = t.split("Hz-", 1)
        electrode = attributes[1].split("-")[0]+"-"+attributes[0]
        electrodetype = electrode.split("-")[0]
        if electrode not in electrodeNums.keys():
            electrodeNums[electrode] = 1
        else:
            electrodeNums[electrode] += 1
        if electrodetype not in electrodeCount:
            electrodeCount.append(electrodetype)


        name= "E"+str(electrodeCount.index(electrodetype)+1)+"_sample_"+attributes[0]+"Hz_"+str(electrodeNums[electrode])
         
        titleCleaned.append(name)
        titleDuplicated.append(name)
        titleDuplicated.append(name)

#print(titleCleaned)
#print(titleDuplicated)

for i in range(len(titleCleaned)):
    read_file = pd.read_excel(spreadsheet_name)
    read_file.columns = titleDuplicated
    read_file = read_file[titleCleaned[i]]
    read_file = read_file.iloc[1:]
    read_file.to_csv (titleCleaned[i]+".csv", index = None, header=None, encoding = "utf-8")

data = []
count =1 
for i in electrodeCount:
    data.append([count, i])
    count +=1
df = pd.DataFrame(data, columns=['Electrode #', 'Target Concentration'])
df.to_excel("ElectrodeNames.xlsx")