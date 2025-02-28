from zipfile import ZipFile
with ZipFile('input (2).zip') as myzip:
    for line in myzip.namelist():
        if '/' not in line:
            print(line)
        else:
            count = line.count('/')
            line = line.split('/')
            if line[-1]:
                print('  ' * (count - 2) + line[-1])
            else:
                print('  ' * (count - 2) + line[-2])