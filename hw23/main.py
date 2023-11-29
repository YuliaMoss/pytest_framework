from constants import ROOT_PATH
from utilities.sqlite_cm import Sqlite

if __name__ == '__main__':
    with Sqlite(f'{ROOT_PATH}/db/test.db') as c:
        query_create = '''
        CREATE TABLE PRODUCTS
        (ID INT PRIMARY     KEY     NOT NULL,
        PRODUCT_NAME        TEXT    NOT NULL,
        CATEGORY            TEXT    NOT NULL,
        BRAND               TEXT    NOT NULL,
        PRICE               REAL,
        QUANTITY            INT,
        COUNTRY_OF_ORIGIN   CHAR(50));
        '''

        c.execute(query_create)
        query_insert = '''
        INSERT INTO PRODUCTS (ID,PRODUCT_NAME,CATEGORY,BRAND,PRICE,QUANTITY,COUNTRY_OF_ORIGIN)
        VALUES 
        (1, 'Laptop ASUS XPS 15', 'Computers', 'ASUS', 1200.00, 10, 'Taiwan'),
        (2, 'Laptop Dell XPS 13', 'Computers', 'Dell', 300.00, 7, 'USA'),
        (3, 'Laptop HP Spectre x360', 'Computers', 'HP', 1200.00, 5, 'USA'),
        (4, 'Smartphone Samsung Galaxy S21', 'Smartphones', 'Samsung', 700.00, 20, 'South Korea'),
        (5, 'Smartphone Apple iPhone 13', 'Smartphones', 'Apple', 999.00, 10, 'USA'),
        (6, 'Camera Canon EOS R5', 'Photography Equipment', 'Canon', 800.00, 5, 'Japan'),
        (7, 'Camera Nikon Z6', 'Photography Equipment', 'Nikon', 150.00, 8, 'Japan'),
        (8, 'Monitor Dell UltraSharp U2719D', 'Monitors', 'Dell', 300.00, 10, 'USA'),
        (9, 'Router TP-Link Archer C7', 'Networking Equipment', 'TP-Link', 80.00, 15, 'China'),
        (10, 'USB Flash Drive SanDisk Ultra 64G', 'Computer Accessories', 'SanDisk', 20.00, 25,  'USA'),
        (11, 'Electric Kettle Philips HD9306/03', 'Home Appliances', 'Philips', 30.00, 20, 'Netherlands'),
        (12, 'Portable Speaker JBL Charge 4', 'Audio Equipment', 'JBL', 100.00, 10, 'USA'),
        (13, 'Printer HP LaserJet Pro M404dn', 'Office Equipment', 'HP', 200.00, 7, 'USA'),
        (14, 'Gaming Mouse Logitech G Pro', 'Gaming', 'Logitech', 60.00, 12, 'Switzerland'),
        (15, 'Headphones Sony WH-1000XM4', 'Audio Equipment', 'Sony', 150.00, 18, 'Japan'),
        (16, 'TV Sony Bravia X900H', 'Televisions', 'Sony', 1000.00, 8, 'Japan'),
        (17, 'Printer HP LaserJet Pro M404dn', 'Office Equipment', 'HP', 'LaserJet Pro M404dn', 299.00, 5, 'USA'),
        (18, 'Printer Canon PIXMA MX922', 'Office Equipment', 'Canon', 'PIXMA MX922', 199.00, 8, 'Japan'),
        (19, 'Headphones Sony WH-1000XM4', 'Audio Equipment', 'Sony', 'WH-1000XM4', 349.00, 10, 'Japan')
        (20, 'Headphones Bose QuietComfort 35 II', 'Audio Equipment', 'Bose', 'QuietComfort 35 II', 299.00, 7, 'USA');
        '''

        c.execute(query_insert)
        res = c.execute("SELECT * FROM PRODUCTS")
        print(res.fetchall())

        # (8, 'Monitor Dell UltraSharp U2719D', 'Monitors', 'Dell', 300.00, 10, 'USA'),
        # (9, 'Router TP-Link Archer C7', 'Networking Equipment', 'TP-Link', 80.00, 15, 'China'),
        # (10, 'USB Flash Drive SanDisk Ultra 64G', 'Computer Accessories', 'SanDisk', 20.00, 25,  'USA'),
        # (11, 'Electric Kettle Philips HD9306/03', 'Home Appliances', 'Philips', 30.00, 20, 'Netherlands'),
        # (12, 'Portable Speaker JBL Charge 4', 'Audio Equipment', 'JBL', 100.00, 10, 'USA'),
        # (13, 'Printer HP LaserJet Pro M404dn', 'Office Equipment', 'HP', 200.00, 7, 'USA'),
        # (14, 'Gaming Mouse Logitech G Pro', 'Gaming', 'Logitech', 60.00, 12, 'Switzerland'),
        # (15, 'Headphones Sony WH-1000XM4', 'Audio Equipment', 'Sony', 150.00, 18, 'Japan'),
        # (16, 'TV Sony Bravia X900H', 'Televisions', 'Sony', 1000.00, 8, 'Japan'),
        # (17, 'Printer HP LaserJet Pro M404dn', 'Office Equipment', 'HP', 'LaserJet Pro M404dn', 299.00, 5, 'USA'),
        # (18, 'Printer Canon PIXMA MX922', 'Office Equipment', 'Canon', 'PIXMA MX922', 199.00, 8, 'Japan'),
        # (19, 'Headphones Sony WH-1000XM4', 'Audio Equipment', 'Sony', 'WH-1000XM4', 349.00, 10, 'Japan')
        # (20, 'Headphones Bose QuietComfort 35 II', 'Audio Equipment', 'Bose', 'QuietComfort 35 II', 299.00, 7, 'USA')
