#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import prompt_vid

import sys, os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBFirm():
    def addBranchA(self, session, mainModelId):
        nodes = []

        nodeIA = prompt_vid.NodeModel()
        nodeIA.setFromEntry(
            friendlyName = "Name for node IA",
            picInfo = [
                {
                    "text": "", "path": "img/img_ia.png",
                    "x": 175, "y": 245, "w":90, "h":90 
                },
            ],
            picButtonInfo = [
                {
                    "text": "To IA1", "path": "img/placeholder.png",
                    "linkname": "IA1",
                    "x": 450, "y": 5, "w":400, "h": 120
                },
                {
                    "text": "To IA2", "path": "img/placeholder.png",
                    "linkname": "IA2",
                    "x": 450, "y": 130, "w":400, "h": 120
                },
                {
                    "text": "To IA3", "path": "img/placeholder.png",
                    "linkname": "IA3",
                    "x": 450, "y": 255, "w":400, "h": 120
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ia.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )


        nodeIA1 = prompt_vid.NodeModel()
        nodeIA1.setFromEntry(
            friendlyName = "Name for node IA1",
            picInfo = [ 
            ],
            picButtonInfo = [
                {
                    "text": "To IA1a", "path": "img/placeholder.png",
                    "linkname": "IA1a",
                    "x": 450, "y": 10, "w": 300, "h": 160
                },
                {
                    "text": "To IA1b", "path": "img/placeholder.png",
                    "linkname": "IA1b",
                    "x": 450, "y": 200, "w": 300, "h": 160
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ia1.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIA1a = prompt_vid.NodeModel()
        nodeIA1a.setFromEntry(
            friendlyName = "Name for node IA1a",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ia1a.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIA1b = prompt_vid.NodeModel()
        nodeIA1b.setFromEntry(
            friendlyName = "Name for node IA1b",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ia1b.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIA2 = prompt_vid.NodeModel()
        nodeIA2.setFromEntry(
            friendlyName = "Name for node IA2",
            picInfo = [ 
            ],
            picButtonInfo = [
                {
                    "text": "To IA2a", "path": "img/placeholder.png",
                    "linkname": "IA2a",
                    "x": 450, "y": 10, "w": 300, "h": 160
                },
                {
                    "text": "To IA2b", "path": "img/placeholder.png",
                    "linkname": "IA2b",
                    "x": 450, "y": 200, "w": 300, "h": 160
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ia2.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIA2a = prompt_vid.NodeModel()
        nodeIA2a.setFromEntry(
            friendlyName = "Name for node IA2a",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ia2a.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIA2b = prompt_vid.NodeModel()
        nodeIA2b.setFromEntry(
            friendlyName = "Name for node IA2b",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ia2b.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIA3 = prompt_vid.NodeModel()
        nodeIA3.setFromEntry(
            friendlyName = "Name for node IA3",
            picInfo = [ 
            ],
            picButtonInfo = [
                {
                    "text": "To IA3a", "path": "img/placeholder.png",
                    "linkname": "IA3a",
                    "x": 450, "y": 10, "w": 300, "h": 160
                },
                {
                    "text": "To IA3b", "path": "img/placeholder.png",
                    "linkname": "IA3b",
                    "x": 450, "y": 200, "w": 300, "h": 160
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ia3.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIA3a = prompt_vid.NodeModel()
        nodeIA3a.setFromEntry(
            friendlyName = "Name for node IA3a",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ia3a.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIA3b = prompt_vid.NodeModel()
        nodeIA3b.setFromEntry(
            friendlyName = "Name for node IA3b",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ia3b.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodes.append(nodeIA)
        nodes.append(nodeIA1)
        nodes.append(nodeIA1a)
        nodes.append(nodeIA1b)
        nodes.append(nodeIA2)
        nodes.append(nodeIA2a)
        nodes.append(nodeIA2b)
        nodes.append(nodeIA3)
        nodes.append(nodeIA3a)
        nodes.append(nodeIA3b)

        session.add_all(nodes)
        session.commit()

        links = [
            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==mainModelId, 
                        prompt_vid.PicButtonModel.linkname == "IA").\
                    first().id,
                childNodeId = nodeIA.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIA.id,
                        prompt_vid.PicButtonModel.linkname == "IA1").\
                    first().id,
                childNodeId = nodeIA1.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIA1.id,
                        prompt_vid.PicButtonModel.linkname == "IA1a").\
                    first().id,
                childNodeId = nodeIA1a.id
            ),
            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIA1.id,
                        prompt_vid.PicButtonModel.linkname == "IA1b").\
                    first().id,
                childNodeId = nodeIA1b.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIA.id,
                        prompt_vid.PicButtonModel.linkname == "IA2").\
                    first().id,
                childNodeId = nodeIA2.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIA2.id,
                        prompt_vid.PicButtonModel.linkname == "IA2a").\
                    first().id,
                childNodeId = nodeIA2a.id
            ),
            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIA2.id,
                        prompt_vid.PicButtonModel.linkname == "IA2b").\
                    first().id,
                childNodeId = nodeIA2b.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIA.id,
                        prompt_vid.PicButtonModel.linkname == "IA3").\
                    first().id,
                childNodeId = nodeIA3.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIA3.id,
                        prompt_vid.PicButtonModel.linkname == "IA3a").\
                    first().id,
                childNodeId = nodeIA3a.id
            ),
            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIA3.id,
                        prompt_vid.PicButtonModel.linkname == "IA3b").\
                    first().id,
                childNodeId = nodeIA3b.id
            ),
        ]

        session.add_all(links)
        session.commit()


    def addBranchB(self, session, mainModelId):
        nodes = []


        nodeIB = prompt_vid.NodeModel()
        nodeIB.setFromEntry(
            friendlyName = "Name for node IB",
            picInfo = [ 
                {
                    "text": "", "path": "img/img_ib.png",
                    "x": 175, "y": 245, "w":90, "h":90 
                },
            ],
            picButtonInfo = [
                {
                    "text": "To IB1", "path": "img/placeholder.png",
                    "linkname": "IB1",
                    "x": 450, "y": 10, "w": 300, "h": 160
                },
                {
                    "text": "To IB2", "path": "img/placeholder.png",
                    "linkname": "IB2",
                    "x": 450, "y": 200, "w": 300, "h": 160
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ib.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIB1 = prompt_vid.NodeModel()
        nodeIB1.setFromEntry(
            friendlyName = "Name for node IB1",
            picInfo = [ 
            ],
            picButtonInfo = [
                {
                    "text": "To IB1a", "path": "img/placeholder.png",
                    "linkname": "IB1a",
                    "x": 450, "y": 10, "w": 300, "h": 160
                },
                {
                    "text": "To IB1b", "path": "img/placeholder.png",
                    "linkname": "IB1b",
                    "x": 450, "y": 200, "w": 300, "h": 160
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ib1.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIB1a = prompt_vid.NodeModel()
        nodeIB1a.setFromEntry(
            friendlyName = "Name for node IB1a",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ib1a.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIB1b = prompt_vid.NodeModel()
        nodeIB1b.setFromEntry(
            friendlyName = "Name for node IB1b",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ib1b.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIB2 = prompt_vid.NodeModel()
        nodeIB2.setFromEntry(
            friendlyName = "Name for node IB2",
            picInfo = [ 
            ],
            picButtonInfo = [
                {
                    "text": "To IB2a", "path": "img/placeholder.png",
                    "linkname": "IB2a",
                    "x": 450, "y": 5, "w":400, "h": 120
                },
                {
                    "text": "To IB2b", "path": "img/placeholder.png",
                    "linkname": "IB2b",
                    "x": 450, "y": 130, "w":400, "h": 120
                },
                {
                    "text": "To IB2c", "path": "img/placeholder.png",
                    "linkname": "IB2c",
                    "x": 450, "y": 255, "w":400, "h": 120
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ib2.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIB2a = prompt_vid.NodeModel()
        nodeIB2a.setFromEntry(
            friendlyName = "Name for node IB2a",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ib2a.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIB2b = prompt_vid.NodeModel()
        nodeIB2b.setFromEntry(
            friendlyName = "Name for node IB2b",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ib2b.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIB2c = prompt_vid.NodeModel()
        nodeIB2c.setFromEntry(
            friendlyName = "Name for node IB2c",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ib2c.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodes.append(nodeIB)
        nodes.append(nodeIB1)
        nodes.append(nodeIB1a)
        nodes.append(nodeIB1b)
        nodes.append(nodeIB2)
        nodes.append(nodeIB2a)
        nodes.append(nodeIB2b)
        nodes.append(nodeIB2c)

        session.add_all(nodes)
        session.commit()

        links = [
            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==mainModelId, 
                        prompt_vid.PicButtonModel.linkname == "IB").\
                    first().id,
                childNodeId = nodeIB.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIB.id,
                        prompt_vid.PicButtonModel.linkname == "IB1").\
                    first().id,
                childNodeId = nodeIB1.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIB1.id,
                        prompt_vid.PicButtonModel.linkname == "IB1a").\
                    first().id,
                childNodeId = nodeIB1a.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIB1.id,
                        prompt_vid.PicButtonModel.linkname == "IB1b").\
                    first().id,
                childNodeId = nodeIB1b.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIB.id,
                        prompt_vid.PicButtonModel.linkname == "IB2").\
                    first().id,
                childNodeId = nodeIB2.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIB2.id,
                        prompt_vid.PicButtonModel.linkname == "IB2a").\
                    first().id,
                childNodeId = nodeIB2a.id
            ),
            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIB2.id,
                        prompt_vid.PicButtonModel.linkname == "IB2b").\
                    first().id,
                childNodeId = nodeIB2b.id
            ),
            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIB2.id,
                        prompt_vid.PicButtonModel.linkname == "IB2c").\
                    first().id,
                childNodeId = nodeIB2c.id
            ),
        ]

        session.add_all(links)
        session.commit()


    def addBranchC(self, session, mainModelId):
        nodes = []

        nodeIC = prompt_vid.NodeModel()
        nodeIC.setFromEntry(
            friendlyName = "Name for node IC",
            picInfo = [ 
                {
                    "text": "", "path": "img/img_ic.png",
                    "x": 175, "y": 245, "w":90, "h":90 
                },
            ],
            picButtonInfo = [
                {
                    "text": "To IC1", "path": "img/placeholder.png",
                    "linkname": "IC1",
                    "x": 450, "y": 10, "w": 300, "h": 160
                },
                {
                    "text": "To IC2", "path": "img/placeholder.png",
                    "linkname": "IC2",
                    "x": 450, "y": 200, "w": 300, "h": 160
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ic.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIC1 = prompt_vid.NodeModel()
        nodeIC1.setFromEntry(
            friendlyName = "Name for node IC1",
            picInfo = [ 
            ],
            picButtonInfo = [
                {
                    "text": "To IC1a", "path": "img/placeholder.png",
                    "linkname": "IC1a",
                    "x": 450, "y": 10, "w": 300, "h": 160
                },
                {
                    "text": "To IC1b", "path": "img/placeholder.png",
                    "linkname": "IC1b",
                    "x": 450, "y": 200, "w": 300, "h": 160
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ic1.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIC1a = prompt_vid.NodeModel()
        nodeIC1a.setFromEntry(
            friendlyName = "Name for node IC1a",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ic1a.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIC1b = prompt_vid.NodeModel()
        nodeIC1b.setFromEntry(
            friendlyName = "Name for node IC1b",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ic1b.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIC2 = prompt_vid.NodeModel()
        nodeIC2.setFromEntry(
            friendlyName = "Name for node IC2",
            picInfo = [ 
            ],
            picButtonInfo = [
                {
                    "text": "To IC2a", "path": "img/placeholder.png",
                    "linkname": "IC2a",
                    "x": 450, "y": 200, "w": 300, "h": 160
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ic2.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIC2a = prompt_vid.NodeModel()
        nodeIC2a.setFromEntry(
            friendlyName = "Name for node IC2a",
            picInfo = [ 
            ],
            picButtonInfo = [
                {
                    "text": "To IC2ai", "path": "img/placeholder.png",
                    "linkname": "IC2ai",
                    "x": 450, "y": 10, "w":170, "h": 160
                },
                {
                    "text": "To IC2aii", "path": "img/placeholder.png",
                    "linkname": "IC2aii",
                    "x": 625, "y": 10, "w":170, "h": 160
                },
                {
                    "text": "To IC2aiii", "path": "img/placeholder.png",
                    "linkname": "IC2aiii",
                    "x": 450, "y": 200, "w":170, "h": 160
                },
                {
                    "text": "To IC2aiv", "path": "img/placeholder.png",
                    "linkname": "IC2aiv",
                    "x": 625, "y": 200, "w":170, "h": 160
                },
            ],
            vidInfo = [
                {
                    "path": "vid/ic2a.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIC2ai = prompt_vid.NodeModel()
        nodeIC2ai.setFromEntry(
            friendlyName = "Name for node IC12ai",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ic2ai.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIC2aii = prompt_vid.NodeModel()
        nodeIC2aii.setFromEntry(
            friendlyName = "Name for node IC12aii",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ic2aii.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIC2aiii = prompt_vid.NodeModel()
        nodeIC2aiii.setFromEntry(
            friendlyName = "Name for node IC12aiii",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ic2aiii.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodeIC2aiv = prompt_vid.NodeModel()
        nodeIC2aiv.setFromEntry(
            friendlyName = "Name for node IC12aiv",
            picInfo = [ 
            ],
            picButtonInfo = [
            ],
            vidInfo = [
                {
                    "path": "vid/ic2aiv.webm",
                    "x": 5, "y": 5, "w":412, "h": 240
                },
            ]
        )

        nodes.append(nodeIC)
        nodes.append(nodeIC1)
        nodes.append(nodeIC1a)
        nodes.append(nodeIC1b)
        nodes.append(nodeIC2)
        nodes.append(nodeIC2a)
        nodes.append(nodeIC2ai)
        nodes.append(nodeIC2aii)
        nodes.append(nodeIC2aiii)
        nodes.append(nodeIC2aiv)

        session.add_all(nodes)
        session.commit()

        links = [
            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==mainModelId, 
                        prompt_vid.PicButtonModel.linkname == "IC").\
                    first().id,
                childNodeId = nodeIC.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIC.id,
                        prompt_vid.PicButtonModel.linkname == "IC1").\
                    first().id,
                childNodeId = nodeIC1.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIC1.id,
                        prompt_vid.PicButtonModel.linkname == "IC1a").\
                    first().id,
                childNodeId = nodeIC1a.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIC1.id,
                        prompt_vid.PicButtonModel.linkname == "IC1b").\
                    first().id,
                childNodeId = nodeIC1b.id
            ),


            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIC.id,
                        prompt_vid.PicButtonModel.linkname == "IC2").\
                    first().id,
                childNodeId = nodeIC2.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIC2.id,
                        prompt_vid.PicButtonModel.linkname == "IC2a").\
                    first().id,
                childNodeId = nodeIC2a.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIC2a.id,
                        prompt_vid.PicButtonModel.linkname == "IC2ai").\
                    first().id,
                childNodeId = nodeIC2ai.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIC2a.id,
                        prompt_vid.PicButtonModel.linkname == "IC2aii").\
                    first().id,
                childNodeId = nodeIC2aii.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIC2a.id,
                        prompt_vid.PicButtonModel.linkname == "IC2aiii").\
                    first().id,
                childNodeId = nodeIC2aiii.id
            ),

            prompt_vid.ButtonLink(
                buttonId = session.query(prompt_vid.PicButtonModel).\
                    filter(prompt_vid.PicButtonModel.nodeId==nodeIC2a.id,
                        prompt_vid.PicButtonModel.linkname == "IC2aiv").\
                    first().id,
                childNodeId = nodeIC2aiv.id
            ),

        ]

        session.add_all(links)
        session.commit()


if __name__ == "__main__":
    sqlite = create_engine("sqlite:///prompt_vid.db")
    Session = sessionmaker(bind=sqlite)
    session = Session()

    main = prompt_vid.NodeModel()
    main.setFromEntry(
        friendlyName = "main",
        picInfo = [
            ],
        picButtonInfo = [
            {
                "text": "To Node IA", "path": "img/placeholder.png",
                "linkname": "IA",
                "x": 450, "y": 5, "w":400, "h": 120
            },
            {
                "text": "To Node IB", "path": "img/placeholder.png",
                "linkname": "IB",
                "x": 450, "y": 130, "w":400, "h": 120
            },
            {
                "text": "To Node IC", "path": "img/placeholder.png",
                "linkname": "IC",
                "x": 450, "y": 255, "w":400, "h": 120
            },
        ],
        vidInfo = [
            {
                "path": "vid/main.webm",
                "x": 5, "y": 5, "w":412, "h": 240
            }
        ]
    )


    session.add(main)
    session.commit()

    dbFirm = DBFirm()
    dbFirm.addBranchA(session, main.id)
    dbFirm.addBranchB(session, main.id)
    dbFirm.addBranchC(session, main.id)
