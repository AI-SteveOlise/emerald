# -*- coding: utf-8 -*-

from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self._create_invoices(final=True)
        return res

