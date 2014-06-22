#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string

rf = open('omuraisu_recipe_data.txt', 'r')

recipe_with_id = {}

id = 1
for recipes in rf.readlines():
	recipe_with_id['id'] = 'recipe' 
	print (id,recipes)
	id += 1

id_requested = input("type in the id you request > ")
print(recipe_with_id.get('id'))

