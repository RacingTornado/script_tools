#!/usr/bin/env python
#Generate a report rgarding formatting for pull requests
from __future__ import print_function
import os, sys
import xlsxwriter
import re
from colorama import init, Fore, Back, Style

def print_colour(str_show):
    print(Fore.CYAN + Back.MAGENTA + Style.BRIGHT + "j")










init(autoreset=True)
print_colour("HI");
begin_cl=['Header #ifdef','Have you indented with uncrustify???','Code should be in the right place.'];
for elem in begin_cl:
    print (elem)
checklist = ['Formatting and spacing','Function naming','Punctuation','Enum or typedef wrapping','Implementation and API separation','BYTE and BOOL ','MACROS for conversion','Try to use short names','Sentences should start with captial letter']
checklist_func=['Why is a given function needed?','What does is the function *required* to do?','What does requiring a function to do something actually mean?','How many different ways could you implment the function?','How would a person use the function?','How could a person abuse the function?','How could a person get the function usage wrong?','Should the function be public or private?','Is every function in the API needed / essential?','What trade offs are you making in the API?','Be as small as possible to achieve the stated goal.','Only the changes needed to achieve the goal should be in the pull request.']



data=""
with open("data.h") as f:
    data=f.read()
    filename = raw_input()
p = re.compile(ur'(\/\*\*[\s\S]*?\*\*\/(\n.*\n))', re.MULTILINE)
k= re.findall(p, data)
for (letters, numbers) in k:
    print (letters)
    print (numbers)
    raw_input();
checklist=[]
fname = "";
folder= os.getcwdu();
print (folder);
fname = folder + sys.argv[0];
print (fname);
# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)
bold = workbook.add_format({'bold': True})
#with open(fname) as f:
#    content = f.readlines()
	# Write some simple text.
worksheet.write('A1', 'Hello')
	# Text with formatting.
worksheet.write('A2', 'World', bold)
	# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)


workbook.close()
