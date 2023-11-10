from odoo import models, fields


class Employee(models.Model):
    _name = 'employee.department'
    name = fields.Many2one('employee.details', string='name')
    Dep_name = fields.Char(string ="dep name")
    Dep_center = fields.Char(string ="dep center")
    Dep_num = fields.Integer(string ="dep num")