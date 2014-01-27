from five import grok
from plone.directives import dexterity, form
from plone.indexer import indexer

from zope import schema
from plone.app.textfield import RichText

from shiji.content import MessageFactory as _


# Interface class; used to define content-type schema.

class IProposal(form.Schema):
    """
    ShiJi Proposal Type
    """
    
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/proposal.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/proposal.xml")

    title = schema.TextLine(
        title=_(u"Title"),
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    body = RichText(
        title=_(u"Body"),
        required=False,
    )


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Proposal(dexterity.Container):
    grok.implements(IProposal)
    
    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# proposal_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(IProposal)
    grok.require('zope2.View')
    grok.name('view')

