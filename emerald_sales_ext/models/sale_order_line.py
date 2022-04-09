# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    balance_qty = fields.Float('Balance Quantity', copy=False, compute='_compute_balance_qty', store=True, digits='Product Unit of Measure', default=0.0)

    @api.depends('product_uom_qty', 'qty_delivered')
    def _compute_balance_qty(self):
        for line in self:
            line.balance_qty = line.product_uom_qty - line.qty_delivered


