from subprocess import call
import csv

def convert_po(po_path, media_path):
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

def update_po_file(data, po_path, media_path):
    """
        update po file with new messages
    """
    try:
        with open(media_path + 'tmp.csv', 'wb') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
        call(["csv2po", media_path + 'tmp.csv', po_path])
        return True
    except Exception as e:
        print e
        return False
