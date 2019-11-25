frappe.ui.form.on("Item Tax Template Detail", {
	"tax_rate": function(frm, cdt, cdn) {
		cur_frm.refresh();
		cur_frm.refresh_fields();
		var d = locals[cdt][cdn];
		var total = 0;
		var sales_invoice = frm.doc.taxes;

   	for(var i in sales_invoice) {
		total = total + sales_invoice[i].tax_rate;
		frm.set_value("tax", total);
	}
}
});

frappe.ui.form.on("Item Tax Template Detail", {
	"taxes_remove": function(frm, cdt, cdn) {
		cur_frm.refresh();
		cur_frm.refresh_fields();
		var d = locals[cdt][cdn];
		var total = 0;
		var sales_invoice = frm.doc.taxes;
		console.log(total)

   	for(var i in sales_invoice) {
		total = total + sales_invoice[i].tax_rate;
		frm.set_value("tax", total);
	}
}
});
