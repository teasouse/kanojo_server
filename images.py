#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'Andrey Derevyagin'
__copyright__ = 'Copyright © 2014'

from PIL import Image
import json
import requests
try:
    from gdrive_cdn import UploadToCDN
except ImportError as e:
    pass
import io


class UploadToDeviantsart(object):
    def __init__(self):
        super(UploadToDeviantsart, self).__init__()

    def upload(self, content, content_type='image/jpeg', filename='image.jpg'):
        r = requests.post('http://deviantsart.com', files={'file': (filename, content, content_type)})
        try:
            rv = json.loads(r.text)
        except ValueError:
            return False
        return rv.get('url', False)



class ImageManager(object):
    def __init__(self):
        super(ImageManager, self).__init__()

    def upload(self, image_data, content_type='image/jpeg', filename='image.jpg'):
        return UploadToDeviantsart().upload(image_data, content_type, filename)

    def upload_user_profile_image(self, img_data, filename='image.jpg'):
        try:
            cdn = UploadToCDN()
        except NameError as e:
            cdn = UploadToDeviantsart()
        im = Image.open(img_data)
        (width, height) = im.size
        if width > 200 or height > 200:
            im.thumbnail((200, 200), Image.ANTIALIAS)
        dt = io.StringIO()
        im.save(dt, format="JPEG", quality=95)
        url = cdn.upload(dt.getvalue(), content_type='image/jpeg', filename=filename)
        dt.close()
        return url

    def crop_and_upload_profile_image(self, img_data, filename='kanojo', upload_full_image=True):
        try:
            cdn = UploadToCDN()
        except NameError as e:
            cdn = UploadToDeviantsart()
        im = Image.open(img_data)
        cr = im.crop((94, 40, 170+94, 170+40))
        cr.thumbnail((88, 88), Image.ANTIALIAS)
        dt = io.StringIO()
        cr.save(dt, format="png")
        crop_url = cdn.upload(dt.getvalue(), content_type='image/png', filename='%ss.png'%filename)
        dt.close()

        full_url = None
        if cdn and upload_full_image:
            dt = io.StringIO()
            im.save(dt, format="png")
            full_url = cdn.upload(dt.getvalue(), content_type='image/png', filename='%s.png'%filename)
            dt.close()
        return (crop_url, full_url)


if __name__=='__main__':
    im = Image.open('1.png')
    #im = Image.open(StringIO.StringIO(buffer))
    cr = im.crop((94, 40, 170+94, 170+40))
    cr.thumbnail((88, 88), Image.ANTIALIAS)
    dt = io.StringIO()
    cr.save(dt, format="png")
    crop_url = UploadToCDN().upload(dt.getvalue(), content_type='image/png', filename='best_girl.png')
    #crop_url = UploadToDeviantsart().upload(dt.getvalue(), content_type='image/png')
    dt.close()

    full_url = None
    try:
        cdn = UploadToCDN()
    except NameError as e:
        cdn = None
    if cdn:
        dt = io.StringIO()
        im.save(dt, format="png")
        full_url = UploadToCDN().upload(dt.getvalue(), content_type='image/png', filename='fk.png')
        dt.close()
    print(crop_url, full_url)