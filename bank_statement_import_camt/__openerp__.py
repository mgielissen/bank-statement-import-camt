##############################################################################
#
#    CAMT .052+.053 import module for Odoo
#    Copyright (C) 2015 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'CAMT Bank Statements Import',
    'summary': 'Imports CAMT .052 and .053 XML files in Odoo',
    'version': '9.0.1.0',
    'license': 'AGPL-3',
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'category': 'Accounting & Finance',
    'depends': ['account_bank_statement_import'],
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
}
