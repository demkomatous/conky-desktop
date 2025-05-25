## Widget created by Matouš Demko ##

[0] Open terminal from your system application launcher
[1] Then install Conky as Conky Manager via commands:
	$ sudo apt update
	$ sudo apt install conky conky-all conky-manager conky-manager-extra
[2] Install fonts in "Fonts" folder
[3] In terminal change directory where the widget is stored
	e.g.: $ cd /home/Sarah/Downloads
[4] Make init script executable
	$ chmod +x ./init.sh
	- In folder where you run init.sh will appear new files
		- autostart -- This will start widgets and services after login
		- config.json -- There you can customize you widget little bit
[5] Run init.sh
	$ ./init.sh
[6] Open "Startup application" from your system application launcher
[7] Click "Add"; name it as you wish and browse for file named autostart
[8] Click "Add"
[9] Choose your background from folder "Shapes"
[10] Re-log yourself. If nothing happened, do it again
[11] Your widgets are ready 

----------- Customizing -----------
- For permanent changes edit files in folder "Code_templates"
	- Every change will be reflected after relogin
- For temporary changes edit files in root directory
	- Every change will be reflected immediately
- Color customizations should be done with config.json
	- Not tested yet
	- I am sure that it will not work (I know the reason, I will change it) 
- Alignment of calendar is not working in config.json
	- You can try to change it yourself in calendar.py

----------- Some bugs -----------
- When the clock changes time and you're on the desktop, the last active programme is displayed