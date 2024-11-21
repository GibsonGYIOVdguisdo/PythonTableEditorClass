from table import Table

class TestCSVImporting:
    table = Table.from_csv("tests/test_csv_1.csv")
    def test_fields_imported(self):
        assert len(self.table.data) == 5
    def test_field_name(self):
        assert "Name" in self.table.data
    def test_ambiguous_field_name(self):
        assert 'Exam,ple' in self.table.data