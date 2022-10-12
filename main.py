def FindItem2(find,table):
  _thing={}
  _thing2={}
  _cur=""
  _pos=0
  _last=""
  if ":" not in find:
    return(1)
  for i in find:
    if i==":":
      _last=_cur
      _thing[_cur]=[]
      _cur=""
    elif i==",":
      _thing[_last].append(_cur)
      _cur=""
    elif _pos==len(find)-1:
      _cur+=i      
      _thing[_last].append(_cur)
      _cur=""
    else:
      _cur=_cur+i
    _pos+=1
  for i in _thing:
    if i not in table:
      return([])
    _thing2[i]=[]
  INDEXES= []
  NeedIndexes=[]
  for field in _thing:
    for value in _thing[field]:
      _pos=0
      for value2 in table[field]:
        if value2==value:
          INDEXES.append(_pos)
        _pos+=1
  for i in INDEXES:
    if INDEXES.count(i)>=len(_thing):
      if i not in NeedIndexes:
        NeedIndexes.append(i)
  return(NeedIndexes)

record = ""
table1 = {}
f = open("table.csv", "r")
asdas = f.readlines()
f.close()
fields = []
_cur = ""
pos = 0
for i in asdas[0]:
  if i == "," or i == "\n":
    table1[_cur.strip()] = []
    fields.append(_cur.strip())
    _cur = ""
  else:
    _cur = _cur + i
  pos += 1

index = 0
for i in asdas[1:len(asdas)]:
  index = 0
  pos = 0
  for x in i:
    if x != ",":
      _cur = _cur + x
    if x == "," or pos == len(i) - 1:
      table1[fields[index]].append(_cur.strip())
      _cur = ""
      index = index + 1
    pos += 1

while True:
  Option = input("What would you like to do?: ").lower()
  if Option == "create":
    print("New record created")
    if "uid" in table1:
      for i in table1:
        if i == "uid":
          newuid = str(len(table1["uid"]))
          while newuid in table1["uid"]:
            newuid = str(int(newuid) + 1)
          table1[i].append(newuid)
          continue
        table1[i].append("empty")
    else:
      for i in table1:
        table1[i].append("empty")
  elif Option == "read":
    Option = input("What records would you like?: ")
    record = ""
    if Option == "all":
      for i in table1:
        record = record + " " + i
      print(record)
      for x in range(0, len(table1[list(table1.keys())[0]])):
        record = ""
        for i in table1:
          record = record + " " + str(table1[i][x])
        print(record)
    else:
      Indexes=FindItem2(Option,table1)
      if Indexes==1:
        print("Invalid syntax")
      elif Indexes!=[]:
        for i in table1:
          record = record + " " + i
        for i in Indexes:
          record+="\n"
          for x in table1:
            record+=table1[x][i]+" "
        print(record)
      else:
        print("Record not found")
          
  elif Option == "Update":
    records=FindItem2(input("What records would you like to update?: "),table1)
    if records==[]:
      print("No records found")
    elif records==1:
      print("Invalid syntax")
    else:
      field = input("What field would you like to update?: ")
      UpdateValue=input("What woud you like to set it to?: ")
      if field in table1:
        for i in records:
          table1[field][i] = UpdateValue
  elif Option == "delete":
    userInput=input("What records do you want to delete?: ")
    DelRecords=FindItem2(userInput,table1)
    if DelRecords==[]:
      print("No records found")
    elif DelRecords==1:
      print("Invalid syntax")
    else:
      while DelRecords!=[]:
        for i in table1:
          del table1[i][DelRecords[0]]
        DelRecords=FindItem2(userInput,table1)
  elif Option == "help":
    print("create: creates a new record")
    print("read: reads a record or all records")
    print("update: updates a record")
    print("delete: deletes a record")
    print("help: shows this menu")
  else:
    print("Command not found")
  f = open("table.csv", "w")
  save = ""
  index = 0
  for i in table1:
    if index == len(table1) - 1:
      save = save + i + "\n"
    else:
      save = save + i + ","
      index += 1

  index1 = 0
  for i in table1[list(table1.keys())[0]]:
    index2 = 0
    for x in table1:
      save += table1[x][index1]
      if index2 != len(table1) - 1:
        save += ","
      index2 += 1
    if index1 != len(table1[list(table1.keys())[0]]) - 1:
      save += "\n"
    index1 += 1
  f.write(save)
  f.close()
