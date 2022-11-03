import product1

def initialize(context): 
    """Inicializa o produto FirstProduct / Faz o objeto aparecer na lista de produtos"""
    context.registerClass(
        product1.FirstProduct,
        constructors = (
            product1.addFirstProductForm,
            product1.addFirstProduct
        ),
        icon = 'controller/view/images/icon.png'
    )