from conn import getConn

def getProducts(connection):
    
    cursor = connection.cursor()

    query = "SELECT * FROM electro_store.products;"

    cursor.execute(query)

    response = [] 

    for (product_id, name, price_per_unit) in cursor:
        response.append(
            {
                "product_id": product_id,
                "name": name,
                "price_per_unit": price_per_unit
            }
        )

    return response

def insert_product(connection, product):
    cursor=connection.cursor()
    query=("INSERT INTO products "
           "(name, price_per_unit)"
           "VALUES (%s,%s);")
    data=(product['name'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor=connection.cursor()
    query=("DELETE FROM products WHERE product_id="+str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    connection=getConn()
    # print(getProducts(connection))

    # print(insert_product(connection, {
    #             "name": 'headphones',
    #             "price_per_unit": '4500'
    # }))

    print(delete_product(connection, 23))

