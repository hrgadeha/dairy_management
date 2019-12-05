from __future__ import unicode_literals

from frappe import _


def get_data():
        return {
                'heatmap_message': _('This is based on Field Order Link with this Order Book'),
                'fieldname': 'name',
                'non_standard_fieldnames': {
                        'Field Order': 'order_book'
                },
                'transactions': [
                        {
                                'label': _('Orders'),
                                'items': ['Field Order']
                        }
                ]
        }

