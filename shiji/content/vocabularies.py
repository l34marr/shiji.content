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

class Origin(object):
    """Origin Vocabulary
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='form', title=u'意見反應單'),
            SimpleTerm(value='app', title=u'APP'),
            SimpleTerm(value='oral', title=u'口頭反應'),
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

