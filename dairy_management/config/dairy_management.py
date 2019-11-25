from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
	{
            "label": _("Orders"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Field Order",
                    "label": _("Field Order"),
                    "description": _("Field Order"),
                                        "onboard": 1,
                },
		{
                    "type": "doctype",
                    "name": "Order Book",
                    "label": _("Order Book"),
                    "description": _("Order Book"),
                                        "onboard": 1,
                }
            ]
        },
	{
            "label": _("Route Master"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Vehicle Route",
                    "label": _("Vehicle Route"),
                    "description": _("Vehicle Route"),
                                        "onboard": 1,
                }
            ]
        },
	{
            "label": _("Masters"),
            "items": [
		{
                    "type": "doctype",
                    "name": "Vehicle",
                    "label": _("Vehicle"),
                    "description": _("Vehicle"),
                                        "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Driver",
                    "label": _("Driver"),
                    "description": _("Driver"),
					"onboard": 1,
                },
		{
                    "type": "doctype",
                    "name": "Location",
                    "label": _("Location"),
                    "description": _("Location"),
					"onboard": 1,
                }
            ]
        }
]
