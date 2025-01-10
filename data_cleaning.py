import pandas as pd

def load_and_merge_data():
    """
    Load raw datasets and merge them into a single DataFrame.
    Returns:
        order_prior (DataFrame): Merged dataset.
    """
    orders = pd.read_csv('data/orders.csv')
    order_products_prior = pd.read_csv('data/order_products__prior.csv')
    products = pd.read_csv('data/products.csv')
    aisles = pd.read_csv('data/aisles.csv')
    departments = pd.read_csv('data/departments.csv')

    # Merge datasets
    order_prior = pd.merge(order_products_prior, products, on='product_id', how='left')
    order_prior = pd.merge(order_prior, aisles, on='aisle_id', how='left')
    order_prior = pd.merge(order_prior, departments, on='department_id', how='left')
    order_prior = pd.merge(order_prior, orders, on='order_id', how='left')

    return order_prior

def clean_data(order_prior):
    """
    Perform cleaning steps on the merged dataset.
    Args:
        order_prior (DataFrame): Merged dataset.
    Returns:
        cleaned DataFrame.
    """
    order_prior.dropna(inplace=True)
    order_prior.drop_duplicates(inplace=True)
    return order_prior