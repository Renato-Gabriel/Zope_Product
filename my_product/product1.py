from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from controller.control_banco import ControlBanco

class FirstProduct(SimpleItem.SimpleItem):

    meta_type = 'Treinamento_Produto'
    x = ControlBanco(id='admin')

    manage_options = (
        {'label': 'View', 'action': 'x/index'},
    )

    def __init__(self, id):
        "initialise a new instance of FirstProduct"
        self.id = id

def addFirstProduct(self, id, REQUEST=None):
    "Add a FirstProduct to a folder."
    self._setObject(id, FirstProduct(id))
    if REQUEST is not None:
        return self.manage_main(self, REQUEST)

addFirstProductForm = PageTemplateFile('controller/view/zpt/addFirstProductForm', globals())