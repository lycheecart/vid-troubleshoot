#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import sys, os
import subprocess
import enum 
from PyQt5.QtCore import Qt, QUrl, QSize
from PyQt5.QtWidgets import (QApplication, QStackedWidget, QVBoxLayout, QPushButton, QWidget)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, backref, relationship

qtApp = QApplication(sys.argv)
Base = declarative_base()

class NodeModel(Base):
    __tablename__ = "PromptNodes"
    id = Column(Integer(), primary_key=True)
    friendlyName = Column(String(255))
    pics       = relationship("PicModel", back_populates = "node")
    vids       = relationship("VidModel", back_populates = "node")
    picButtons = relationship("PicButtonModel", back_populates = "node")

    def setFromEntry(self, friendlyName = "", picInfo = [], picButtonInfo = [], vidInfo = []):
        self.friendlyName = friendlyName

        for p in picInfo:
            self.pics.append(PicModel(
                path = os.path.join(os.path.dirname(__file__), p["path"]), 
                text = p["text"], 
                geometryX = p["x"], geometryY = p["y"], 
                geometryW = p["w"], geometryH = p["h"]
                ))

        for p in picButtonInfo:
            self.picButtons.append(PicButtonModel(
                path = os.path.join(os.path.dirname(__file__), p["path"]), 
                text = p["text"],
                linkname = p["linkname"],
                geometryX = p["x"], geometryY = p["y"], 
                geometryW = p["w"], geometryH = p["h"]
                ))

        for p in vidInfo:
            self.vids.append(VidModel(
                path = os.path.join(os.path.dirname(__file__), p["path"]),
                geometryX = p["x"], geometryY = p["y"], 
                geometryW = p["w"], geometryH = p["h"]
                ))



class PicButtonModel(Base):
    __tablename__ = "PicButtons"
    id = Column(Integer(), primary_key=True)
    nodeId = Column(Integer(), ForeignKey("PromptNodes.id"))
    path = Column(String(4096), default = "")
    text = Column(String(4096), default = "")
    linkname = Column(String(4096), default = "")
    node = relationship("NodeModel", back_populates = "picButtons") 
    geometryX = Column(Integer())
    geometryY = Column(Integer())
    geometryW = Column(Integer())
    geometryH = Column(Integer())

class PicModel(Base):
    __tablename__ = "Pics"
    id = Column(Integer(), primary_key=True)
    nodeId = Column(Integer(), ForeignKey("PromptNodes.id"))
    path = Column(String(4096), default = "")
    text = Column(String(4096), default = "")
    node = relationship("NodeModel", back_populates = "pics")
    geometryX = Column(Integer())
    geometryY = Column(Integer())
    geometryW = Column(Integer())
    geometryH = Column(Integer())

class VidModel(Base):
    __tablename__ = "Vids"
    id = Column(Integer(), primary_key=True)
    nodeId = Column(Integer(), ForeignKey("PromptNodes.id"))
    path = Column(String(4096), default = "")
    node = relationship("NodeModel", back_populates = "vids")
    geometryX = Column(Integer())
    geometryY = Column(Integer())
    geometryW = Column(Integer())
    geometryH = Column(Integer())

class ButtonLink(Base):
    __tablename__ = "ButtonLinks"
    id = Column(Integer(), primary_key=True)
    buttonId = Column(Integer(), default=None)
    childNodeId = Column(Integer(), default=None)

sqlite = create_engine('sqlite:///prompt_vid.db')
Base.metadata.create_all(sqlite)

class VidWidg(QWidget):
    def __init__(self, parent, modelId = None, filename="vid.webm",
                 geoX = 0, geoY = 0, geoW = 400, geoH = 280):
        QWidget.__init__(self, parent)
        self.setGeometry(geoX, geoY, geoW, geoH)
        self.file_path = os.path.join(os.path.dirname(__file__), filename)
        self.modelId = modelId

        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.playlist = QMediaPlaylist()
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        url = QUrl.fromLocalFile(self.file_path)
        self.playlist.addMedia(QMediaContent(url))
        self.player.setPlaylist(self.playlist)
        self.player.setVideoOutput(videoWidget)
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        self.setLayout(layout)

    def play(self):
        self.player.play()

    def stop(self):
        self.player.stop()

class PromptButton(QPushButton):
    def __init__(self, parent, modelId = None, clickable=False, session = None, 
    txt = "", imgPath = "", geoX = 0, geoY = 0, geoW = 180, geoH = 180
    ):
        QPushButton.__init__(self, parent)
        self.parent = parent
        self.clickable = clickable

        self.file_path = os.path.join(os.path.dirname(__file__), imgPath)
        self.session = session
        self.modelId = modelId

        ss = ""
        ss += ".PromptButton {"
        ss += "background-image: url('" + self.file_path + "'); "
        ss += "border: none; "
        ss += "} "
        
        self.setStyleSheet(ss)
        self.setText(txt)
        self.setGeometry(geoX, geoY, geoW, geoH)

        self.clicked.connect(lambda: self.foo())

    def foo(self):
        print(self.text() + " clicked")

        if self.clickable:
            node = PromptNode(session=self.session)
            childIdSubq = self.session.query(ButtonLink.childNodeId).\
                filter(ButtonLink.buttonId == self.modelId).\
                scalar()

            node.setFromModel(self.session.query(NodeModel).\
                filter_by(id=childIdSubq).\
                one())

            container.historyStack.append(container.currentWidget().model.id)
            self.parent.stop()
            container.replaceView(node)

