#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Andrey Derevyagin'
__copyright__ = 'Copyright © 2014'

import io

from PIL import Image

def save_image(content, filename='image.png'):
	with open(filename, 'bw') as f:
		f.write(content)
	return filename

#For User
def save_profile_image(img_data, filename):
	im = Image.open(img_data)
	(width, height) = im.size
	if width > 200 or height > 200:
		im = im.resize((200, 200), resample=Image.LANCZOS)
	dt = io.BytesIO()
	im.save(dt, format="JPEG", quality=100)
	save_image(dt.getvalue(), filename=f'{filename}.jpg')
	dt.close()

#For Kanojo
def crop_and_save_profile_image(img_data, destination):
	im = Image.open(img_data)
	#cr = im.crop((94, 40, 170 + 94, 170 + 40))	#Original face from 368
	#cr = im.crop((im.width * 0.25543, im.width * 0.108, im.width * 0.71739, im.width * 0.570))	#Old Face
	cr = im.crop((im.width * 0.27173, im.width * 0.10869, im.width * 0.72826, im.width * 0.56521))
	#cr.thumbnail((88, 88), Image.ANTIALIAS)
	dt = io.BytesIO()
	cr.save(dt, format="png")
	save_image(dt.getvalue(), filename=f'{destination}/icon.png')
	dt.close()

	cr = im.crop((im.width*0.25, im.width*0.09, im.width*0.75, im.width*0.59))	#Good for bust image (v1 style)
	dt = io.BytesIO()
	cr.save(dt, format="png")
	save_image(dt.getvalue(), filename=f'{destination}/iconv1.png')
	dt.close()

	dt = io.BytesIO()
	im.save(dt, format="png")
	save_image(dt.getvalue(), filename=f'{destination}/full.png')
	dt.close()

def save_resized_image(filename, size):
	im = Image.open(filename+'.png')
	rs = im.resize((size, size), resample=Image.LANCZOS)
	dt = io.BytesIO()
	rs.save(dt, format="png")
	save_image(dt.getvalue(), filename=f'{filename}_{size}.png')
	dt.close()

if __name__=='__main__':
	im = Image.open('1.png')
	#im = Image.open(StringIO.StringIO(buffer))
	cr = im.crop((94, 40, 170+94, 170+40))
	cr.thumbnail((88, 88), Image.ANTIALIAS)
	dt = io.StringIO()
	cr.save(dt, format="png")
	save_image(dt.getvalue(), filename='best_girl.png')
	dt.close()

	dt = io.StringIO()
	im.save(dt, format="png")
	save_image(dt.getvalue(), filename='fk.png')
	dt.close()