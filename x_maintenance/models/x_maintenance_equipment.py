# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    product_id = fields.Many2one(
        'product.product',
        'Product',
        required=True,
        check_company=True,
        domain="[('type', 'in', ['product', 'consu'])]")

    @api.onchange('product_id')
    def _onchange_model(self):
        if self.product_id:
            self.name = self.product_id.name
