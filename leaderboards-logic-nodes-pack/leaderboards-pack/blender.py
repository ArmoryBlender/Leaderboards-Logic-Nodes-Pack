import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class AddScore(ArmLogicTreeNode):
    """Add Score"""
    bl_idname = 'LNAddScore'
    bl_label = 'Add Score'

    # Use this as a tooltip in the add node menu.
    # If `bl_description` does not exist, the docstring of this node is used instead.
    bl_description = 'Adding score'

    # The category in which this node is listed in the user interface
    arm_category = 'Leaderboards'

    # Set the version of this node. If you update the node's Python
    # code later, increment this version so that older projects get
    # updated automatically.
    # See https://github.com/armory3d/armory/wiki/logicnodes#node-versioning
    arm_version = 0

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')

        self.add_input('ArmStringSocket', 'Name')

        self.add_input('ArmIntSocket', 'Score')


        self.add_output('ArmNodeSocketAction', 'Out')

class GetScore(ArmLogicTreeNode):
    """Get Score"""
    bl_idname = 'LNGetScore'
    bl_label = 'Get Score'

    # Use this as a tooltip in the add node menu.
    # If `bl_description` does not exist, the docstring of this node is used instead.
    bl_description = 'Getting score'

    # The category in which this node is listed in the user interface
    arm_category = 'Leaderboards'

    # Set the version of this node. If you update the node's Python
    # code later, increment this version so that older projects get
    # updated automatically.
    # See https://github.com/armory3d/armory/wiki/logicnodes#node-versioning
    arm_version = 0

    def init(self, context):
        self.add_output('ArmStringSocket', 'Name')

        self.add_output('ArmIntSocket', 'Score')

class ResetScore(ArmLogicTreeNode):
    """Reset Score"""
    bl_idname = 'LNResetScore'
    bl_label = 'Reset Score'

    # Use this as a tooltip in the add node menu.
    # If `bl_description` does not exist, the docstring of this node is used instead.
    bl_description = 'Reset score'

    # The category in which this node is listed in the user interface
    arm_category = 'Leaderboards'

    # Set the version of this node. If you update the node's Python
    # code later, increment this version so that older projects get
    # updated automatically.
    # See https://github.com/armory3d/armory/wiki/logicnodes#node-versioning
    arm_version = 0

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')

        self.add_output('ArmNodeSocketAction', 'Out')


def register():
    """This function is called when Armory loads this library."""

    # Add a new category of nodes in which we will put the TestNode.
    # This step is optional, you can also add nodes to Armory's default
    # categories.
    add_category('Leaderboards', icon='PLAY')

    # Register the TestNode
    AddScore.on_register()
    GetScore.on_register()
    ResetScore.on_register()
