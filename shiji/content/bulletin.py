from five import grok
from plone.directives import form
from plone.dexterity.content import Item
from plone.app.contenttypes.interfaces import IFile

from zope import schema
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobFile
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from shiji.content import MessageFactory as _

duty = SimpleVocabulary([
    SimpleTerm(value=u'gw', title=_(u'GW')),
    SimpleTerm(value=u'sw', title=_(u'SW')),
    SimpleTerm(value=u'wk', title=_(u'WK')),
    SimpleTerm(value=u'hb', title=_(u'HB')),
    SimpleTerm(value=u'aq', title=_(u'AQ'))
])

building = SimpleVocabulary([
    SimpleTerm(value='J', title=_(u'J')),
    SimpleTerm(value='K', title=_(u'K')),
    SimpleTerm(value='L', title=_(u'L')),
    SimpleTerm(value='M', title=_(u'M')),
    SimpleTerm(value='N', title=_(u'N')),
    SimpleTerm(value='O', title=_(u'O')),
    SimpleTerm(value='P', title=_(u'P')),
    SimpleTerm(value='Q', title=_(u'Q'))
])

# Interface class; used to define content-type schema.

class IBulletin(form.Schema):
    """ShiJi Bulletin Type
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/proposal.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/bulletin.xml")

    start = schema.Date(
        title=_(u"Start Date"),
        required=False,
    )

    end = schema.Date(
        title=_(u"End Date"),
        required=False,
    )

    duty = schema.List(
        title=_(u"Duty"),
        required=False,
        value_type=schema.Choice(
            vocabulary=duty,
        )
    )

    building = schema.List(
        title=_(u"Building"),
        required=False,
        value_type=schema.Choice(
            vocabulary=building,
        )
    )

    note = RichText(
        title=_(u"Note"),
        required=False,
    )

    searchable = schema.Text(
        title=_(u"Searchable Text"),
        required=False,
    )

    form.primary('file')
    file = NamedBlobFile(
        title=_(u"File"),
        required=False,
    )
    
# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Bulletin(Item):
    grok.implements(IBulletin, IFile)
    
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
    grok.context(IBulletin)
    grok.require('zope2.View')
    grok.name('view')

