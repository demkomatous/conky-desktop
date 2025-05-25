import time
import json
from datetime import datetime

# ${font Casual:size=50}${color1}${execi 3 cat /calendar_output.txt}

def code_text(string, template):
	start = 0
	addition = 50
	script = ""
	string = string.replace("\n", "#")

	for letter in string:
		if letter == "#":
			script += "\n"
			start = 0
		else:
			script += "${goto " + str(start) + "}" + str(letter)
			start += addition

	template += script
	with open(conky_file, "w") as f:
		f.write(template)

# — Home — #
home = "/home/matous/Downloads/Conky"

with open(home + "/config.json", "r") as f:
    config = f.read()
    config = json.loads(config)

conky_template = f"{config['home']}/{config['templates']}/calendar_template"
conky_file = f"{config['home']}/calendar"

with open(conky_template, "r") as f:
	template = f.read()

day_orientation = config["calendar_settings"]["day_orientation"]
if day_orientation not in config["valid_orientations"]:
	raise Exception(f"Invalid value for day_orientation: {day_orientation}")

while True:
	# if day_orientation == "horizontal":
	# 	a = datetime.now().strftime('%A').upper()
	# 	b = datetime.now().strftime('%B').upper()
	# elif day_orientation == "vertical":
	# 	a = datetime.now().strftime('%B').upper()
	# 	b = datetime.now().strftime('%A').upper()
	# else:
	# 	raise Exception(f"Invalid value for day_orientation: {day_orientation}")
	# 	exit()

	a = datetime.now().strftime('%A').upper()
	b = datetime.now().strftime('%B').upper()
	ix_a = -1
	ix_b = -1

	for letter in a:
		if letter in b:
			ix_a = a.index(letter)
			ix_b = b.index(letter)
			break

	if ix_a != -1:
		b_arr = list(b)
		for letter in range(len(b_arr)):
			for i in range(ix_a):
				b_arr[letter] = " " + b_arr[letter]
			b_arr[letter] += "\n"

			b_arr[ix_b] = "#"
		fi = ""
		for letter in b_arr:
			if letter != "#":
				fi += letter
			else:
				fi += a + "\n"

		code_text(fi, template)
	else:
		value = f"{a}\n\n{b}"
		code_text(value, template)
	
	while datetime.now().strftime('%A').upper() == a:
		time.sleep(10)
