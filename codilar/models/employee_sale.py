from odoo import models, fields, api


class EmployeeSale(models.Model):
    _name = 'employee.sale'

    department = fields.Many2one('employee.department', string='Department Name')
    sale_amount = fields.Float(string='sale amount')
    sale_cost = fields.Float(String='Sale Cost')
    total = fields.Float(string='Total')
    result = fields.Float(string='Result', compute='_total',  store=True)

    @api.onchange('sale_amount', 'sale_cost')
    def onchange_sale_fields(self):
        for total in self:
            total.total = total.sale_cost + total.sale_amount

    def calculate_result(self):
        for record in self:
            record.total = record.sale_amount + record.sale_cost

    @api.depends('sale_amount', 'sale_cost')
    def _total(self):
        for record in self:
            record.result = record.sale_amount + record.sale_cost
