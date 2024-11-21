import pytest
from table import Table

class TestTableClass:
    table = Table.from_csv("tests/test_csv_1.csv")
    def test_table_count(self):
        assert Table.table_count == 1
    def test_ambiguous_field_name(self):
        assert 'Exam,ple' in self.table.data
