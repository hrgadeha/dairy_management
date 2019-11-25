from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.document import Document


@frappe.whitelist(allow_guest=True)
def getSP(user):
        sp = frappe.db.sql("""select name from `tabSales Person` where 
				user_id = '{}';""".format(user))

        return sp[0][0] if sp else ""

