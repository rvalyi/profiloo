# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{'name': 'Base Profile',
 'version': '0.0.1',
 'author': 'Akretion',
 'website': 'www.akretion.com',
 'license': 'AGPL-3',
 'category': 'Generic Modules',
 'description': """
    This module will install the minimal necessary to extend the base module
 """,
 'depends': [
     'document',

     # https://github.com/akretion/odoo-usability
     'base_usability',
     'mail_usability',
     'base_technical_features',
     'base_company_extension',
     'eradicate_quick_create',
     'partner_tree_default',
     'base_partner_ref',

     # https://github.com/OCA/partner-contact
     'partner_firstname',

     # https://github.com/OCA/server-tools
     'scheduler_error_mailer',
     'disable_odoo_online',
     'auth_admin_passkey',
     'sentry',

     # https://github.com/OCA/web
     'web_sheet_full_width',
     'web_export_view',
     'web_translate_dialog',
     'web_environment_ribbon',
     'web_responsive',

 ],
 'data': [
 ],
 'installable': True,
 'application': True,
 }



