# ReadMe

This is a project to override a page limit when doing a TWAIN scan with ezEMRx. The scan function in ezERMRx generates a jnlp. Firefox is normally configured to open this file type using the javaws.exe.  The jnlp file contains a parameter that limits the number of pages scanned to 15.  This project will intercept the jnlp before it gets to javaws, change the number of pages (currently set to 99) and then send the modified jnlp on to javaws.

# Set up
1.) Install Python https://www.python.org/downloads/windows/

2.) Place project directory into the root of C:\  (c:\editscan)

3.) Edit the .py file's subprocess.run line to point to your current Java runtime's javaws.exe (something like "C:\Program Files (x86)\Java\<yourjavaversionhere>\bin\javaws.exe")

4.) In Firefox, go to Settings and search for Applications. Find the JNLP file type and choose "Use other..." then Browse. For filename, paste in:  C:\editscan\launchedit.bat   This is because Firefox expects an .exe or .com, but we're using a bat file to launch the script.

Now, proceed to scan documents into E-charts as normal. When you've given it a file name and click Scan, the generated JNLP file will open with the batch file, then Python will edit it, save a new one, and then pass that to javaws.exe. The rest of the process works normally.  The only parameter that gets changed is "totalPages" value="99".  You can still select Verification Required, ADF Scan, Duplex, etc.  When scan is complete, choose Upload.
