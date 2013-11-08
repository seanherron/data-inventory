import urllib2
from mmap import mmap,ACCESS_READ
import os
from xlrd import open_workbook
import csv

from .models import Program_Code, Bureau_Code

def program_code_import(filename):
    workbook = open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    
    for row in range(sheet.nrows):
        program = []
        for col in range(sheet.ncols):
            cell = sheet.cell(row,col).value
            program.append(cell)
        if program[5] == 'ProgramCodePODFormat':
            pass
        else:
            obj, created = Program_Code.objects.get_or_create(agency=program[0], program_name=program[1], program_code=program[5])
            
def bureau_code_import(filename):
    file = open(filename, "rb")
    reader = csv.reader(file)
    for row in reader:
        bureau = []
        for col in row:
            bureau.append(col)
        if bureau[0] == "Branch":
            pass
        else:
            obj, created = Bureau_Code.objects.get_or_create(branch=bureau[0], department=bureau[1], agency=bureau[2], agency_code=bureau[3], bureau_code=bureau[4])