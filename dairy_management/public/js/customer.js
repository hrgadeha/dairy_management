frappe.ui.form.on("Customer", "customer_group", function(frm) {
    cur_frm.set_query("link_with_distributor", function() {
        return {
            "filters": {
                "customer_group": "Distributor"
            }
        };
    });
});

frappe.ui.form.on('Customer', {
	validate(frm) {
		if(frm.doc.is_distributor){
		    frm.set_value("link_with_distributor",frm.doc.customer_name);
		}
	}
});
