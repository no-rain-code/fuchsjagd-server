# encoding=utf-8
import datetime
from piston.handler import BaseHandler
from piston.utils import rc

from senders.models import SenderGroup

class SenderGroupHandler(BaseHandler):
    allowed_methods = ('GET',)
    fields = (
        'hash',
        'description',
        ('senders', (
            'longitude',
            'latitude',
            'senderpower',
        )),
    )
    model = SenderGroup
