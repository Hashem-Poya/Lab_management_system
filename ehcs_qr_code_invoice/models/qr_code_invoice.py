# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request
from odoo.addons.ehcs_qr_code_base.models.qr_code_base import generate_qr_code


class QRCodeInvoice(models.Model):
    _inherit = 'account.move'

    qr_image = fields.Binary("QR Code", compute='_generate_qr_code')

    def _generate_qr_code(self):

        patient = self.env['lab.patient'].search(
            [('patient', '=', self.partner_id.id)])
        self.qr_image = generate_qr_code(patient.name)
        # print('++++++++++++++++++++++++++++++++++++++++++++++++++')
        # global pid
        # pid = patient.name
        # print(pid)

    def sticker_barcode_generator(self):
        # patient = self.env['lab.patient'].search([('patient', '=', self.partner_id.id)])
        # self.qr_image = generate_qr_code(patient.name)
        patient = self.env['lab.patient'].search(
            [('patient', '=', self.partner_id.id)])
        data = {
            "qr_code_image": self.qr_image,
            'pid': patient.name
        }
        return self.env.ref("ehcs_qr_code_invoice.sticker_barcode_action").report_action(
            self, data=data
        )
