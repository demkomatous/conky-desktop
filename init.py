import os
import json


config_file = "config.json"
autostart = "#!/bin/bash\n"

with open(config_file, "r") as f:
	config = json.loads(f.read())

colors_point = "# — Colors — #\n"
home_point = "# — Home — #\n"

for python_file in config["python_files"]:
	autostart += f"python3 {config['home']}/{python_file}.py &\n"
	path = f"{config['home']}/{python_file}.py"

	with open(path, "r") as f:
		lines = f.readlines()

	ix = lines.index(home_point) + 1
	h = config['home']
	lines[ix] = f'home = "{h}"\n'

	with open(path, "w") as f:
		f.writelines(lines)

for conky_file in config["conky_files"]:
	file = f'{config["home"]}/{config["templates"]}/{conky_file}_template'
	with open(file, "r") as f:
		lines = f.readlines()

	ix = lines.index(colors_point) + 1
	lines[ix] = f"color1 {config['schemes'][config['scheme']]['color']}\n"

	with open(file, "w") as f:
		f.writelines(lines)

	autostart += f"conky -c {config['home']}/{conky_file} &\n"

	file = f'{config["home"]}/{conky_file}'
	# Init conky file
	if not os.path.exists(file):
		with open(file, "w") as f:
			f.write("")

with open("autostart", "w") as f:
	f.write(autostart[:-2])