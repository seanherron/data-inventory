import urllib2
from mmap import mmap,ACCESS_READ
import os
from xlrd import open_workbook

from .models import Program_Code

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