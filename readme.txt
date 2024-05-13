A pyqt5 "template app" for navigating through a tree of windows of short videos. Widget contents (button positions and text, paths to videos and images) are loaded from a sqlite database. 
This is a starter project intended for general reuse. Widgets' contents are created in the db_push.py script; app.py runs the UI. 

apt packages i installed to make this work include:

libpyside2-dev 
python3-pyside2.qtcore  
python3-pyside2.qtgui  
python3-pyside2.qtwidgets  
python3-pyqt5.qtmultimedia 
libgstreamer1.0-dev  
libgstreamer-plugins-base1.0-dev  
libgstreamer-plugins-good1.0-dev 
python3-sqlalchemy 



To use it,
cd to the project directory
if you don't have a "prompt_vid.db", run db_push.py
run app.py

How it works
The video and picture tables just save a path in the filesystem.
ContainerNode inherits from QStackedWidget; this allows "inner widgets" to be push'd and pop'd, in ContainerNode.replaceView. 
ContainerNode also keeps a "historyStack" of model id's. PromptNode.replaceWithParent gets its parent id from this stack, then fills in a widget by selecting details using this id as a primary and foreign key.
The ButtonLink table pairs every button id to the node id of its target.


--
To add a node
 in db_push.py,  
 create a new prompt_vid.NodeModel
 
  funNewNode = prompt_vid.NodeModel()
 
 you can use the NodeModel.setFromEntry method to set the node's attributes, including paths and window positions of its background picture(s), buttons, and videos
 
    funNewNode.setFromEntry(
        friendlyName = "fun new node",
        picInfo = [
            ],
        picButtonInfo = [
            {
                "text": "To main node", "path": "img/some_image.png",
                "linkname": "fun_main",
                "x": 450, "y": 5, "w":400, "h": 120
            },
        ],
        vidInfo = [
            {
                "path": "vid/some video.mkv",
                "x": 5, "y": 5, "w":412, "h": 240
            }
        ]
    )

 :

 commit the NodeModel to the sqlalchemy session
 
    session.add(funNewNode)
    session.commit()

 :

 create the new Node's PicButtons' links if it has buttons. (example assumes main node is in the same scope)
 inside the function 
 
    funLink = prompt_vid.ButtonLink(
        buttonId = session.query(prompt_vid.PicButtonModel).\
            filter(prompt_vid.PicButtonModel.nodeId==funNewNode.id,
                prompt_vid.PicButtonModel.linkname == "fun_main").\
            first().id,
        childNodeId = main.id
    )
    session.add(funLink)
    session.commit()

 :

 (link an existing node's PicButtonInfo to point to your new node)

 :

 delete prompt_vid.db and rerun db_push.py

