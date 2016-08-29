#!/usr/bin/env python3
import sys

sys.path.append("../pa_tools")

import mod_generator

mod_generator.run("src/mod.json")

# now we also generate that compatiblity mod for weapons tracking.

targets = [
	'pa*/ammo/**/*.json',
	'pa*/units/**/*_ammo*.json',
	'pa*/units/**/*_deploy.json',
	'pa*/units/**/torpedeo.json',
	'pa*/units/land/artillery_short/artillery_short_tool_weapon.json',
	'pa_ex1/units/land/artillery_unit_launcher/artillery_unit_launcher_tool_weapon.json'
]

import os
from os.path import join
from glob import glob

for target in targets:
	path = join('.', target)
	for file in glob(path):
		print (path)
