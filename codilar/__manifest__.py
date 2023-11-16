{
    'name': 'Employee',
    'version': '1.0',
    'sequence': -100 ,
    'author': 'vismaya',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views_inherit.xml',
        'views/employee_details.xml',
        'views/employee_department.xml',
        'views/employee_sale.xml',
        'views/employee_recruitment.xml',
        'data/send_email_template.xml',
    ]
}
