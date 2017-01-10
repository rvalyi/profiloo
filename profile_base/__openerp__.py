# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2014 Akretion (http://www.akretion.com).
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

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
     'admin_technical_features',
     'disable_openerp_online',
     'shell',
     'scheduler_error_mailer',
     'cron_run_manually',
     'base_partner_always_multi_contacts',
     'base_usability',
     'base_company_extension',
     'base_fix_display_address',
     'partner_search',
     'web_translate_dialog',
 ],
 'data': [
 ],
 'installable': True,
 'application': True,
 }



