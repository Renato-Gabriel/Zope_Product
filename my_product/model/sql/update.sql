update stocks set

stock=<dtml-sqlvar stock type="string">,
codigo=<dtml-sqlvar codigo type="string">,
quantidade=<dtml-sqlvar quantidade type="int">,
valor=<dtml-sqlvar valor type="float">

where
id=<dtml-sqlvar id type="int">;