class PromptNode(QWidget):
    def __init__(self, parent = None, pName = "", session = None, picInfo = [], picButtonInfo = [], vidInfo = []):
        QWidget.__init__(self, parent)
        self.parent = parent
        self.picWidgets = []
        self.picButtonWidgets = []
        self.vidWidgets = []
        self.session = session 

        if pName != "":
            self.model = NodeModel(
                friendlyName = pName
            )
            for p in picInfo:
                self.model.pics.append(PicModel(
                    path = os.path.join(os.path.dirname(__file__), p["path"]), 
                    text = p["text"], 
                    geometryX = p["x"], geometryY = p["y"], 
                    geometryW = p["w"], geometryH = p["h"]
                    ))

                self.picWidgets.append(PromptButton(self, 
                    session=session, clickable=False, txt=p["text"], imgPath=p["path"], 
                    geoX = p["x"], geoY = p["y"], geoW = p["w"], geoH = p["h"]
                    ))

            for p in picButtonInfo:
                self.model.picButtons.append(PicButtonModel(
                    path = os.path.join(os.path.dirname(__file__), p["path"]), 
                    text = p["text"],
                    linkname = p["linkname"],
                    geometryX = p["x"], geometryY = p["y"], 
                    geometryW = p["w"], geometryH = p["h"]
                    ))
                self.picButtonWidgets.append(PromptButton(self, 
                    session=session, clickable=True, txt=p["text"], imgPath=p["path"], 
                    geoX = p["x"], geoY = p["y"], geoW = p["w"], geoH = p["h"]
                    ))

            for p in vidInfo:
                self.model.vids.append(VidModel(
                    path = os.path.join(os.path.dirname(__file__), p["path"]),
                    geometryX = p["x"], geometryY = p["y"], 
                    geometryW = p["w"], geometryH = p["h"]
                    ))

                self.vidWidgets.append(VidWidg(self, filename=p["path"],
                    geoX = p["x"], geoY = p["y"], geoW = p["w"], geoH = p["h"]
                ))
            self.setupGraphics()

    def setFromModel(self, model): #python doesn't support multiple constructors
        self.model = model
        for w in model.pics:
            self.picWidgets.append(PromptButton(
                self, modelId = w.id, session = self.session, 
                clickable=False,
                txt=w.text, imgPath=w.path, 
                geoX = w.geometryX, geoY = w.geometryY, geoW = w.geometryW, geoH = w.geometryH
            ))
        for w in model.picButtons:
            self.picButtonWidgets.append(PromptButton(
                self, modelId = w.id, session = self.session, 
                clickable=True,
                txt=w.text, imgPath=w.path,
                geoX = w.geometryX, geoY = w.geometryY, geoW = w.geometryW, geoH = w.geometryH
            ))
        for w in model.vids:
            self.vidWidgets.append(
                VidWidg(self, modelId = w.id, filename=w.path,
                geoX = w.geometryX, geoY = w.geometryY, 
                geoW = w.geometryW, geoH = w.geometryH
            ))
        self.setupGraphics()

    def setupGraphics(self):
        self.setMinimumSize(QSize(800, 400))

        backText = "(Back)"
        backPath = "img/meta/back.png"

        topText = "(Home screen)"
        topPath = "img/meta/top.png"

        backButton = PromptButton(self, session = self.session, txt=backText, imgPath=backPath)
        topButton  = PromptButton(self, session = self.session, txt=topText, imgPath=topPath)

        backButton.foo = self.replaceWithParent
        topButton.foo  = self.replaceWithHome

        backButton.setGeometry(10, 355, 100, 40)
        topButton.setGeometry(115, 355, 100, 40)

    def replaceWithParent(self):
        if (self.model.friendlyName == "main"):
            return

        parent = PromptNode(session = self.session)
        parentId = container.historyStack.pop()

        parent.setFromModel(self.session.query(NodeModel).\
            filter_by(id=parentId).\
            one())
        container.replaceView(parent)

    def replaceWithHome(self):
        node = PromptNode(session=self.session)
        node.setFromModel(self.session.query(NodeModel).\
            filter_by(friendlyName="main").\
            one())
        container.historyStack[:] = []
        container.replaceView(node)

    def dbPush(self, sesh):
        sesh.add(self.model)
        sesh.commit()

    def stop(self):
        for v in self.vidWidgets:
            v.stop()

    def play(self):
        for v in self.vidWidgets:
            v.play()

class ContainerNode(QStackedWidget):
    def __init__(self):
        QStackedWidget.__init__(self)
        self.historyStack = []

    def runMain(self):
        self.show()
        qtApp.exec_()

    def replaceView(self, w):
        c = self.count()
        for i in range(c, 0, -1):
            d = self.widget(i)
            if d is not None:
                d.stop()
                self.removeWidget(d)
                d.deleteLater()

        self.addWidget(w)
        self.setCurrentWidget(w) 
        w.show()
        w.play()

    def closeEvent(self, event):
        event.accept()
        QApplication.quit()
        sys.exit()

container = ContainerNode()

class Main():
    def run(self, sesh):
        mainModel = sesh.query(NodeModel).filter_by(friendlyName="main").one()
        mainNode  = PromptNode(parent = container, session = sesh)
        mainNode.setFromModel(mainModel)

        container.addWidget(mainNode)
        container.replaceView(mainNode)
        container.runMain()

