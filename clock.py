import time
import json
from PIL import Image, ImageDraw
from datetime import datetime


def write_code(code_template, marks):
    for mark in marks.keys():
        code_template = code_template.replace(f"#{mark}", str(marks[mark]))

    return code_template


def get_image_source(value, to_check, option_1, option_2):
    if value == to_check:
        return filled_rectangle_name
    else:
        return outlined_rectangle_name

# — Home — #
home = "/home/matous/Downloads/Conky"

with open(home + "/config.json", "r") as f:
    config = f.read()
    config = json.loads(config)

rectangle_path = f"{config['home']}/{config['shapes']}/"
filled_rectangle_name = config["clock_rectangles"]["filled"]
outlined_rectangle_name = config["clock_rectangles"]["outlined"]

image_code_template = "${image #PATH -p #X,#Y -s 10x20}"
label_code_template = "${goto #X}#LABEL"
clock_template = f"{config['home']}/{config['templates']}/clock_template"
clock_target = f"{config['home']}/clock"

increment_1 = 20
increment_2 = 30

with open(clock_template, "r") as f:
    template = f.read()

while True:
    current_time = datetime.now()
    
    # Script for hour labels
    label_hours = ""
    images_hours = ""
    hour = int(current_time.strftime("%I"))
    am_pm = current_time.strftime("%p")

    position_x = 0
    position_x_image = 0
    position_y = 25
    for i in range(1, 13):
        if i > 10:
            position_x += increment_2
            position_x_image += increment_2
        else:
            position_x += increment_1
            position_x_image += increment_1

        if i == 10:
            position_x_image += 5

        dc = {
            "X": position_x,
            "LABEL": i
        }
        label_hours += write_code(label_code_template, dc)

        image_source = rectangle_path + get_image_source(hour, i, filled_rectangle_name, outlined_rectangle_name)

        dc = {
            "X": position_x_image,
            "Y": position_y,
            "PATH": image_source
        }
        images_hours += write_code(image_code_template, dc)

    position_x += increment_2 + 15
    dc = {
        "X": position_x,
        "LABEL": "a"
    }
    label_hours += write_code(label_code_template, dc)

    image_source = rectangle_path + get_image_source(am_pm, "AM", filled_rectangle_name, outlined_rectangle_name)

    dc = {
        "X": position_x,
        "Y": position_y,
        "PATH": image_source
    }
    images_hours += write_code(image_code_template, dc)

    position_x += increment_2 - 5

    dc = {
        "X": position_x,
        "LABEL": "p"
    }
    label_hours += write_code(label_code_template, dc)

    image_source = rectangle_path + get_image_source(am_pm, "PM", filled_rectangle_name, outlined_rectangle_name)
    dc = {
        "X": position_x,
        "Y": position_y,
        "PATH": image_source
    }
    images_hours += write_code(image_code_template, dc)

    # Script for minute labels
    label_minutes = ""
    images_minutes = ""

    minutes = current_time.strftime("%M")
    minutes_0 = int(minutes[0])
    minutes_1 = int(minutes[1])

    position_x = -10
    position_x_image = -5
    position_y = 80
    
    for i in range(1, 6):
        position_x_image += increment_2
        position_x += increment_2

        dc = {
            "X": position_x,
            "LABEL": str(i) + "0"
        }
        label_minutes += write_code(label_code_template, dc)

        image_source = rectangle_path + get_image_source(minutes_0, i, filled_rectangle_name, outlined_rectangle_name)

        dc = {
            "X": position_x_image,
            "Y": position_y,
            "PATH": image_source
        }
        images_minutes += write_code(image_code_template, dc)

    for i in range(1, 10):
        if i == 1:
            position_x += increment_2
        else:
            position_x += increment_1

        dc = {
            "X": position_x,
            "LABEL": i
        }
        label_minutes += write_code(label_code_template, dc)

        image_source = rectangle_path + get_image_source(minutes_1, i, filled_rectangle_name, outlined_rectangle_name)
        dc = {
            "X": position_x,
            "Y": position_y,
            "PATH": image_source
        }
        images_minutes += write_code(image_code_template, dc)

    offset = "${voffset 5}"
    code = f"{template}{label_hours}\n{images_hours}\n{offset}{label_minutes}\n{images_minutes}"

    with open(clock_target, "w") as f:
        f.write(code)

    while minutes == datetime.now().strftime("%M"):
        time.sleep(5)
