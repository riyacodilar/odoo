{
    'name': 'Employee',
    'version': '1.0',
    'sequence': '-100',
    'author': 'Riya',
    'depends': ['hr', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views_inherit.xml',
        'views/employee_details.xml',
        'views/employee_department.xml',
        'views/employee_sale.xml',
        'views/employee_recruitment.xml',
        'data/send_email_template.xml',
        # 'views/project_task_views.xml',
        'report/report.xml',
        'report/employee_report_template.xml',
        'report/sale_report_template.xml'
    ]
}
