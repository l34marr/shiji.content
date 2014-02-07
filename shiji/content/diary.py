from five import grok
from plone.directives import form
from plone.dexterity.content import Item

from zope import schema
from plone.app.textfield import RichText
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from shiji.content import MessageFactory as _

duty = SimpleVocabulary([
    SimpleTerm(value=u'gw', title=_(u'GW')),
    SimpleTerm(value=u'sw', title=_(u'SW')),
    SimpleTerm(value=u'wk', title=_(u'WK')),
    SimpleTerm(value=u'hb', title=_(u'HB')),
    SimpleTerm(value=u'aq', title=_(u'AQ'))
])


# Interface class; used to define content-type schema.

class IDiary(form.Schema):
    """ShiJi Diary Type
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/proposal.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/diary.xml")

    title = schema.TextLine(
        title=_(u"Title"),
    )

    date = schema.Date(
        title=_(u"Date"),
        required=False,
    )

    duty = schema.List(
        title=_(u"Duty"),
        required=False,
        value_type=schema.Choice(
            vocabulary=duty,
        )
    )

    logistics = RichText(
        title=_(u"Logistics"),
        required=False,
    )

    security = RichText(
        title=_(u"Security"),
        required=False,
    )

    maintain = RichText(
        title=_(u"Maintain"),
        required=False,
    )

    hallwork = RichText(
        title=_(u"HallWork"),
        required=False,
    )

    absence = RichText(
        title=_(u"Absence"),
        required=False,
    )

    comment = RichText(
        title=_(u"Comment"),
        required=False,
    )

    residence = RichText(
        title=_(u"Residence"),
        required=False,
    )

    note = RichText(
        title=_(u"Note"),
        required=False,
    )


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Diary(Item):
    grok.implements(IDiary)
    
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
    grok.context(IDiary)
    grok.require('zope2.View')
    grok.name('view')

