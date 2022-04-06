"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
# open file in filepath
f = open('sales-report.txt')
# salesperson name, sales_result, melon quantity
for line in f:  # loop over each line in file object
    line = line.rstrip()  # remove trailing whitespace
    entries = line.split('|')  # split each line by | to create a list of data
    salesperson = entries[0]  # get salesperson name by indexing
    melons = int(entries[2])  # number of melons they sold

    if salesperson in salespeople:

        # if salesperson is already in salespeople, increment the no of melons sold
        # list.index(list-item) return first index of value
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
# otherwise add the person's name to salespeople and melons to melons sold
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# loop over indices of sales people to print out info
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
