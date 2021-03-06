# -*- coding: utf-8 -*-


{
    'name': "Medical Lab Management",
    'version': '14.0.1.0.0',
    'summary': """Manage Medical Lab Operations.""",
    'description': """Manage Medical Lab General Operations, Odoo13, Odoo 13""",

    'category': 'Industries',

    'depends': ['base', 'mail', 'account', 'website', 'im_livechat', 'account', 'website_mail_channel', 'website_blog'],

    'data': [
        'security/lab_users.xml',
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/lab_patient_view.xml',
        'views/test_unit_view.xml',
        'views/lab_test_type.xml',
        'views/lab_test_content_type.xml',
        'views/physician_specialty.xml',
        'views/summary_demo_data.xml',
        'views/lab_request.xml',
        'views/lab_appointment.xml',
        'views/account_invoice.xml',
        'views/lab_cashier.xml',
        'views/lab_createbatch.xml',
        'views/center_manager.xml',
        'views/lab_mobile_team.xml',
        'views/create_team.xml',
        'views/assign_mobile_team.xml',
        'report/report.xml',
        'report/lab_test_report.xml',
        'report/lab_patient_card.xml',

        # 'views/custommodel.xml',
        'views/create_partner_by_website.xml',
        # 'views/create_partner.xml',
        # 'views/tmp_customer_registration_form.xml',
        # 'views/tmp_customer_registration_form_success.xml',
        'views/tmp_patient_form_success.xml',
        'views/tmp_patient_form.xml',
        # 'views/tmp_login_form.xml',
        # 'views/tmp_login_form_success.xml',
        'views/index.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
