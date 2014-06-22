#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string

rf = open('omuraisu_recipe_data.txt', 'r')

id = 1
for recipes in rf.readlines():
	print (id,recipes)
	id += 1
