// Copyright (c) 2019, Jamali Infocom and contributors
// For license information, please see license.txt

frappe.ui.form.on('Order Book', {
	onload: function(frm) {
		frm.page.sidebar.remove();
                frm.page.wrapper.find(".layout-main-section-wrapper").removeClass("col-md-10");
	 }
});

frappe.ui.form.on("Order Book", {
  get_order: function(frm) {
	cur_frm.refresh();
	cur_frm.clear_table("field_orders");
	cur_frm.refresh_fields();
    frappe.call({
    "method": "dairy_management.dairy_management.doctype.order_book.order_book.insert_data",
args: {
order_period: frm.doc.order_period,
from_date: frm.doc.from_date
},
callback:function(r){
	var len=r.message.length;
	console.log(r)
	for (var i=0;i<len;i++){
	        var row = frm.add_child("field_orders");
		row.field_order = r.message[i][0];
		row.customer = r.message[i][1];
		row.retailer = r.message[i][2];
		row.customer_group = r.message[i][3];
		row.territory = r.message[i][4];
		row.order_period = r.message[i][5];
		row.date = r.message[i][6];
		row.time = r.message[i][7];
		row.customer_address = r.message[i][8];
		row.contact_person = r.message[i][9];
		row.item_code = r.message[i][10];
		row.item_name = r.message[i][11];
		row.qty = r.message[i][12];
		row.rate = r.message[i][13];
		row.amount = r.message[i][14];
		row.item_tax_template = r.message[i][15];
		row.gst_rate = r.message[i][16];
		row.grand_total = r.message[i][17];
		row.sales_person = r.message[i][18];
	}
		cur_frm.refresh();
	}
    });
}
});

frappe.ui.form.on('Order Book Item', {
        qty(frm,cdt,cdn) {
		cur_frm.refresh_fields();
		var d = locals[cdt][cdn];
		frappe.model.set_value(d.doctype, d.name, "amount", (d.qty * d.rate));
		frappe.model.set_value(d.doctype, d.name, "grand_total", (d.amount + (d.amount * (d.gst_rate / 100))));
        },
        rate(frm,cdt,cdn) {
                cur_frm.refresh_fields();
                var d = locals[cdt][cdn];
                frappe.model.set_value(d.doctype, d.name, "amount", (d.qty * d.rate));
		frappe.model.set_value(d.doctype, d.name, "grand_total", (d.amount + (d.amount * (d.gst_rate / 100))));
        }
});
