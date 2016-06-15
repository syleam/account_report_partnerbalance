# -*- coding: utf-8 -*-
##############################################################################
#
#    account_report_partnerbalance module for OpenERP, Extra Accounting Report Partner Balance
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.syleam.fr>)
#              Sebastien LANGE <sebastien.lange@syleam.fr>
#
#    This file is a part of account_extra_report_partnerbalance
#
#    account_report_partnerbalance is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    account_report_partnerbalance is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Extra Accounting Report Partner Balance',
    'version': '1.0',
    'category': 'Accounting & Finance',
    'description': """Extra Accounting Report Partner Balance""",
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'depends': [
        'account_extra_reports',
    ],
    'data': [
        'views/report_partnerbalance.xml',
        'wizard/account_report_partner_balance_view.xml',
        'data/account_report.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
