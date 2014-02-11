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

