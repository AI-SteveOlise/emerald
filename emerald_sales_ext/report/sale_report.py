# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleReport(models.Model):
    _inherit = 'sale.report'

    balance_qty = fields.Float('Balance Qty', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['balance_qty'] = ", sum(l.balance_qty / u.factor * u2.factor) as balance_qty"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)