from Qt import QtWidgets

from PyFlow.UI.Canvas.UINodeBase import UINodeBase
from PyFlow.UI.Canvas.UINodeBase import getUINodeInstance
from PyFlow.Core.Common import *


class UICompoundNode(UINodeBase):
    def __init__(self, raw_node):
        super(UICompoundNode, self).__init__(raw_node)

    def updateSize(self, name):
        self.updateWidth()
        self.updateNodeShape()

    def onGraphInputPinExposed(self, rawPin):
        # create ui wrapper for raw exposed pin
        # and connect signals
        uiCompanionPin = self._createUIPinWrapper(rawPin)

    def serialize(self):
        default = super(UICompoundNode, self).serialize()

        return default

    def onGraphOutputPinExposed(self, rawPin):
        uiCompanionPin = self._createUIPinWrapper(rawPin)

    def mouseDoubleClickEvent(self, event):
        self._rawNode.graph().graphManager.selectGraph(self.name)
        event.accept()

    def kill(self, *args, **kwargs):
        super(UICompoundNode, self).kill()

    def onGraphNameChanged(self, newName):
        self.displayName = newName
        self.name = newName

    def postCreate(self, jsonTemplate=None):
        super(UICompoundNode, self).postCreate(jsonTemplate)
        self.canvasRef().createWrappersForGraph(self._rawNode.rawGraph)
        self._rawNode.rawGraph.nameChanged.connect(self.onGraphNameChanged)
