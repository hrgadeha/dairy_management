// Copyright (c) 2019, Jamali Infocom and contributors
// For license information, please see license.txt

frappe.ui.form.on('Field Order', {
	// refresh: function(frm) {

	// }
});

cur_frm.add_fetch("item_code","item_name","item_name")
cur_frm.add_fetch("item_code","standard_rate","rate")
cur_frm.add_fetch("item_code","stock_uom","uom")


frappe.ui.form.on('Field Order', {
    onload: function(frm) {
        if(frm.doc.__islocal){
            frappe.call({
                "method": "dairy_management.dairy_management.doctype.sales_team.getSP",
                args: {
                        user: frappe.session.user
                },
                callback:function(r){
                    frm.set_value("sales_person",r.message);

}
});
}
}
});

frappe.ui.form.on('Field Order', {
    customer: function(frm) {
        if(frm.doc.customer){
            frappe.call({
                "method": "dairy_management.dairy_management.doctype.field_order.field_order.getContact",
                args: {
                        customer: frm.doc.customer
                },
                callback:function(r){
                    frm.set_value("contact_person",r.message);

}
});
}
}
});


frappe.ui.form.on('Field Order', {
    customer: function(frm) {
        if(frm.doc.customer){
            frappe.call({
                "method": "dairy_management.dairy_management.doctype.field_order.field_order.getAddress",
                args: {
                        customer: frm.doc.customer
                },
                callback:function(r){
                    frm.set_value("customer_address",r.message);

}
});
}
}
});

frappe.ui.form.on('Field Order', {
	qty(frm) {
		frm.set_value("amount",(frm.doc.rate * frm.doc.qty));
		frm.set_value("grand_total",(frm.doc.rate * frm.doc.qty));
		frm.set_value("grand_total",(((frm.doc.tax / 100) * frm.doc.amount)) + frm.doc.amount);
	},
	rate(frm) {
		frm.set_value("amount",(frm.doc.rate * frm.doc.qty));
		frm.set_value("grand_total",(frm.doc.rate * frm.doc.qty));
		frm.set_value("grand_total",(((frm.doc.tax / 100) * frm.doc.amount)) + frm.doc.amount);
	},
	tax(frm) {
		frm.set_value("grand_total",(((frm.doc.tax / 100) * frm.doc.amount)) + frm.doc.amount);
	}
});
