from mlxtend.frequent_patterns import apriori, association_rules

def run_market_basket_analysis(data, min_support=0.02, lift_threshold=1.2):
    """
    Perform Market Basket Analysis using the Apriori algorithm.
    Args:
        data (DataFrame): Transactional data with one-hot encoded products.
        min_support (float): Minimum support threshold.
        lift_threshold (float): Minimum lift threshold.
    Returns:
        rules (DataFrame): Generated association rules.
    """
    # Apply Apriori
    frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric='lift', min_threshold=lift_threshold)
    return rules
