# -*- coding: utf-8 -*-
from openerp import fields, models, api, exceptions

import logging
_logger = logging.getLogger(__name__)

class crm_lead(models.Model):
    _inherit = 'crm.lead'
