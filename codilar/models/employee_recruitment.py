from odoo import models, fields


class Employees(models.Model):
    _name = 'employee.recruitment'

    Dep_name = fields.Many2many('employee.department', string='dep name')
    boolean = fields.Boolean(string='department', default=False)




