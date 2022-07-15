"""
AUTHOR: Faris Abufarha

"""

import camelot  # opencv needed
import PyPDF2


def red():
    print("\033[0;31m")


def reset():
    print("\033[0m")


file_name = input('PDF FILE (without extension ): ')
try:
    file = open(f'{file_name}.pdf', 'rb')
    readpdf = PyPDF2.PdfFileReader(file)
    totalpages = readpdf.numPages
    file.close()

except FileNotFoundError:
    red()
    print('FILE NOT FOUND')
    reset()
    exit(1)

print(totalpages)

for i in range(totalpages):
    tables = camelot.read_pdf(f'{file_name}.pdf', pages=str(i))
    if len(tables) > 0:
        tables.export(f'{file_name}{i}.csv', f='csv', compress=True)  # compresses every table in each page

    cnt = 0
    for table in tables:
        table.to_csv(f'{file_name}{i}{cnt}.csv')
        cnt += 1

# print(tables)
