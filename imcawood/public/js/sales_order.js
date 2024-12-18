frappe.ui.form.on("Sales Order Item", {
	item_code: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];        
        if(row.item_group === "Panels")
            {
            frm.get_field("items").grid.toggle_display("custom_pack", true);
            frm.get_field("items").grid.toggle_display("custom_sheets", true);
        }else {
            frm.get_field("items").grid.toggle_display("custom_pack", false);
            frm.get_field("items").grid.toggle_display("custom_sheets", false);
        }
	},
});
