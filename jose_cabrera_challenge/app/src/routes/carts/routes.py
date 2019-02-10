import json
import uuid
from . import carts
from flask import Flask, request, Response
from flask_expects_json import expects_json
from src import db
from src.models.cart import cart, build_cart_object
from src.models.product import product
from sqlalchemy import and_


@carts.errorhandler(404)
def not_found(id):
    message = {
        'status': 404,
        'message': 'Cart:' + id + ' Not Found.'
    }
    return Response( json.dumps(message) , status=404, mimetype='application/json')

@carts.route('/carts', methods=['GET'])
def getAllCarts():
    try:
        all_shopping_carts_ids = db.session.query(cart.id).all()
    except Exception:
        return Response(json.dumps({"error" : str(e)}), status=500, mimetype='application/json')
    else:        
        cart_objects = []
        built_shopping_cart_ids = []
        for shopping_cart_id in all_shopping_carts_ids:
            if shopping_cart_id not in built_shopping_cart_ids:
                cart_objects.append(build_cart_object(cart.query.filter_by(id=shopping_cart_id).all()))
                built_shopping_cart_ids.append(shopping_cart_id)    
        return Response(json.dumps(cart_objects), status=200, mimetype='application/json')

@carts.route('/carts/<cartId>', methods=['GET'])
def getCart(cartId):
    try:
        cart.query.filter_by(id=cartId).one()
    except Exception:
        return not_found(cartId)
    else:
        selected_cart = cart.query.filter_by(id=cartId).all()
        return Response(json.dumps(build_cart_object(selected_cart)), status=200, mimetype='application/json')

@carts.route('/carts', methods=['POST'])
def createCart():
    data = request.get_json()
    cart_id = uuid.uuid4()
    try:
        for cart_data in data:
            try:
                db.session.query(product).filter(product.id == cart_data['productId']).one()
            except Exception as e:
                return Response(json.dumps({"error": "Product: " + str(cart_data['productId']) + " doesn't exist."}), status=404, mimetype='application/json')
            else:
                db.session.add(cart(id = cart_id, product_id = cart_data['productId'], quantity = cart_data['quantity']))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return Response(json.dumps({"error" : str(e)}), status=500, mimetype='application/json')
    else:
        return Response(json.dumps({"createdCartId" : str(cart_id)}), status=200, mimetype='application/json')

# updateCart will only be able to update the quantity number of the product included in the Car.
@carts.route('/carts/<cartId>', methods=['PUT'])
def updateCart(cartId):
    data = request.get_json()

    for cart_data in data:
        try:
            cart_to_be_updated = db.session.query(cart).filter(
                    and_(
                        cart.id == cartId,
                        cart.product_id == cart_data['productId']
                    ) 
                ).one()
        except Exception:
            return not_found(cartId)
        else:
            cart_to_be_updated.quantity = cart_data['quantity']
            try:
                db.session.commit()
            except Exception:
                db.session.rollback()
                return Response(json.dumps({"error" : str(e)}), status=500, mimetype='application/json')

    return Response(json.dumps({"updatedCartId" : str(cartId)}), status=200, mimetype='application/json')

@carts.route('/carts/<cartId>', methods=['DELETE'])
def deleteCart(cartId):
    try:
        cart_to_be_deleted = db.session.query(cart).filter(cart.id == cartId).one()
    except Exception as e:
        db.session.rollback()
        return not_found(cartId)
    else:
        db.session.query(cart).filter(cart.id == cartId).delete()
        db.session.commit()
        return Response(json.dumps({"deletedCartId" : str(cartId)}), status=200, mimetype='application/json')
    