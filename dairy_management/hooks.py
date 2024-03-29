# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "dairy_management"
app_title = "Dairy Management"
app_publisher = "Jamali Infocom"
app_description = "App for Dairy Management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dairy_management/css/dairy_management.css"
# app_include_js = "/assets/dairy_management/js/dairy_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/dairy_management/css/dairy_management.css"
# web_include_js = "/assets/dairy_management/js/dairy_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
		"Sales Order" : "public/js/sales_order.js",
		"Customer" : "public/js/customer.js",
		"Item Tax Template" : "public/js/item_tax_template.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "dairy_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dairy_management.install.before_install"
# after_install = "dairy_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dairy_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

fixtures = [
	{
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
			"Sales Order-type_of_order",
			"Sales Order-vehicle_route",
			"Sales Person-user_id",
			"Customer-link_with_distributor",
			"Item Tax Template-tax",
			"Field Order-auto_repeat",
			"Delivery Note-retailer",
			"Sales Order Item-retailer",
			"Customer-is_distributor"
		]
	   ]
	]
    	},
	{
        "doctype": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
                        "Sales Order-naming_series-options",
			"Sales Order-naming_series-read_only",
			"Sales Order-delivery_date-default",
			"Field Order-naming_series-default",
			"Field Order-naming_series-options",
			"Vehicle Route-naming_series-default",
			"Vehicle Route-naming_series-options"
                ]
           ]
        ]
        }
]

#Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"on_submit": "dairy_management.dairy_management.doctype.order_book.order_book.createDN"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dairy_management.tasks.all"
# 	],
# 	"daily": [
# 		"dairy_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"dairy_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dairy_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dairy_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dairy_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dairy_management.event.get_events"
# }

