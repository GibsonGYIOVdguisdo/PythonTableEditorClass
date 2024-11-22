from table import Table

class TestCSVExporting:
    def test_exporting_speechmarks(self):
        table = Table({'"Quote"':['"Hello"']})
        table.save_to_csv("tests/test_save.csv")
        test_csv = open("tests/test_save.csv")
        assert(test_csv.readlines() == ['"""Quote"""\n', '"""Hello"""'])