from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    l10n_mx_edi_usage = fields.Selection(
        selection=[
            ('G01', 'Adquisición de mercancías'),
            ('G02', 'Devoluciones, descuentos o bonificaciones'),
            ('G03', 'Gastos en general'),
            ('I01', 'Construcciones'),
            ('I02', 'Mobilario y equipo de oficina por inversiones'),
            ('I03', 'Equipo de transporte'),
            ('I04', 'Equipo de cómputo y accesorios'),
            ('I05', 'Dados, troqueles, moldes, matrices y herramental'),
            ('I06', 'Comunicaciones telefónicas'),
            ('I07', 'Comunicaciones satelitales'),
            ('I08', 'Otra maquinaria y equipo'),
            ('D01', 'Honorarios médicos, dentales y gastos hospitalarios'),
            ('D02', 'Gastos médicos por incapacidad o discapacidad'),
            ('D03', 'Gastos funerales'),
            ('D04', 'Donativos'),
            ('D05', 'Intereses reales efectivamente pagados por créditos hipotecarios (casa habitación)'),
            ('D06', 'Aportaciones voluntarias al SAR'),
            ('D07', 'Primas por seguros de gastos médicos'),
            ('D08', 'Gastos de transportación escolar obligatoria'),
            ('D09', 'Depósitos en cuentas para el ahorro, primas que tengan como base planes de pensiones'),
            ('D10', 'Pagos por servicios educativos (colegiaturas)'),
            ('P01', 'A definir (CFDI 3.3 Unicamente)'),
            ('S01', 'Sin efectos fiscales'),
        ],
        string="Uso CFDI",
        default='P01',
        help=("Utilizado en CFDI 3.3 para expresar la clave del uso que el receptor dará a esta factura. "
                "Este valor es definido por el cliente."
                "\nNota: No es motivo de cancelación si la clave establecida "
                "no es el uso que dará el receptor del documento."),
    )
    l10n_mx_edi_payment_method_id = fields.Many2one(
        'l10n_mx_edi.payment.method',
        string="Forma de Pago",
        help=("Indica la forma en que se pagó/se pagará la factura, donde las opciones podrían ser: "
              "Efectivo, Cheque nominal, Tarjeta de crédito, etc. Deje en blanco si no lo conoce y el XML mostrará"
              " 'No identificado'."),
        store=True
    )
