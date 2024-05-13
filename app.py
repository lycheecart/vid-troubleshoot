#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import prompt_vid

import sys, os
"""
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.phonon import Phonon
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    sqlite = create_engine('sqlite:///prompt_vid.db')
    Session = sessionmaker(bind=sqlite)
    session = Session()
    prompt_vid.Main().run(session)
