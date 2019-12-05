frappe.listview_settings['Field Order'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		if (doc.status === "Draft"){
			return [__("Draft"), "Red", "docstatus,=,Draft"];
		}
		else if (doc.status === "Order Booked") {
                        return [__("Order Booked"), "green", "status,=,Order Booked"];
                }
	}
};
