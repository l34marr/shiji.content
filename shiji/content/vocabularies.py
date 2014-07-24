# -*- coding: utf-8 -*-

from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from shiji.content import MessageFactory as _


class Duty(object):
    """Duty Vocabulary
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='GW', title=_(u'GW')),
            SimpleTerm(value='SW', title=_(u'SW')),
            SimpleTerm(value='WK', title=_(u'WK')),
            SimpleTerm(value='HB', title=_(u'HB')),
            SimpleTerm(value='AQ', title=_(u'AQ'))
        )
        return SimpleVocabulary(items)
DutyFactory = Duty()

class Area(object):
    """Area Vocabulary
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='ktv', title=_(u'KTV')),
            SimpleTerm(value='swn', title=_(u'SWN')),
            SimpleTerm(value='jyt', title=_(u'JYT')),
            SimpleTerm(value='etyxs', title=_(u'ETYXS')),
            SimpleTerm(value='etyxq', title=_(u'ETYXQ')),
            SimpleTerm(value='etyls', title=_(u'ETYLS')),
            SimpleTerm(value='yht', title=_(u'YHT')),
            SimpleTerm(value='tbltns', title=_(u'TBLTNS')),
            SimpleTerm(value='jsf', title=_(u'JSF')),
            SimpleTerm(value='yyc', title=_(u'YYC')),
            SimpleTerm(value='sts', title=_(u'STS')),
            SimpleTerm(value='tsg', title=_(u'TSG')),
            SimpleTerm(value='snooker', title=_(u'SNOOKER')),
            SimpleTerm(value='yljs', title=_(u'YLJS'))
        )
        return SimpleVocabulary(items)
AreaFactory = Area()

class Origin(object):
    """Origin Vocabulary
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='form', title=_(u'Form')),
            SimpleTerm(value='app', title=_(u'APP')),
            SimpleTerm(value='oral', title=_(u'Oral')),
        )
        return SimpleVocabulary(items)
OriginFactory = Origin()

class Track(object):
    """Track Vocabulary
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='valid', title=u'持續列管'),
            SimpleTerm(value='done', title=u'解除列管'),
        )
        return SimpleVocabulary(items)
TrackFactory = Track()

class Category(object):
    """Category Vocabulary
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='execute', title=u'會議會議決議案執行情形'),
            SimpleTerm(value='maintain', title=u'會館工務修繕'),
            SimpleTerm(value='track', title=u'意見反映處理'),
        )
        return SimpleVocabulary(items)
CategoryFactory = Category()

