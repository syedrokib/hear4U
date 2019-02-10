from . import products
from flask import Flask, request, json, Response
from src import db
from src.models.cart import cart
from src.models.product import product, build_product_object

@products.errorhandler(404)
def not_found(id):
    message = {
        'status': 404,
        'message': 'Product:' + id + ' Not Found.'
    }
    return Response( json.dumps(message) , status=404, mimetype='application/json')

@products.route('/products', methods=['GET'])
def getAllProducts():
    if request.args.get('inStock', None) == 'true':
        all_products = product.query.filter(product.inventory_count > 0).all()
    else:
        all_products = product.query.all()
    
    all_products_response = []
    for prod in all_products:
        all_products_response.append(build_product_object(prod))
    
    return Response(json.dumps(all_products_response), status=200, mimetype='application/json')


@products.route('/products/<productId>', methods=['GET'])
def getProduct(productId):
    try:
        prod = product.query.filter_by(id=productId).one()
    except Exception:
        return not_found(productId)
    else:
        return Response(json.dumps(build_product_object(prod)), status=200, mimetype='application/json')


@products.route('/products', methods=['POST'])
def createProduct():
    data = request.get_json()
    product_id = None
    try:
        product_object = product(title=data['title'], price=data['price'], inventory_count=data['inventoryCount'])
        db.session.add(product_object)
        db.session.commit()
        product_id = product_object.id
    except Exception as e:
        db.session.rollback()
        return Response(json.dumps({"error" : str(e)}), status=500, mimetype='application/json')
    return Response(json.dumps({"createdProductId" : productId}), status=200, mimetype='application/json')

@products.route('/products/<productId>', methods=['PUT'])
def updateProduct(productId):
    data = request.get_json()
    try:
        product_to_be_updated = db.session.query(product).filter(product.id == productId).one()
    except Exception:
        return not_found(productId)
    else:
        product_to_be_updated.title = data['title']
        product_to_be_updated.price = data['price']
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return Response(json.dumps({"error" : str(e)}), status=500, mimetype='application/json')
    return Response(json.dumps({"updatedProductId" : productId}), status=200, mimetype='application/json')

@products.route('/products/<productId>', methods=['DELETE'])
def deleteProduct(productId):
    try:
        product_to_be_deleted = db.session.query(product).filter(product.id == productId).one()
    except Exception :
        return not_found(productId)
    else:
        db.session.delete(product_to_be_deleted)
        db.session.commit()
        # propagates deletion to cart objects containing this product
        products_from_cart_to_be_deleted = db.session.query(cart).filter(cart.product_id == productId).all()
        for products in products_from_cart_to_be_deleted:
            db.session.delete(products)
        db.session.commit()
    return Response(json.dumps({"deletedProductId" : productId}), status=200, mimetype='application/json')

