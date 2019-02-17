import json
from . import translator
from flask import Flask, redirect, request, Response
from src.handlers.translator import translateAudioFile

@translator.route('/translator', methods=['POST'])
def translate():
    # if 'file' not in request.files:
    #     return Response(json.dumps("Bad Request missing key"), status=400, mimetype='application/json')
    #
    # file = request.files['file']
    #
    # if file.filename == '':
    #     return Response(json.dumps("Bad Request"), status=400, mimetype='application/json')
    # else:

    payload = str(request.get_json()['payload'])
    print(payload)
    #
    # fileContent = translateAudioFile(file)
    # file.close()


    return Response(json.dumps({"Content" : payload}), status=200, mimetype='application/json')



# return Response(json.dumps({"Content": str(fileContent)}), status=200, mimetype='application/json' )


    # cartId = str(request.get_json()['cartId'])
    # try:
    #     selected_cart = db.session.query(cart).filter(cart.id == cartId).all()
    # except Exception as e:
    #     return not_found(cartId)
    # else:
    #     selected_cart_json = build_cart_object(selected_cart)
    #     for data in selected_cart_json['products']:
    #         # First check if the quantity specified for the product is in stock.
    #         product_to_be_purchased = None
    #         try:
    #             product_to_be_purchased = db.session.query(product).filter(
    #                 and_(
    #                     product.id == data['productId'],
    #                     product.inventory_count >= data['quantity']
    #                 )
    #             ).one()
    #         except Exception:
    #             message = {"error" : "Not enough stock for " + str(data['quantity']) + " unit(s) of product: " + str(data['productId'])}
    #             return Response(json.dumps(message), status=400, mimetype='application/json')
    #         else:
    #             product_to_be_purchased.inventory_count = product_to_be_purchased.inventory_count - data['quantity']
    #             try:
    #                 db.session.commit()
    #             except Exception:
    #                 return Response(json.dumps({"error" : str(e)}), status=500, mimetype='application/json')
    #     return Response(json.dumps({"cartPurchased" : cartId, "cartDetails" : selected_cart_json}), status=200, mimetype='application/json' )
