import subprocess, os

#path for ghostscript executable
gs_path = 'C:\\Program Files\\gs\\gs9.23\\bin'

# dir where pdfs are located
dir_name = '\Desktop'

# pdf to extract text from
file_name = os.path.join(dir_name,'text.pdf')

# output text file name
outfile_name = os.path.join(dir_name,'text.txt')

os.chdir(gs_path)

filepath = "\Desktop\\test.pdf"
filepath2 = "\Desktop\\test.txt"

subprocess.check_output(['gswin64',
'-dBATCH', '-dNOPAUSE', '-sPageList=1-', 'sDEVICE=txtwrite',
'-sOUTPUTFILE=\Desktop\\test.txt',
'\Desktop\\test.pdf'])
