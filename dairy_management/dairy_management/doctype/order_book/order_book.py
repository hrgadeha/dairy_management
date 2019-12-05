# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jamali Infocom and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.document import Document

class OrderBook(Document):
	def on_submit(self):
		for d in self.field_orders:
			sv = frappe.get_doc("Field Order",d.field_order)
			sv.order_book = self.name
			sv.status = "Order Booked"
			sv.save()

		customer = []
		for d in self.field_orders:
			customer.append(d.customer)
		customer = list(dict.fromkeys(customer))
		for c in customer:
			sales_order = None
			items = []
			for i in self.field_orders:
				item_li = {"retailer":i.retailer,"item_code": i.item_code,"item_name": i.item_name,"description": i.item_name,"qty": i.qty,"rate": i.rate,"item_tax_template":d.item_tax_template}
				if i.customer == c:
					items.append(item_li)
					sales_order = frappe.get_doc({
					"doctype": "Sales Order",
					"customer": i.customer,
					"type_of_order": i.order_period,
					"transaction_date": i.date,
					"delivery_date": i.date,
					"items": items
					})
			sales_order.insert(ignore_permissions=True)
			sales_order.save()

@frappe.whitelist(allow_guest=True)
def insert_data(from_date,order_period,status = "Order Booked"):
	query="select name,distributor,customer,customer_group,territory,order_period,date,time,customer_address,contact_person,item_code,item_name,qty,rate,amount,gst_rate,tax,grand_total,sales_person from `tabField Order` where status != '"+str(status)+"' and docstatus = 1 and date = '"+str(from_date)+"' and order_period = '"+str(order_period)+"' order by customer;"
	li=[]
	dic=frappe.db.sql(query, as_dict=True)
	for i in dic:
		name,distributor,customer,customer_group,territory,order_period,date,time,customer_address,contact_person,item_code,item_name,qty,rate,amount,gst_rate,tax,grand_total,sales_person = i["name"],i["distributor"],i["customer"],i["customer_group"],i["territory"],i["order_period"],i["date"],i["time"],i["customer_address"],i["contact_person"],i["item_code"],i["item_name"],i["qty"],i["rate"],i["amount"],i["gst_rate"],i["tax"],i["grand_total"],i["sales_person"]
		li.append([name,distributor,customer,customer_group,territory,order_period,date,time,customer_address,contact_person,item_code,item_name,qty,rate,amount,gst_rate,tax,grand_total,sales_person])
	return li

@frappe.whitelist(allow_guest=True)
def createDN(doc,method):
	for d in doc.items:
		sales_order = frappe.get_doc({
		"doctype": "Delivery Note",
		"customer": doc.customer,
		"retailer": d.retailer,
		"posting_date": doc.delivery_date,
		"grand_total": d.amount,
		"items": [
		{
			"item_code": d.item_code,
			"item_name": d.item_name,
			"qty": d.qty,
			"rate": d.rate,
			"amount": d.amount,
			"warehouse": "Stores - VD",
			"item_tax_template": d.item_tax_template,
			"against_sales_order": doc.name,
			"so_detail": d.name
		}
		]
		})
		sales_order.insert()
