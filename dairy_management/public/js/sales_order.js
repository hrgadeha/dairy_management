frappe.ui.form.on('Sales Order', {
	type_of_order(frm) {
        if(frm.doc.type_of_order == 'Morning Order'){
            frm.set_value("naming_series","SO-MOR-.-");
        }
        if(frm.doc.type_of_order == 'Evening Order'){
            frm.set_value("naming_series","SO-EVE-.-");
        }
	}
});

frappe.ui.form.on('Sales Order', {
    onload: function(frm) {
        if(frm.doc.__islocal){
            frappe.call({
		"method": "dairy_management.dairy_management.doctype.sales_team.getSP",
		args: {
			user: frappe.session.user
		},
		callback:function(r){
		    frm.clear_table("sales_team");
            var d = frm.add_child("sales_team");
                d.sales_person = r.message;
				d.allocated_percentage = 100;
            frm.refresh_field("sales_team");

}
});
}
}
});

