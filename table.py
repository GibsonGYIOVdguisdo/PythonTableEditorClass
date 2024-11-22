class Table():
    table_count=0
    def __init__(self, data):
        self.data=data
        Table.table_count+=1
    @classmethod
    def from_csv(cls, filename):
        data={}
        filename = Table.__get_file_name(filename, "csv")
        try:
            f=open(filename,"r")
        except:
            raise ValueError("File does not exist")
        lines=f.readlines()
        f.close()
        if len(lines)==0:
            raise ValueError("File is empty")
        fields=Table.__split_csv_line(lines[0])
        for i in fields:
            i=i.replace("\n","")
            data[i]=[]
        for i in lines[1:]:
            i=i.replace("\n","")
            records=Table.__split_csv_line(i)
            for z,x in zip(data,records):
                data[z].append(x)
        return cls(data)
    @classmethod
    def from_json(cls, filename):
        text={}
        filename = Table.__get_file_name(filename, "json")
        try:
            file=open(f"{filename}","r")
        except:
            raise ValueError("The file does not exist")
        text=file.readline()
        file.close()
        return(cls(eval(text)))
    def save_to_json(self, file_name):
        file_name = Table.__get_file_name(file_name, "json")
        Table.__write_to_file(file_name, str(self.data))
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
    def add_field(self, field_name,placeholder=""):
        self.data[field_name]=[]
        for i in range(0,len(self.data[str(list(self.data.keys())[0])])):
            self.data[field_name].append(placeholder)

    def save_to_csv(self, file_name, fill_empty_vals=False):
        data_to_write=""
        for field in self.data:
            if "," in field or '"' in field:
                field = field.replace('"', '""')
                field = f'"{field}"'
            data_to_write+=f"{field},"
        data_to_write=data_to_write[:-1]+"\n"
        for i in range(0,len(self.data[str(list(self.data.keys())[0])])):
            for key in self.data:
                record_value = self.data[key][i]
                if record_value=="":
                    if fill_empty_vals==True:
                        data_to_write=data_to_write+"EmptyVal,"
                else:
                    if "," in record_value or '"' in record_value:
                        record_value = record_value.replace('"', '""')
                        record_value = f'"{record_value}"'
                    data_to_write=data_to_write+f"{record_value},"
            data_to_write=data_to_write[:-1]+"\n"
        data_to_write=data_to_write[:-1]
        file_name = Table.__get_file_name(file_name, "csv")
        Table.__write_to_file(file_name, data_to_write)
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
                raise KeyError(f"The {field} field is not in the table!")
    def del_record(self, *record_indexes):
        record_indexes=sorted(list(record_indexes))
        record_indexes=record_indexes[::-1]
        for record_index in record_indexes:
            if len(self.data[str(list(self.data.keys())[0])])>=record_index:
                for key in self.data:
                    del self.data[key][record_index]
            else:
                raise IndexError(f"The index {key} is not in the table!")
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
        if "count" not in kwargs:
            count=len(self.data[field])
        else:
            count=kwargs["count"]
        for i,v in enumerate(self.data[field]):
            if v in index:
                index[v].append(i)
            else:
                index[v]=[i]
        tempfield=sorted(list(set(self.data[field])))
        indexes=[]
        if "order" in kwargs:
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
    @staticmethod
    def __write_to_file(file_name, data_to_write):
        try:
            file=open(file_name,"x")
        except:
            file=open(file_name,"w")
        file.write(data_to_write)
        file.close()
    @staticmethod
    def __get_file_name(file_name, file_extension):
        if file_name == "":
            raise ValueError("The filename is invalid")
        if file_name[len(file_name) - len(file_extension):].lower() != file_extension.lower():
            file_name=f"{file_name}.{file_extension}"
        return file_name
    @staticmethod
    def __split_csv_line(line):
        if "," not in line:
            return line
        if len(line) < 3:
            return line.split(",")
        unexpected_characters = False
        remove_whitespace = True
        skip_char = False
        split_line = []
        current_segment = ""
        for i in range(len(line[:-1])):
            if skip_char == True:
                skip_char = False
                continue
            first_char = line[i]
            next_char = line[i+1]
            if first_char == "," and unexpected_characters == False:
                if remove_whitespace == True:
                    current_segment = current_segment.strip()
                split_line.append(current_segment)
                remove_whitespace = True
                current_segment = ""
                if next_char == '"':
                    unexpected_characters = True
                    skip_char = True
                continue

            if first_char == '"':
                if next_char == '"':
                    skip_char = True
                    current_segment += first_char
                    continue
                elif next_char == ",":
                    remove_whitespace = False
                    unexpected_characters = False
                    continue

            current_segment += first_char
        if skip_char == False:
            current_segment = f"{current_segment}{line[-1]}"
        split_line.append(current_segment)
        return split_line
    @staticmethod
    def __str__(self):
        records="{:<8}".format("index ")
        for i in self.data:
            records+="{:<8}".format(f"{i} ")
        records+="\n"
        for index in range(0,len(self.data[str(list(self.data)[0])])):
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
