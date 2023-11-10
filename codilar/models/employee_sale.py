from odoo import models, fields


class Employees(models.Model):
    _name = 'employee.sale'

    Dep_name = fields.Many2one('employee.department', string='dep name')
    sale_amount = fields.Float(string="sale amount")




