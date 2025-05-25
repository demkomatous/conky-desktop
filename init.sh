#!/bin/bash

# path="file:///home"
# Try to set the wallpaper using gsettings not working
# gsettings set org.gnome.desktop.background picture-uri "$path"

home=$(pwd)
config_template_path="$home/Code_templates/config_template.json"

config_template=$(<"$config_template_path")
config="${config_template//#HOME_DIRECTORY/$home}"

echo "$config" > "$home/config.json"

python3 "$home/Shapes/rectangles.py"
python3 "$home/init.py"
chmod +x autostart