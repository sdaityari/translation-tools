from subprocess import call
import csv

def convert_po(po_path, pk, media_path):
    """
        convert po file
    """
    try:
        call(["po2csv", po_path, media_path + 'tmp.csv' ])
        with open(media_path + 'tmp.csv', 'rb') as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
        return data
    except Exception as e:
        print e
        return False
