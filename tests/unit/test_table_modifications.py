from copy import deepcopy
from table import Table

class TestTableModifications:
    table = Table.from_csv("tests/test_csv_1.csv")
    def test_deleting_field(self):
        table_to_edit = Table(deepcopy(self.table.data))
        table_to_edit.del_field("Score")
        assert not "Score" in table_to_edit.data
    def test_edit_field_name(self):
        table_to_edit = Table(deepcopy(self.table.data))
        table_to_edit.edit_field_name("Score", "Points")
        assert "Points" in table_to_edit.data
    def test_adding_field(self):
        table_to_edit = Table(deepcopy(self.table.data))
        table_to_edit.add_field("Level", 1)
        assert "Level" in table_to_edit.data
    def test_adding_record(self):
        table_to_edit = Table(deepcopy(self.table.data))
        table_to_edit.add_record(["Name10", 32, 32, "example", "other data"])
        assert table_to_edit.get_records(-1) == [["Name10", 32, 32, "example", "other data"]]
    def test_editing_record(self):
        table_to_edit = Table(deepcopy(self.table.data))
        table_to_edit.edit_record(0, "Score", 0)
        assert table_to_edit.data["Score"][0] == 0
    def test_deleting_record(self):
        table_to_edit = Table(deepcopy(self.table.data))
        table_to_edit.del_record(0)
        assert len(self.table.data["Score"]) - 1 == len(table_to_edit.data["Score"])

