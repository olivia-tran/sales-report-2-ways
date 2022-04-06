"""Generate sales report showing total melons each salesperson sold."""


def get_melons_sold_by_salesperson(filepath):
    """accept a txt data file, return a dictionary of salespeople and their melon sales """
    melon_sales_data = {}

    with open(filepath) as f:
        for line in f:
            line = line.rstrip()
            salesperson_name, total_dollars, melons_sold = line.split('|')
            if salesperson_name in melon_sales_data:
                melon_sales_data[salesperson_name] += int(melons_sold)
            melon_sales_data[salesperson_name] = int(melons_sold)
            # melon_sales_data = sorted(melon_sales_data)
        return melon_sales_data


def print_sales_report(melons_sold_by_salesperson):
    """accept a dictionary of melon sales by salesperson, print a sales report based on the data"""
    for salesperson_name, melons_sold in melons_sold_by_salesperson.items():
        print(f'{salesperson_name} sold {melons_sold} melons. ')


print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))
