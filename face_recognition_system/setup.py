import cx_Freeze
import sys
import os
base=None

if sys.platform=='win32':
    base="Win32GUI"

os.environ['TCL_LIBRARY']=r"CC:\Users\Krunal\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY']=r"C:\Users\Krunal\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables=[cx_Freeze.Executable("FRAMS.py",base=base,icon="Purple E-sports Illustrative Gaming and Technology Logo.ico")]


cx_Freeze.setup(
    name="Facial Recognition Attendance System",
    options={"build.exe":{"packages":["tkinter","os"],"include_files":["Purple E-sports Illustrative Gaming and Technology Logo.ico",'tcl86t.dll','tk86t.dll','college_images','data','database','attendance_report']}},
    version="1.0",
    description="Facial Recognition Attendance System (FRAMS)| Developed By Team FRAMS",
    executables=executables
    )