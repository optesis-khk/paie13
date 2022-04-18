{
    'name': 'Hr Loan',
    'version': '13.0.1',
    'author': 'Mouhamadou Yacine DIallo',
    'category': 'Human Resources',
    'description': """

	""",

    'depends': ['hr', 'hr_payroll', 'account', 'mail', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/hr_loan_notification.xml',
        'wizard/hr_loan_action_refusal.xml',
        'views/hr_loan_view.xml',
        'views/hr_payroll_view.xml',
    ],

    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
