def calculate_income_tax(taxable_income):
    # Define the tax rates and income thresholds
    rate1 = 0.0
    rate2 = 0.10
    rate3 = 0.20
    threshold1 = 10000
    threshold2 = 20000

# Calculate income tax
    if taxable_income <= threshold1:
        income_tax = taxable_income * rate1
    elif threshold1 < taxable_income <= threshold2:
        income_tax = (threshold1 * rate1) + ((taxable_income - threshold1) * rate2)
    else:
        income_tax = (threshold1 * rate1) + (threshold2 * rate2) + ((taxable_income - threshold2) * rate3)

    return income_tax
# Test case

# Print the result

