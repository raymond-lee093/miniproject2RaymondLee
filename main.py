# INF601 - Advanced Programming in Python
# Raymond Lee
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#(5/5 points) Proper import of packages used.
#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve such as:
#"How many homes in the US have access to 100Mbps Internet or more?"
#"How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
#Here are some other great datasets: https://www.kaggle.com/datasets
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

# From years 2010-2022, What do people in the United States spend the most money on for Valentine's Day?

# Create charts directory to store png files of graphs
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

##### Graph 1

# Reads data in gifts_age.csv file and assigns it to giftsByAge_dat
giftsByAge_data = pd.read_csv("valentinesDayConsumerData/gifts_age.csv", index_col=0)

# Plot the line graph, edited arguments in method call
giftsByAge_data.plot(figsize=(12,12), linewidth=4, fontsize=22)

# Set y-axis limits
plt.ylim(0, 80)

# Set graph labels, edited arguments in method call
plt.xlabel("Age Group (years)", fontsize=17)
plt.ylabel("Spending Average (dollars)", fontsize=17)
plt.title("Years 2010 to 2022 Consumer Spending patterns on Valentine\'s Day Gifts", pad=35, fontsize=22)
plt.legend(title='Gifts', title_fontsize=13, loc='upper right', fontsize=12)

# Set gridlines
plt.grid(True)

# Saving the Graph 1
savefile = "charts/" + "lineGraph" + ".png"
plt.savefig(savefile)

##### Graph 2

# Reads data in historical_spending.csv file and assigns it to giftsByAge_dat
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

# Saving the Graph 2
savefile = "charts/" + "barGraph" + ".png"
plt.savefig(savefile)

##### Graph 3

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

# Saving the Graph 3
savefile = "charts/" + "scatterPlot" + ".png"
plt.savefig(savefile)

##### Graph 4 and 5

# Reads data in gifts_gender.csv file and assigns it to giftsByAge_dat
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
plt.suptitle("Years 2010 to 2022 Consumer Spending patterns on Valentine\'s Day Gifts (Men vs. Women)",
             fontsize=18, y=0.95)
# Rotate x-axis tick labels by 45 degrees
plt.xticks(rotation=10)

# Set larger legend for both subplots
subPlot_obj[0].legend(fontsize=15)
subPlot_obj[1].legend(fontsize=15)

# Saving the Graph 4 and Graph5
savefile = "charts/" + "subplotGraphs" + ".png"
plt.savefig(savefile)

# Show graphs
plt.show()

