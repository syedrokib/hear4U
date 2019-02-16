# import time
# from src import db
# from src.models.product import product
# from src.models.cart import  cart
#
# product_sample_data = [
#     {
#         'title' : 'The Legend of Zelda: Ocarina Of Time',
#         'price' : 50,
#         'inventoryCount': 3
#     },
#     {
#         'title' : 'E.T The Extra Terrestial Atari',
#         'price' : 5,
#         'inventoryCount': 1
#     },
#     {
#         'title' : 'Pokemon Emerald Version',
#         'price' : 25,
#         'inventoryCount': 0
#     }
# ]
#
# cart_sample_data = [
#     {
#         'id': 1,
#         'productId' : 1,
#         'quantity': 1
#     },
#     {
#         'id': 2,
#         'productId' : 2,
#         'quantity': 2,
#     },
#     {
#         'id': 3,
#         'productId' : 3,
#         'quantity': 3
#     }
# ]
#
# def database_initialization_sequence():
#     for data in product_sample_data:
#         db.session.add(
#             product(
#                 title = data['title'],
#                 price = data['price'],
#                 inventory_count = data['inventoryCount']
#             )
#         )
#     try:
#         db.session.commit()
#     except Exception:
#         db.session.rollback()
#
#     for data in cart_sample_data:
#         db.session.add(
#             cart(
#                 id = data['id'],
#                 product_id = data['productId'],
#                 quantity = data ['quantity']
#             )
#         )
#     try:
#         db.session.commit()
#     except Exception:
#         db.session.rollback()
