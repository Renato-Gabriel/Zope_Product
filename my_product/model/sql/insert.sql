insert into stocks
(
stock,
codigo,
quantidade,
valor
)

values
(
<dtml-sqlvar stock type="string">,
<dtml-sqlvar codigo type="string">,
<dtml-sqlvar quantidade type="int">,
<dtml-sqlvar valor type="float">
);