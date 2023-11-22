from odoo import models, fields


class Project(models.Model):
    _inherit = 'project.task'

    jira_id = fields.Char(string="Jira Id")
    create_date = fields.Date(string="Create Date")
