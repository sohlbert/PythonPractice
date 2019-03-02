
#%%
import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join(r"C:\Users\sohlb\OneDrive\Desktop\NUCHI201902DATA1\Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv")

#%%
#The total number of months included in the dataset
###The net total amount of "Profit/Losses" over the entire period 
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


#%%
budget_data = r"C:\Users\sohlb\OneDrive\Desktop\NUCHI201902DATA1\Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"
budget_data = read_csv(budget_data)
#budget_data_pd.head(10)
#budget_data_pd.describe


#%%
#Calculating the total number of months included in the dataset

#budget_data_pd.head()
#Date = budget_data_pd["Date"]
#Date
#budget_data.len()
#row_count = sum(1 for row in budget_data)
#row_count
#budget_data["Date"].value_counts()
#count = budget_data_pd["Date"].len()
#count
#budget_data_pd.columns
Total_Months = len(budget_data_pd["Date"].unique())
print("Total Months:", Total_Months)


#%%
#The net total amount of "Profit/Losses" over the entire period

Gross_Margin = budget_data_pd["Profit/Losses"].sum()
print('Total Margin is: ${:,}'.format(Gross_Margin))


#%%
#The average of the changes in "Profit/Losses" over the entire period##
##For the PyBank portion of the assignment, the "Average Change" refers to the average difference in "Profit/Losses" 
###between each row. You will not get the right answer if you just take an average of the entire column
####- calculate the differences (row2-row1, row3-row2, row4-row3, etc), and then take an average of those values.

average = budget_data_pd["Profit/Losses"].mean()
print('Average Change in Margin by Month is: ${:,.2f}'.format(average))


#%%
#The greatest increase in profits (date and amount) over the entire period


#%%
#The greatest decrease in losses (date and amount) over the entire period


#%%
# Place all of the data found into a summary DataFrame
summary_table = pd.DataFrame({"Total Months": Total_Months,
                              "Total Margin": Gross_Margin,
                              "Average Change": average,
                              "Greatest Increase in Profits": "Answer Here",
                              "Greatest Decrease in Profits": "Answer Here"})
summary_table


#%%
# Export file as a CSV, without the Pandas index, but with the header
#file_one_df.to_csv("Output/fileOne.csv", index=False, header=True)

