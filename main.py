
record=""
table1={}
f = open("table.csv", "r")
asdas=f.readlines()
f.close()
fields=[]
_cur=""
for i in asdas[0]:
  if i == "," or i=="\n":
    table1[_cur.strip()]=[]
    fields.append(_cur.strip())
    _cur=""
  else:
    _cur=_cur+i

index=0
for i in asdas[1:len(asdas)]:
  index=0
  pos=0
  for x in i:
    if x != ",":
      _cur=_cur+x
    if x == "," or pos==len(i)-1:
      table1[fields[index]].append(_cur.strip())
      _cur=""
      index=index+1
    
    pos+=1


while True:
  Option=input("What would you like to do?: ")
  if Option=="create":
    print("new record created")
    for i in table1:
      if i == "uid":
        newuid=str(len(table1["uid"]))
        while newuid in table1["uid"]:
          newuid=str(int(newuid)+1)
        table1[i].append(newuid)
        continue
      table1[i].append("empty")
  elif Option=="read":
    Option=input("what record would you like (enter uid or type all): ")
    record=""
    if Option=="all":
      for i in table1:
        record=record+" "+i
      print(record)
      for x in range(0,len(table1["uid"])):
        record=""
        for i in table1:
          record=record+" "+str(table1[i][x])
        print(record)
    else:
      if Option in table1["uid"]:
        print("record found")
        record=""
        for i in table1:
          record=record+" "+i
        record+="\n"
        for x in table1:
          record=record+" "+str(table1[x][table1["uid"].index(Option)])
        print(record)
      else:
        print("record not found")
  elif Option=="update":
    record=input("what record would you like to update?(enteruid): ")
    if record in table1["uid"]:
      field=input("what field would you like to update?: ")
      if field in table1:
        table1[field][table1["uid"].index(record)]=input("What would you like to set it to?: ")
      else:
        print("field not found")
    else:
      print("record not found")
  elif Option=="delete":
    record=input("what record do you want to delete?(enter uid): ")
    if record in table1["uid"]:
      index213=table1["uid"].index(record)
      for i in table1:
        print(table1[i][index213])
        table1[i].pop(index213)
    else:
      print("record not found")
  elif Option=="help":
    print("create: creates a new record")
    print("read: reads a record or all records")
    print("update: updates a record")
    print("delete: deletes a record")
    print("help: shows this menu")
  else:
    print("command not found")
  f = open("table.csv", "w")
  save=""
  index=0
  for i in table1:
    if index==len(table1)-1:
      save=save+i+"\n"
    else:
      save=save+i+","
      index+=1

  index1=0
  for i in table1["uid"]:
    index2=0
    for x in table1:
      save+=table1[x][index1]
      if index2!=len(table1)-1:
        save+=","
      index2+=1
    if index1!=len(table1["uid"])-1:
      save+="\n"
    index1+=1
  f.write(save)
  f.close()
