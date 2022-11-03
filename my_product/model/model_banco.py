import os
from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL
from Globals import package_home


global product_path
product_path = os.path.join(package_home(globals())) + '/'

class ModelBanco(SimpleItem.SimpleItem):

    def __init__(self, id):
        self.id = id

    def m_insert(self, stock, codigo, quantidade, valor):
        return self._insert(stock=stock, codigo=codigo, quantidade=quantidade, valor=valor)

    def m_delete(self, id):
        return self._delete(id=id)

    def m_update(self, id, stock, codigo, quantidade, valor):
        return self._update(id=id, stock=stock, codigo=codigo, quantidade=quantidade, valor=valor)

    def m_select(self):
        return self._select()


    _insert = SQL(id='insert', title='', connection_id='Psycopg2_database_connection',
                   arguments='stock codigo quantidade valor',
                   template=open(product_path + 'sql/insert.sql').read())

    _delete = SQL(id='delete', title='', connection_id='Psycopg2_database_connection',
                   arguments='id',
                   template=open(product_path + 'sql/delete.sql').read())

    _update = SQL(id='update', title='', connection_id='Psycopg2_database_connection',
                   arguments='id stock codigo quantidade valor',
                   template=open(product_path + 'sql/update.sql').read())

    _select = SQL(id='select', title='', connection_id='Psycopg2_database_connection',
                   arguments='',
                   template=open(product_path + 'sql/select.sql').read())
    
