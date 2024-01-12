# HR COB process statistics tool
<a href="https://twitter.com/giuseppewdev"> <img src = "https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fgiuseppewdev"> </a> <a href="https://dev.to/giuseppewdev"><img src="https://img.shields.io/badge/-DEV-black?logo=dev.to"></a>



#### Description


The COB/Unilav is an integral part of the Italian HR process, requiring employees to submit a filled form to employment centers at the conclusion of certain procedures. To gauge the effort employees invest in this process on a monthly or yearly basis, I have developed a tool.

Ideally, the tool is designed for annual assessments, but it can also be employed on a monthly basis. The user will be prompted to input the number of tickets submitted for each specific month, corresponding to processes that necessitate the COB/Unilav.

Upon entering all the information, the tool will generate three distinct files:

        1. Monthly Breakdown of Minutes Spent: This file details the time spent on each procedure for every month.

        2. Monthly Hours Dedicated to COB/Unilav: Provides an overview of the hours devoted to the COB/Unilav process each month.

        3. Percentage of Time Allocation: Displays the percentage of time spent on each procedure per month, with 100% representing a full 168 hours of work.

This tool serves as a comprehensive resource to understand and analyze the time and effort invested by employees in fulfilling COB/Unilav requirements, facilitating both monthly and yearly assessments.


## Installation :package:

<a href=https://www.python.org/ ><img src="https://img.shields.io/badge/-Python-white?logo=python"></a> <a href="https://matplotlib.org/"><img src="https://img.shields.io/badge/-Matplotlib-blue"></a>


<a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/-Visual%20Studio%20Code-0098ff?logo=visualstudiocode" ></a>



Then we import on COB.py all the following:

```python
from tkinter import *
from COB_class import Month

import matplotlib.pyplot as plt
import math
```

In the file COB_class.py we import:

```python 
import tkinter as tk
from tkinter import messagebox
```

No additional package are required.


#### List of the process that require the COB/Unilav

Hire or Rehire Full and Par times
Hire or Rehire an Internships Extracurricular
Contract Renewals
Transfer Internal Changes
Employee Termination
Injuries


#### Time spend in mm

HIRING = 15 mm
TERMINATION  = 10 mm
EXTENSION = 10 mm
INAIL= 30 mm
TRANSFORMATION = 10 mm

## Directory

In the directory project there are the following directories:

▪️ COB.py

▪️ COB_class.py

▪️ process_mm.png

▪️ monthly_hh.png

▪️ monthly_percent.png

▪️ README.md

▪️ .gitignore

▪️ LICENSE.md



## Design

The project (code) is on two file COB_class.py and COB.py.

In order to work with haft to import the COB_class.py inside our COB.py file.

```python
from COB_class import Month
```

In the file COB_class.py we have all the information that the user need to enter , (all process). The class use the library tkinter.

In the file COB.py we import the class COB_class.py and will create the plot to be displayed and stored in  the file process_mm.png , monthly_hh.png and monthly_percent.png



## Visuals

We can visualize the results on the file of this project :

▪️ process_mm.png

▪️ monthly_hh.png

▪️ monthly_percent.png



## License

<a href="https://github.com/Giuseppe-Bonifati/GamesForYou/blob/main/LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue"></a>
