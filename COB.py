from tkinter import *
from COB_class import Month

import matplotlib.pyplot as plt
import math






#create an empty directory to store for each months a key and a value , so we will have a dictionary of dictionary .
dic_months = {}

for _ in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"," November","December"]:
     #each time we loop on the class we will create a dictionary and the key will be the month
     month = Month(_)
     month.mainloop()
     #at the key position of the months ,we will add as the value another dictionary that come from the class.( the entry the we submit)
     dic_months[_] = month.process
     #in case we will close the window, the loop will stop and pop will remove the last month if it is empty
     if month.window_closed_manually:
            dic_months.pop(_)
            break




csv_file = 'user.csv'

#if there is no info in dic_months then pass else create and write the info in a csv file

if not dic_months:
     pass
else:
     # we will create the first plot with all information base on the minute we spend  , the result is coming correctly already from the class 
     num_rows = 4
     num_cols = 3

     # Create subplots
     fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))

     # Flatten the axes for easier iteration
     axes = axes.flatten()

     # Iterate over months and create a subplot for each
     for i, month in enumerate(dic_months.keys()):
          categories = list(dic_months[month].keys())
          values = [dic_months[month][category] if isinstance(dic_months[month][category], int) else 0 for category in categories]

          # Make the y-axis visible
          axes[i].tick_params(axis='y', which='both', left=True, right=False)

          # Plot on the corresponding subplot
          axes[i].bar(categories, values)
          axes[i].set_title(month)
          axes[i].set_ylabel('Count(mm)')

          # Display the numerical values on top of the bars
          for j, value in enumerate(values):
               axes[i].text(j, value, str(value), ha='center', va='bottom')

               # Rotate x-axis labels for better visibility
               axes[i].tick_params(axis='x', rotation=35)

     # Adjust layout for better spacing
     plt.tight_layout()
     #save the plot
     plt.savefig('process_mm.png')

     plt.show()




     #From here on we will start to create another plot to display the hours that we spend on each process
     count_hh = {}

     #loop to the dictionary that come from the class and we will store every value of inner dictionary inside count_hh and the key will be the outer dictionary
     for key, value in dic_months.items():
          number = 0
          for x,y in value.items():
               if y == "N/A":
                    number += 0
               else:
              
                    number += y   
          #to get the hours we will divide the min by 60
          count_hh[key] = number/60






     keys = list(count_hh.keys())
     values = list(count_hh.values())



     plt.barh(keys, values)
     plt.xlabel('Count(hh)')
     plt.ylabel('Keys')
     plt.title('Unilav per hours for each months ')

     # Display the numerical values on the right of the bars
     for i, value in enumerate(values):
          plt.text(value, i, f'{value:.2f}', ha='left', va='center')


     plt.savefig('monthly_hh.png')

     plt.show()



     #form here on we will start to create the last plot that will display the percentage
     count_percent = {}

     #we loop through the hours (count_hh) and we will calculate the percentage and will store key and value in count_percent
     for key, value in count_hh.items():  
          #we calculate the percentage based that 168 hours of work per months it is the 100 percent
          count_percent[key] = value/168*100

     

     # Calculate the number of rows and columns needed based on the number of plots
     num_plots = len(count_percent)
     #this is the percentage of break time in a months (3 hours in total if we count 15 min per day) 
     num_cols = 3 
     num_rows = math.ceil(num_plots / num_cols)

     # Create subplots
     fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 3 * num_rows))

     # Flatten the subplot grid into a 1D array for easy iteration
     axs = axs.flatten()

     # Loop through the dictionary and create a pie plot for each key-value pair
     for i, (key, value) in enumerate(count_percent.items()):
          # Calculate break time (assuming it's constant at 3 for each plot)
          break_time = 3
          
          # Create the pie plot with labels
          axs[i].pie([value, break_time, 100 - value - break_time], labels=["Unilavs", "Break", "Others"],
                         autopct='%1.1f%%', startangle=140)
          
          axs[i].set_title(key)

     # Adjust layout to prevent overlapping
     plt.tight_layout()

     plt.savefig('monthly_percent.png')

     # Show the plot
     plt.show()





















     # fig, axs = plt.subplots(2, 2, figsize=(10, 8))

     # # Flatten the 2x2 subplot grid into a 1D array for easy iteration
     # axs = axs.flatten()

     # # Loop through the dictionary and create a pie plot for each key-value pair
     # for i, (key, value) in enumerate(count_percent.items()):
     #      axs[i].pie([value, 100 - value], labels=["Unilavs","Others"], autopct='%1.1f%%', startangle=140)
     #      axs[i].set_title(key)

     # # Adjust layout to prevent overlapping
     # plt.tight_layout()

     # plt.savefig('monthly_percent.png')

     # # Show the plot
     # plt.show()