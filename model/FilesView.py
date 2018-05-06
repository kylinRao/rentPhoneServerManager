#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 21:46
# @Author  : Aries
# @Site    : 
# @File    : FilesView.py
# @Software: PyCharm
import os

from flask import send_from_directory, request,abort
from flask_admin import BaseView, expose
STATIC_FILES_DIR = 'static/files'

class FilesView(BaseView):

    @expose('/',methods=('GET', 'POST'))
    def download(self):
        for currentDir,b,files in os.walk(STATIC_FILES_DIR):
            return self.render("download.html",files=files)
    @expose('/downloadFile',methods=('GET', 'POST'))
    def downloadFile(self):
        filename = request.args.get('filename')
        if os.path.isfile(os.path.join(STATIC_FILES_DIR, filename)):
            return send_from_directory(STATIC_FILES_DIR,filename,as_attachment=True)
        abort(404)