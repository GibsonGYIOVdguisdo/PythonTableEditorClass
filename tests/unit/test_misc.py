from table import Table

class TestMisc:
    def test_get_file_name(self):
        table1 = Table.from_csv("tests/test_csv_1")
        table2 = Table.from_csv("tests/test_csv_1.csv")
        assert table1.data == table2.data