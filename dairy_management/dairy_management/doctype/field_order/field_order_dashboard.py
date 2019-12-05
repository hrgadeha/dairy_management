from __future__ import unicode_literals

from frappe import _


def get_data():
        return {
                'heatmap_message': _('This is based on Order Book Link with this Field Order'),
                'fieldname': 'name',
                'non_standard_fieldnames': {
                        'Order Book': 'field_order'
                },
                'transactions': [
                        {
                                'label': _('Orders'),
                                'items': ['Order Book']
                        }
                ]
        }

