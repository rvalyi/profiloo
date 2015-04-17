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

{'name': 'Accounting Profile',
 'version': '0.0.1',
 'author': 'Akretion',
 'website': 'www.akretion.com',
 'license': 'AGPL-3',
 'category': 'Profile Modules',
 'description': """
    This module is a generic profile for accounting.
 """,
 'depends': [
     'profile_base',
     'invoice_fiscal_position_update',
     'account_balance_line',
     'account_check_deposit',
     'account_constraints',
     'account_default_draft_move',
     'account_fiscal_position_vat_check',
     'account_journal_always_check_date',
     'account_move_line_no_default_search',
     'account_move_line_payable_receivable_filter',
     'account_reversal',
     'account_export_csv',
     'account_financial_report_webkit',
     'account_financial_report_webkit_xls',
     'account_journal_report_xls',
     'account_move_line_report_xls',
 ],
 'data': [
 ],
 'installable': True,
 'application': True,
 }
