from Products.Archetypes.atapi import process_types, listTypes
from Products.CMFCore import utils, DirectoryView
from Products.SimpleAttachment.config import PROJECTNAME
from Products.SimpleAttachment.config import DEFAULT_ADD_CONTENT_PERMISSION

from zope.i18nmessageid import MessageFactory

SimpleAttachmentMessageFactory = MessageFactory('simpleattachment')

DirectoryView.registerDirectory('skins', globals())


def initialize(context):

    # Import the type, which results in registerType() being called
    from .content import FileAttachment, ImageAttachment
    FileAttachment, ImageAttachment     # make pyflakes happy :)

    # initialize the content, including types and add permissions
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types=content_types,
        permission=DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors=constructors,
        fti=ftis,
    ).initialize(context)
