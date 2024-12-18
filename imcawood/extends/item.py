import frappe
from erpnext.stock.doctype.item.item import Item

class X_Item(Item):
    def validate(self):
        super(X_Item, self).validate()
        
        self.custom_volume = self.custom_height*self.custom_width*self.custom_length
    