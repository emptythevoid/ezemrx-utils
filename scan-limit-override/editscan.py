import os, shutil
import sys
import subprocess


#with open(sys.argv[1], 'r') as file:
##    for line in file:
##        print(line)

# Create an outfile in the the project directory.
outfile = open(r"c:\editscan\scan.jnlp",'w')

#outfile.write("test")   
with open(sys.argv[1], 'r') as file:
    for line in file:
        if 'totalPages' in line:
            print("found the line")
	    # override parameter to say 99
            outfile.write(r'		<param name="totalPages"  value="99"/>'+"\n")
        else:	
            outfile.write(line)

outfile.close()
# the r is to force Python to interpret it as a raw string treat backslashes as raw characters, not escape
#subprocess.run([r"C:\Program Files (x86)\Java\jre1.8.0_351\bin\javaws.exe", r"c:\editscan\scan.jnlp"])  #8u351
subprocess.run([r"C:\Program Files (x86)\Java\jre1.8.0_192\bin\javaws.exe", r"c:\editscan\scan.jnlp"])    #8u192

# kill java process, in case it gets stuck. The process shouldn't get killed until the above process has finished.
subprocess.run([r"taskkill", r"/f /t /im jp2launcher.exe"])