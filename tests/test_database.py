from database.db_client import DatabaseClient


def test_product_database():

    db = DatabaseClient()

    db.create_products_table()

    db.add_product(
        1,
        "Sauce Labs Backpack",
        29.99
    )

    product = db.get_product(1)

    assert product is not None

    assert product[0] == 1
    assert product[1] == "Sauce Labs Backpack"
    assert product[2] == 29.99

    db.close()