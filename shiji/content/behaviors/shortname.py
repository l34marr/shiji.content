from zope.component import adapts
from zope.interface import Interface
from zope.interface import implements
from zope.component import getUtility
from plone.app.content.interfaces import INameFromTitle
from Products.CMFCore.interfaces import ISiteRoot
from zope.annotation.interfaces import IAnnotations

ANNOTATION_DATE_ID = 'shiji.content.behavior.dateid'
ANNOTATION_NEXT_ID = 'shiji.content.behavior.nextid'


class INameFromCreationDate(Interface):
    """Enable Name from CreationDate Behavior
    """


class NameFromCreationDate(object):
    implements(INameFromTitle)
    adapts(INameFromCreationDate)

    def __new__(cls, context):
        instance = super(NameFromCreationDate, cls).__new__(cls)
        site = getUtility(ISiteRoot)
        storage = IAnnotations(site, {})
        cdate = context.creation_date
        current_date = "%d%s%s" % (cdate.year(), cdate.mm(), cdate.dd())

        if not storage.has_key(ANNOTATION_DATE_ID):
            storage[ANNOTATION_DATE_ID] = current_date
            dateid = current_date
        else:
            dateid = storage.get(ANNOTATION_DATE_ID)

        if dateid != current_date:
            dateid = current_date
            storage[ANNOTATION_DATE_ID] = current_date
            nextid = 1
        else:
            nextid = storage.get(ANNOTATION_NEXT_ID, 1)

        storage[ANNOTATION_NEXT_ID] = nextid + 1

        instance.title = '%s%s' % (dateid, str(nextid).zfill(2))
        return instance

    def __init__(self, context):
        self.context = context

