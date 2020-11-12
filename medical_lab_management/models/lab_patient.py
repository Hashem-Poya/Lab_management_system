

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _


class LabPatient(models.Model):
    _name = 'lab.patient'
    _rec_name = 'name'
    _description = 'Patient'

    patient = fields.Many2one('res.partner', string='Partner')
    patient_image = fields.Binary(string='Photo')
    patient_id = fields.Char(string='Patient ID')
    name = fields.Char(string='Patient ID',
                       default=lambda self: _('New'), readonly=True)
    title = fields.Selection([
        ('ms', 'Miss'),
        ('mister', 'Mister'),
        ('mrs', 'Mrs'),
    ], string='Title', default='mister')
    emergency_contact = fields.Many2one(
        'res.partner', string='Emergency Contact')
    gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'),
         ('ot', 'Other')], 'Gender')
    dob = fields.Date(string='Date Of Birth')
    age = fields.Char(string='Age', compute='compute_age')
    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        'Blood Group')
    visa_info = fields.Char(string='Visa Info', size=64)
    id_proof_number = fields.Char(string='ID Proof Number')
    note = fields.Text(string='Note')
    date = fields.Datetime(string='Date Requested',
                           default=lambda s: fields.Datetime.now())
    phone = fields.Char(string="Phone", )
    email = fields.Char(string="Email",)
    date = fields.Datetime(string='Date Requested',
                           default=lambda s: fields.Datetime.now(), invisible=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)
    mobile_team_request = fields.Selection(
        [('y', 'Yes'), ('n', 'No')], 'Mobile Team Request', default='n')
    no_of_visitors = fields.Integer(string='visitors')

    # def name_get(self):
    #     '''Display name in breadcrumb'''
    #     result = []
    #     for rec in self:
    #         name = rec.name
    #         result.append((rec.id, name))
    #     return result

    # def count_visitor(self):
    #     test_obj = self.env["lab.patient"].search([])
    # no_of_count = len(test_obj)

    def compute_age(self):
        for data in self:
            if data.dob:
                dob = fields.Datetime.from_string(data.dob)
                date = fields.Datetime.from_string(data.date)
                delta = relativedelta(date, dob)
                data.age = str(delta.years) + ' years'
            else:
                data.age = ''

    def patient_register_confirmation(self, result):

        message_body = "Dear " + result.patient.name + "," + "<br>You have successfully registered as Patient " \
            + "<br>Your Patient ID : <bold>" + result.name + "<bold><br>Date : " + str(result.date) + \
            '\bYou will soon recieve your Appointment confirmation Email.<br><br>Thank you'

        template_obj = self.env['mail.mail']
        template_data = {
            'subject': 'Patient register Confirmation',
            'body_html': message_body,
            'email_from': self.env.user.company_id.email,
            'email_to': result.email
        }
        template_id = template_obj.create(template_data)
        template_obj.send(template_id)

    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].next_by_code('lab.patient')
        vals['name'] = sequence or _('New')
        result = super(LabPatient, self).create(vals)
        # patient_register_confirmation(result)
        return result

    @api.onchange('patient')
    def detail_get(self):
        self.phone = self.patient.phone
        self.email = self.patient.email
