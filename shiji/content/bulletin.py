# -*- coding: utf-8 -*-

from five import grok
from plone.directives import form
from plone.dexterity.content import Item
from plone.app.contenttypes.interfaces import IFile

from zope import schema
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobFile
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

from shiji.content import MessageFactory as _

area = SimpleVocabulary([
    SimpleTerm(value=u'KTV', token='ktv', title=u'KTV'),
    SimpleTerm(value=u'\u4e09\u6eab\u6696', token='swn', title=u'\u4e09\u6eab\u6696'),
    SimpleTerm(value=u'\u4ea4\u8abc\u5ef3', token='jyt', title=u'\u4ea4\u8abc\u5ef3'),
    SimpleTerm(value=u'\u5152\u7ae5\u904a\u6232\u5ba4', token='etyxs',title=u'\u5152\u7ae5\u904a\u6232\u5ba4'),
    SimpleTerm(value=u'\u5152\u7ae5\u904a\u6232\u5340', token='etyxq',title=u'\u5152\u7ae5\u904a\u6232\u5340'),
    SimpleTerm(value=u'\u5152\u7ae5\u95b1\u89bd\u5ba4', token='etyls',title=u'\u5152\u7ae5\u95b1\u89bd\u5ba4'),
    SimpleTerm(value=u'\u5bb4\u6703\u5ef3', token='yht', title=u'\u5bb4\u6703\u5ef3'),
    SimpleTerm(value=u'\u684c\u7403\u5ba4', token='tbltns', title=u'\u684c\u7403\u5ba4'),
    SimpleTerm(value=u'\u5065\u8eab\u623f', token='jsf', title=u'\u5065\u8eab\u623f'),
    SimpleTerm(value=u'\u6e38\u6cf3\u6c60', token='yyc', title=u'\u6e38\u6cf3\u6c60'),
    SimpleTerm(value=u'\u8996\u807d\u5ba4', token='sts', title=u'\u8996\u807d\u5ba4'),
    SimpleTerm(value=u'\u5716\u66f8\u9928', token='tsg', title=u'\u5716\u66f8\u9928'),
    SimpleTerm(value=u'\u649e\u7403\u5ba4', token='snooker', title=u'\u649e\u7403\u5ba4'),
    SimpleTerm(value=u'\u97fb\u5f8b\u6559\u5ba4', token='yljs', title=u'\u97fb\u5f8b\u6559\u5ba4'),
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
    # models/bulletin.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/bulletin.xml")

    date = schema.Date(
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
            vocabulary='duty',
        )
    )

    area = schema.List(
        title=_(u"Area"),
        required=False,
        value_type=schema.Choice(
            vocabulary=area,
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
# bulletin_templates.
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

    def t_title(self, value):
        if value in ('GW', 'SW', 'WK', 'HB', 'AQ'):
            factory = getUtility(IVocabularyFactory, 'duty')
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        else:
            return None

