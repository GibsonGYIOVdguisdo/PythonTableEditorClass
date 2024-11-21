from table import Table

class TestTableReading:
    table = Table.from_csv("tests/test_csv_1.csv")
    def test_get_records_singular(self):
        assert self.table.get_records(1) == [["Name2", "41","142","examp,le","other data"]]
    def test_get_records_multiple(self):
        assert self.table.get_records(1,2,6) == [["Name2", "41", "142", "examp,le", "other data"],
                                                  ["Name3", "34", "156", "", "other data"],
                                                  ["Name7", "23", "164", "example", "other data"]]
        
    