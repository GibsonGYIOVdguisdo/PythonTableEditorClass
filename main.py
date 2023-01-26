class table():
    table_count=0
    def __init__(self, data):
        self.data=data
        table.table_count+=1
    @classmethod #Alternative constructor
    def from_csv(cls, filename):
        data={}
        split=filename.split(".")
        if len(filename)==0:
            raise ValueError("The value inputed is invalid")
        try:
            if len(split)==2:
                if split[1]=="csv":
                    f=open(filename,"r")
            else:
                f=open(f"{filename}.csv","r")
        except:
            raise ValueError("The table inputed does not exist")
        lines=f.readlines()
        f.close()
        if len(lines)==0:
            raise ValueError("The table inputed has no data")
        fields=lines[0].split(",")
        for i in fields:
            i=i.replace("\n","")
            data[i]=[]
        for i in lines[1:]:
            i=i.replace("\n","")
            records=i.split(",")
            for z,x in zip(data,records):
                data[z].append(x)
        return cls(data)
    def add_uid_field(self): #This is likely to be later removed
        self.data["UID"]=[]
        for i in range(0,len(self.data[str(list(self.data.keys())[0])])):
            self.data["UID"].append(str(i))
    def del_uid_field(self):
        del self.data["UID"]
    def add_record(self,record):
        if len(self.data)!=len(record):
            raise ValueError(f"Invalid data inputed as record! Table has {len(self.data)} fields but {len(record)} values where assigned!")
        else:
            for key,value in zip(self.data,record):
                self.data[key].append(value)
    def add_field(self, field_name):
        self.data[field_name]=[]
        for i in range(0,len(self.data[str(list(self.data.keys())[0])])):
            self.data[field_name].append("")

    def save_to_csv(self, file_name, fill_empty_vals=True):
        data_to_write=""
        for i in self.data:
            data_to_write+=f"{i},"
        data_to_write=data_to_write[:-1]+"\n"
        for i in range(0,len(self.data[str(list(self.data.keys())[0])])):
            for key in self.data:
                if self.data[key][i]=="":
                    if fill_empty_vals==True:
                        data_to_write=data_to_write+"EmptyVal,"
                else:
                    data_to_write=data_to_write+f"{self.data[key][i]},"
            data_to_write=data_to_write[:-1]+"\n"
        data_to_write=data_to_write[:-1]
        try:
            f=open(file_name,"x")
        except:
            f=open(file_name,"w")
        finally:
            f.write(data_to_write)
            f.close()
    def edit_field_name(self, old_field_name,new_field_name):
        self.data[new_field_name]=self.data.pop(old_field_name)
    def edit_record(self, record_index, field_name, new_value):
        if field_name in self.data:
            if len(self.data[str(list(self.data.keys())[0])])>=record_index:
                self.data[field_name][record_index]=new_value
            else:
                raise IndexError("The entered index is not in the table!")
        else:
            raise KeyError("The entered field is not in the table!")
    def del_field(self,*fields):
        for field in fields:
            if field in self.data:
                del self.data[field]
            else:
                raise KeyError("The entered field is not in the table!")
    def del_record(self, *record_indexes):
        record_indexes=sorted(list(record_indexes))
        record_indexes=record_indexes[::-1]
        for record_index in record_indexes:
            if len(self.data[str(list(self.data.keys())[0])])>=record_index:
                for key in self.data:
                    del self.data[key][record_index]
            else:
                raise IndexError("The entered index is not in the table!")
    def set_field_type(self,field,type):
        type=type.upper()
        temp_field=self.data[field]
        self.data[field]=[]
        for i in temp_field:
            if type=="BOOL" or type=="BOOLEAN":
                self.data[field].append(bool(i))
            elif type == "INT" or type == "INTEGER":
                self.data[field].append(int(i))
            elif type == "FLOAT" or type == "REAL":
                self.data[field].append(float(i))
            elif type == "STRING" or type == "TEXT":
                self.data[field].append(str(i))
    def get_field_type(self,field):
        return(type(self.data[field][0]))
    def get_ordered_index(self, field, **kwargs):
        index={}
        if "count" not in kwargs.keys():
            count=len(self.data[field])
        else:
            count=kwargs["count"]
        for i,v in enumerate(self.data[field]):
            if v in index.keys():
                index[v].append(i)
            else:
                index[v]=[i]
        tempfield=sorted(list(set(self.data[field])))
        indexes=[]
        if "order" in kwargs.keys():
            upordown=kwargs["order"].upper()
            if upordown=="UP" or upordown=="ASCENDING" or upordown=="ASC":
                tempfield=tempfield[::-1]
        for i,v in enumerate(tempfield[::-1]):
            if i>count:
                break
            else:
                indexes+=index[v]
        return(indexes[:count])
    def get_records(self,*record_indexes):
        if type(record_indexes[0])==list:
            record_indexes=record_indexes[0]
        records=[]
        for index in record_indexes:
            temp_record=[]
            for i in self.data:
                temp_record.append(self.data[i][index])
            records.append(temp_record)
        return(records)
    def __str__(self):
        records="{:<8}".format("index ")
        for i in self.data:
            records+="{:<8}".format(f"{i} ")
        records+="\n"
        for index in range(0,len(self.data[str(list(self.data.keys())[0])])):
            records+="{:<8}".format(f"{index} ")
            for key in self.data:
                if self.data[key][index]=="":
                    records+="{:<8}".format("\"\"")
                else:
                    records+="{:<8}".format(f"{self.data[key][index]} ")
            records+="\n"
        records=records[:-1]
        return(records)
    def __repr__(self):
        return(f"table({str(self.data)})")

