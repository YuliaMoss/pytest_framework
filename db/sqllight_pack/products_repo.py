from db.sqllight_pack._base_db_connector import BaseDBConnection


class ProductsRepo:
    def __init__(self, db_params):
        self._db = BaseDBConnection(db_params)
        self._table_name = 'PRODUCTS'

    def get_all(self):
        res = self._db.conn.execute(f"SELECT * FROM {self._table_name}")
        return res.fetchall()

    def get_one_by_id(self, product_id: int):
        res = self._db.conn.execute(f"SELECT * FROM {self._table_name} WHERE id={product_id}")
        prod = res.fetchone()
        return prod

    def get_products_by_country(self):
        res = self._db.conn.execute(f"SELECT * FROM {self._table_name} WHERE country_of_origin='USA';")
        return res.fetchall()

    def get_one_in_tuple_by_id(self, product_id: int):
        res = self._db.conn.execute(f"SELECT * FROM {self._table_name} WHERE id={product_id}")
        prod = res.fetchone()
        return prod

    def insert_one(self, product_id: int, product_name: str, category: str, brand: str, price: float, quantity: int,
                   country_of_origin: str):
        query_insert = f'''
            INSERT INTO {self._table_name} (ID,PRODUCT_NAME,CATEGORY,BRAND,PRICE,QUANTITY,COUNTRY_OF_ORIGIN)
            VALUES ({product_id}, '{product_name}', '{category}', '{brand}', {price}, {quantity}, 
            '{country_of_origin}');
            '''
        self._db.conn.execute(query_insert)
        self._db.conn.commit()

    def product_exists(self, product_id: int) -> bool:
        query_check = f"SELECT 1 FROM {self._table_name} WHERE id = ?"
        result = self._db.conn.execute(query_check, (product_id,)).fetchone()
        return result is not None

    def update_quantity(self, product_id: int, new_quantity: int):
        if not self.product_exists(product_id):
            print(f"Product with ID {product_id} does not exist.")
            return
        else:
            query_update = f'''UPDATE {self._table_name}
                              SET quantity=?
                              WHERE id=?'''
            self._db.conn.execute(query_update, (new_quantity, product_id))
            self._db.conn.commit()
            updated_product = self.get_one_in_tuple_by_id(product_id)
            return updated_product

    def delete_one(self, product_id: int):
        if not self.product_exists(product_id):
            print(f"Product with ID {product_id} does not exist.")
            return
        else:
            query = f"DELETE FROM {self._table_name} WHERE ID = ?"
            self._db.conn.execute(query, (product_id,))
            self._db.conn.commit()

    def insert_many(self, data):
        # Assuming each item in data is a tuple representing a product
        query = f"INSERT INTO {self._table_name} VALUES (?, ?, ?, ?, ?, ?, ?)"
        self._db.conn.executemany(query, data)
        self._db.conn.commit()

    def insert_minimal_product(self, product_id: int, product_name: str):
        query_insert = f'''
            INSERT INTO {self._table_name} (ID, PRODUCT_NAME, PRICE, QUANTITY, COUNTRY_OF_ORIGIN)
            VALUES ({product_id}, '{product_name}', NULL, NULL, NULL);
        '''
        self._db.conn.execute(query_insert)
        self._db.conn.commit()

    def __del__(self):
        pass

    def close_connection(self):
        self._db.cursor.close()
        self._db.conn.close()
