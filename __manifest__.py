# -*- coding: utf-8 -*-
################################################################################
#
#    RENACE Technologies
#
#    Copyright (C) 2023-TODAY RENACE Technologies(<https://www.renace.tech>).
#    Author: ADDERLY MARTE (admarte@renace.tech)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
{
    'name': "Eliminar Líneas de Pedido en POS",
    'version': '17.0.1.0.0',
    'category': 'Punto de Venta',
    'summary': """Eliminar Líneas de Pedido Individuales en Punto de Venta.""",
    'description': """Elimina cada línea del pedido seleccionado simplemente 
    haciendo clic en el botón X o borra todo el pedido con un solo clic.""",
    'author': "Adderly Marte (RENACE.TECH)",
    'company': 'RENACE.TECH',
    'maintainer': "Adderly Marte (RENACE.TECH)",
    'website': "https://www.renace.tech",
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_delete_orderline/static/src/js/clear_button.js',
            'pos_delete_orderline/static/src/js/clear_order_line.js',
            'pos_delete_orderline/static/src/xml/clear_button_templates.xml',
            'pos_delete_orderline/static/src/xml/clear_order_line_templates.xml',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
