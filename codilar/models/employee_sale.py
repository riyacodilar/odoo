from odoo import models, fields


class Employees(models.Model):
    _name = 'employee.sale'

    department = fields.Many2one('employee.department', string='department name')
    sale_amount = fields.Float(string="sale amount")




