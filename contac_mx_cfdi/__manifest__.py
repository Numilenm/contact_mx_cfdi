# -*- coding: utf-8 -*-
{
    'name': "CFDI en contacto",
    'author': "GECONS SAS",
    'category': 'Contact',
    'depends': ['base', 'l10n_mx_edi', 'account', 'contacts', 'payment'],
    'data': [
        'views/res_partner_view.xml',
    ],
    'price': 151.99,
    'currency': 'USD',
    'license': 'LGPL-3',
    'description': """
    English:
    This Odoo module extends the functionality to associate MX EDI contact details in the contact notebook for Mexican
     localization by default. It facilitates the use of CFDI (Comprobante Fiscal Digital por Internet) and payment methods, with these values being inherited into the invoice.

    Español:
    Este módulo de Odoo extiende la funcionalidad para asociar detalles de contacto MX EDI en la libreta de
     direcciones de contactos para la localización mexicana de forma predeterminada. Facilita el uso de CFDI (Comprobante Fiscal Digital por Internet) y métodos de pago, con estos valores heredándose a la factura.
    """,
    'installable': True,
    'application': True,
    'auto_install': False,
}
