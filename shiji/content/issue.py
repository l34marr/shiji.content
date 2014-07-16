from five import grok
from plone.directives import dexterity, form

from zope import schema
from plone.app.textfield import RichText
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

from shiji.content import MessageFactory as _

# Interface class; used to define content-type schema.

class IIssue(form.Schema):
    """
    ShiJi Issue Type
    """
    
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/issue.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/issue.xml")

    title = schema.TextLine(
        title=_(u"Title"),
    )

    spot = schema.Date(
        title=_(u"Spot Date"),
        required=False,
    )

    origin = schema.List(
        title=_(u"Origin"),
        required=False,
        value_type=schema.Choice(
            vocabulary='origin',
        )
    )

    form = schema.TextLine(
        title=_(u"Form Number"),
        required=False,
    )

    duty = schema.List(
        title=_(u"Duty"),
        required=False,
        value_type=schema.Choice(
            vocabulary='duty',
        )
    )

    description = schema.Text(
        title=_(u"Issue"),
        required=False,
    )

    body = RichText(
        title=_(u"Process"),
        required=False,
    )

    track = schema.Choice(
        title=_(u"Track"),
        required=False,
        vocabulary='track',
    )

    done = schema.Date(
        title=_(u"Done Date"),
        required=False,
    )

    in_charge = schema.Tuple(
        title=_(u"Persons in Charge"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )

    note = RichText(
        title=_(u"Note"),
        required=False,
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Issue(dexterity.Container):
    grok.implements(IIssue)
    
    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# issue_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(IIssue)
    grok.require('zope2.View')
    grok.name('view')

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None

