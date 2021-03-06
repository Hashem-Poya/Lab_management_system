# -*- coding: utf-8 -*-
{
    'name': 'QR Code Invoice',
    'version': '13.0.1.0.0',
    'category': 'Accounting',
    'author': 'ERP Harbor Consulting Services',
    'summary': 'Generate QR Code for Invoice',
    'website': 'http://www.erpharbor.com',
    'description': """""",
    'depends': [
        'ehcs_qr_code_base',
        'account',
        'medical_lab_management'
    ],
    'data': [
        'report/account_invoice_report_template.xml',
        'views/qr_code_invoice_view.xml',
        'views/qr_code_patient_view.xml',
        'report/barcode_template.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
}
