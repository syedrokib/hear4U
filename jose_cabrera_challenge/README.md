# jose-cabrera-challenge

* This is a simple server side web api for an online market place application.
* The api uses a Postgres database and the python Flask Framework.

## Installation
* To run this on your computer you must first install [docker](https://docs.docker.com/engine/installation/).
* Once Docker is installed, run the following command: `cd jose_cabrera_challenge && docker-compose up --build -d`
* The application will be ready to use in `localhost:5000` port

## Running
* After the application has been installed, use this commands to run and stop the application.
* Upon start, a data base initialization sequence will seed sample data in the db, so the endpoints
can be tested immediately after.
```c 
	docker-compose up --build -d   # Run the container.

	docker-compose down   # Stop and remove everything.
```

## Testing
* Testing GET endpoints and `Purchase` through Cart feature (Based on recently seeded data):
	* Hit `GET` product endpoints: 
		* `localhost:5000/products` vs `localhost:5000/products?inStock=true`
		* `localhost:5000/products/2`
	* Hit `GET` cart endpoints:
		* `localhost:5000/carts`
		* `localhost:5000/carts/2`
	* Hit `POST` purchase endpoints.
		* Cart with product with enough items:
			```c
				{
					"cartId" : "1"
				}			 
			```
		* Hit `GET` `localhost:5000/products/1` and notice reduction of `inventoryCount`
		* Cart with product without enough items (Notice response):
			```c
				{
					"cartId" : "2"
				}			 
			```
		* Hit `GET` `localhost:5000/products/2` and notice no modification of `inventoryCount`
		
* Please see below for detailed list of `Endpoints` with `Example` Request and Responses.



## Added Feature
* Carts are composed of a list of `productId` and `quantity`. You can purchase `quantity` number of products in a single
server request. There is validation to make sure that the `quantity` specified in the `cart` does not surpass the `product` stock.


## Product Endpoints & Examples
* [GET] /products || [GET] /products?inStock=true
    * Will fetch all existing `products`. If no products are found it will return an empty list.
    * If `inStock` query parameter is set to `true`, the response will only include products with `inventoryCount` > 0.
    * Example Response:
    ```c
        [
            {
                "id": 1,
                "invetoryCount": 3,
                "price": 50,
                "title": "The Legend of Zelda: Ocarina Of Time"
            },
            {
                "id": 2,
                "invetoryCount": 1,
                "price": 5,
                "title": "E.T The Extra Terrestial Atari"
            },
            {
                "id": 3,
                "invetoryCount": 1,
                "price": 25,
                "title": "Pokemon Emerald Version"
            }
        ]
    ```
    
* [GET] /product/{productId}
    * Will fetch the product that matches the specified `{productId}` .
    * Example Response for `/product/1`:
    ```c
        {
            "id": 1,
            "invetoryCount": 3,
            "price": 50,
            "title": "The Legend of Zelda: Ocarina Of Time"
        }
    ```
    
* [POST] /product
    * Will create a product
    * Example Request:
    ```c
        {
            "title" : "Super Metroid",
            "price" : 50,
            "inventoryCount" : 3
        }
    ``` 
    * Example Response:
    ```c
        {
            "createdProductId": {id}
        }
    ```
    
* [PUT] /product/{productId}
    * Will update an existing Product
    * Cannot only update `title` and `price` since `inventoryCount` can only be updated when the product is purchased.
    * Example Request:
    ```c
        {
            "title" : "Super Metroid",
            "price" : 25
        }
    ```
    * Example Response:
    ```c 
        {
            "updatedProductId": {id}
        }
    ```
* [DELETE] /product/{productId}
    * Will delete an existing Product with the provided `productId`.
    ```c 
        {
            "deletedProductId": {id}
        }
    ```
    
## Cart Endpoints & Examples
* [GET] /carts
    * Will fetch all existing `carts`. If no carts are found it will return an empty list.
    * `totalPrice` will be calculated based both in the `quantity` and `price` of each `product` in the `Cart`.
    * Example Response:
    ```c
        [
            {
                "id": "1",
                "products": [
                    {
                        "productId": 1,
                        "quantity": 1
                    }
                ],
                "totalPrice": 50
            },
            {
                "id": "2",
                "products": [
                    {
                        "productId": 2,
                        "quantity": 2
                    }
                ],
                "totalPrice": 10
            },
            {
                "id": "3",
                "products": [
                    {
                        "productId": 3,
                        "quantity": 3
                    }
                ],
                "totalPrice": 75
            }
        ]
    ```
    
* [GET] /carts/{cartId}
    * Will fetch the cartId that matches the specified `{cartId}` .
    * `totalPrice` will be calculated based both in the `quantity` and `price` of each `product` in the `Cart`.
    * Example Response for `/carts/1`:
    ```c
        {
            "id": "1",
            "products": [
                {
                    "productId": 1,
                    "quantity": 1
                }
            ],
            "totalPrice": 50
        }
    ```
    
* [POST] /carts
    * Will create a cart based on the provided list of products.
    * Uses uuid4() to generate the cart `id`.
    * Example Request:
    ```c
        [
            {
                "productId" : 1,
                "quantity": 2
            },
            {
                "productId" : 2,
                "quantity": 1
            }
        ]
    ``` 
    * Example Response:
    ```c
        {
            "createdCartId": {id}
        }
    ```
    
* [PUT] /cart/{cartId}
    * Will only update the `quantity` specified for a `product`.
    * Example Request:
    ```c
        [
            {
                "productId" : 1,
                "quantity": 555
            },
            {
                "productId" : 2,
                "quantity": 666
            }
        ]
    ```
    * Example Response:
    ```c 
        {
            "updatedCartId": {id}
        }
    ```
* [DELETE] /cart/{cartId}
    * Will delete an existing Cart with the provided `cartId`.
    * Example Response:
    ```c 
        {
            "deletedCartId": {id}
        }
    ```
    
## Purchases Endpoints & Examples
* [POST] /purchases
    * Will perform a purchase (decrease the `invetoryCount` of a product) based on `Cart` information of `productId`
    and `quantity`.
    * Will only succeed if there is enough number of `product` for the specified `quantity`
    * Example Request:
    ```c 
        {
            "cartId" : "{id}"
        }
    ```
    * Example successful Response:
    ```c
        {
            "cartPurchased": "{id}",
            "cartDetails": {
                "id": "{id}",
                "products": [
                    {
                        "productId": {productId},
                        "quantity": 2
                    }
                ],
                "totalPrice": 10
            }
        }
     
    ```
    * Example of not enough items Response:
    ```c 
        {
            "error": "Not enough stock for 2 unit(s) of product: 2"
        }
    ```
