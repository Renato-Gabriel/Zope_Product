from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from Products.my_product.model.model_banco import ModelBanco

class ControlBanco(SimpleItem.SimpleItem):

    def __init__(self, id):
        self.id = id
        self.model = ModelBanco('123')

    def c_insert(self, stock, codigo, quantidade, valor):
        """Insere uma nova row ao banco."""
        self.model.m_insert(stock=stock, codigo=codigo, quantidade=quantidade, valor=valor)
        return self.c_select()

    def c_delete(self, id):
        """Recebe argumento id e deleta a row."""
        self.model.m_delete(id=id)
        return self.c_select()

    def c_update(self, id, stock, codigo, quantidade, valor):
        """Atualiza a row de acordo com os argumentos inputados."""
        self.model.m_update(id=id, stock=stock, codigo=codigo, quantidade=quantidade, valor=valor)
        return self.c_select()

    def c_select(self):
        """Retorna a page select com o argumento da model."""
        d = self.model.m_select()
        return self.select(dados=d)
    

    index = PageTemplateFile('view/zpt/index', globals())
    header = PageTemplateFile('view/zpt/header', globals())
    footer = PageTemplateFile('view/zpt/footer', globals())
    css = PageTemplateFile('view/css/main.css', globals())
    install = PageTemplateFile('view/zpt/install', globals())
    zope = PageTemplateFile('view/zpt/zope', globals())
    ref = PageTemplateFile('view/zpt/ref', globals())
    select = PageTemplateFile('view/zpt/select', globals())