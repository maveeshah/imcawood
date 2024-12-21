import frappe
from erpnext.stock.doctype.item.item import Item


class CustomItem(Item):
    def validate(self):
        super(CustomItem, self).validate()

        if self.item_group and self.item_group == "Panels":
            self.custom_volume = (
                self.custom_height * self.custom_width * self.custom_length
            )
