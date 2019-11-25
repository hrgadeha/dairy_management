frappe.ui.form.on("Customer", "customer_group", function(frm) {
    cur_frm.set_query("link_with_distributor", function() {
        return {
            "filters": {
                "customer_group": "Distributor"
            }
        };
    });
});

