# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_mx_edi_cfdi_request = fields.Selection(readonly=False)

    @api.onchange('partner_id')
    def _change_partner_fields(self):
        for move in self:
            if move.partner_id:
                if move.partner_id.l10n_mx_edi_usage:
                    move.l10n_mx_edi_usage = move.partner_id.l10n_mx_edi_usage
                if move.partner_id.l10n_mx_edi_payment_method_id:
                    move.l10n_mx_edi_payment_method_id = move.partner_id.l10n_mx_edi_payment_method_id


