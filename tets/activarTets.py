from cart import tests as testCart
from orders import tests as testOrders
from products import tests as testProduct

# Invocar test activarlos

testCart.TestCartModels()
testOrders.TestOrderModels()
testProduct.TestProductModels()

print("Tets echo")
