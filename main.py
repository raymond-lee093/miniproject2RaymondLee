# INF601 - Advanced Programming in Python
# Raymond Lee
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# What is the primary expenditure for Valentine's Day among Americans from 2010 to 2022?

# Create charts directory to store png files of graphs
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

##### Line graph

# Creates a dataframe and reads data from gifts_age.csv file and assigns it to giftsByAge_dat
giftsByAge_data = pd.read_csv("valentinesDayConsumerData/gifts_age.csv", index_col=0)

# Plot the line graph, edited arguments in method call
giftsByAge_data.plot(figsize=(12,12), linewidth=4, fontsize=22)

# Set y-axis limits
plt.ylim(0, 80)

# Set graph labels, edited arguments in method call
plt.xlabel("Age Group (years)", fontsize=17)
plt.ylabel("Spending Average (dollars)", fontsize=17)
plt.title("Years 2010 to 2022 Consumer Spending on Valentine\'s Day Gifts", pad=35, fontsize=22)
plt.legend(title='Gifts', title_fontsize=13, loc='upper right', fontsize=12)

# Set gridlines
plt.grid(True)

# Saving the line graph
savefile = "charts/" + "lineGraph" + ".png"
plt.savefig(savefile)

##### Bar graph

# Creates a dataframe and reads data from historical_spending.csv file and assigns it to giftsByAge_dat
histSpending_data = pd.read_csv("valentinesDayConsumerData/historical_spending.csv", index_col=0)

# Extract the year and prices columns
year = histSpending_data.index
prices = histSpending_data['PerPerson']

# Set figure size
plt.figure(figsize=(10, 6))

# Plot the bar graph
plt.bar(year, prices, color='pink')

# Set graph labels, edited arguments in method call
plt.xlabel("Years", fontsize=14.5)
plt.ylabel("Spending Average (dollars)", fontsize=14.5)
plt.title("Historical Spending on Valentine\'s Day (Per Person)", fontsize=17)

# Set the x-axis ticks to include all years
plt.xticks(year)

# Saving the bar graph
savefile = "charts/" + "barGraph" + ".png"
plt.savefig(savefile)

##### Scatter plot graph

# Continuation of using histSpending_data
# Drop the "PerPerson" and "PercentCelebrating" column
histSpending_data = histSpending_data.drop(columns=["PerPerson", "PercentCelebrating"])

# Set figure size
plt.figure(figsize=(10, 6))

# Plot the scatter plot
for column in histSpending_data.columns:
    # Set x value and y value for data, set label for legend, set size for dots on graph
    plt.scatter(histSpending_data.index, histSpending_data[column], label=column, s=100)

# Set graph labels, edited arguments in method call
plt.xlabel("Years", fontsize=14.5)
plt.ylabel("Spending Average (dollars)", fontsize=14.5)
plt.title("Historical Spending on Gifts for Valentine\'s Day ", fontsize=17)
plt.legend(title="Gifts", fontsize=7)

# Set y-axis limits
plt.ylim(0, 50)

# Set the x-axis ticks to include all years
plt.xticks(year)

# Set gridlines
plt.grid(True)

# Saving the scatter plot graph
savefile = "charts/" + "scatterPlot" + ".png"
plt.savefig(savefile)

##### Subplot graphs

# Creates a dataframe and reads data from gifts_gender.csv file and assigns it to giftsByAge_dat
giftsByGender_data = pd.read_csv("valentinesDayConsumerData/gifts_gender.csv", index_col=0)

# Transpose the DataFrame rows and column swap
transposed_data = giftsByGender_data.transpose()

# Set fontsize for the entire figure
plt.rcParams.update({'font.size': 12})

# Plot the subplot graphs, assign the objects, edited arguments in method call
subPlot_obj= transposed_data.plot.area(figsize=(12, 7), subplots=True, color=["teal", "purple"])

# Set graph labels, edited arguments in method call
plt.xlabel("Gifts", fontsize=15, labelpad=0)
plt.ylabel("Spending Average (dollars)", fontsize=15)
# Vertically set y-axis label
plt.gca().yaxis.set_label_coords(-0.07, 1)
# Set a single title for the entire figure
plt.suptitle("Years 2010 to 2022 Consumer Spending on Valentine\'s Day Gifts (Men vs. Women)",
             fontsize=18, y=0.95)
# Rotate x-axis tick labels by 45 degrees
plt.xticks(rotation=10)

# Set larger legend for both subplots
subPlot_obj[0].legend(fontsize=15)
subPlot_obj[1].legend(fontsize=15)

# Saving the subplot graphs
savefile = "charts/" + "subplotGraphs" + ".png"
plt.savefig(savefile)

# Show graphs
plt.show()

