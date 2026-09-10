class CSVExporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self):
        return f"CSV Export: {self.file_name}.csv"


class JSONExporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self):
        return f"JSON Export: {self.file_name}.json"


class PDFExporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self):
        return f"PDF Export: {self.file_name}.pdf"


def run_exporters(exporters):
    # Process every exporter using one loop
    for i in exporters:
        print(i.export())


file_name = input()

# Create exporter objects, store them in one list and run them
c = CSVExporter(file_name)
j = JSONExporter(file_name)
p = PDFExporter(file_name)

exporters = [c, j, p]
run_exporters(exporters)