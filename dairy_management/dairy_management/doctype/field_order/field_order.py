# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jamali Infocom and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class FieldOrder(Document):
	pass


@frappe.whitelist(allow_guest=True)
def getContact(customer):
	item_data = frappe.db.sql("""select con.name from `tabDynamic Link` dl, `tabContact` con 
		where dl.parent = con.name and dl.link_doctype = 'Customer' and dl.link_name = '{0}';""".format(customer), as_list=1)
	return item_data[0][0] if item_data else ""

@frappe.whitelist(allow_guest=True)
def getAddress(customer):
        item_data = frappe.db.sql("""select adr.name from `tabDynamic Link` dl, `tabAddress` adr 
				where dl.parent = adr.name and dl.link_doctype = 'Customer' 
			and dl.link_name = '{0}';""".format(customer), as_list=1)
        return item_data[0][0] if item_data else ""
