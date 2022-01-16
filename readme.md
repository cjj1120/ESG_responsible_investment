# Welcome to ESG Responsible Investing

[Competition Description that we can add at your own time]

## Setup
1. Open your Terminal or Powershell and change directory to your desktop (or any preferred work space). Note these instructions are primarily written for MacOS. WindowOS users can update this if needed.

    Type:

    ```cd Desktop```

2. Then clone the repo using 

    ```git clone <HTTPS link or SSH link>```

3. Create a virtual environment. This prevents the packages installed in this project to interfere with your other packages on your machine. Also, it makes it easier to standardize versions. It is also a good practice to ensure reproducibility, especially when collaborating on Github. 

    **3.1** Change your directory by entering the ESG_responsible_investing folder
    
    ```cd ESG_responsible_investing```

    **3.2** Once inside type ```python3 -m venv .```

    **3.3** To activate the virtual environment <br>
    For Mac: ```source bin/activate```<br>
    For Windows: ```Scripts\activate``` or refer to this [medium article](https://towardsdatascience.com/getting-started-with-python-virtual-environments-252a6bd2240)

    **3.4** When you need to install packages, just type 
    
    ```pip install <package name>```

    **3.5** If you downloaded a new package, push the new package into Github as well so we can download the new package as well. Generate the list of packages by running <br>
    For Mac: ```pip3 freeze > work/requirements.txt```<br>
    For Windows: ```pip freeze > work/requirements_windows.txt``` 

    **3.6** To download the packages from requirements.txt, run 
    
    ```pip install -r work/requirements.txt```

    [ I have pre-installed some packages for you to run ```jupyter lab``` or ```jupyter notebook``` ]

## Organization

We practice good file organization. We can be [hardcore](https://www.kdnuggets.com/2018/07/cookiecutter-data-science-organize-data-project.html) but at this point we keep it simple:

```
ESG_responsible_investing
|___ Work
     |___ data               # Stores the data
     |    |___ raw           # Raw data from a source. No data cleaning here
     |    |___ transform     # Tables that are joined, cleaned, normalized, denormalized etc. Most of your work should occur here
     |    |___ report        # These are tables that are used for Visualization. Very little to no transformation would occur here
     |____ src               # Runs scripts if needed
     |____ notebook          # For experimentation and rapid prototyping
     |     |___ Analysis     # Data exploration or ML modeling occurs here
     |     |___ ETL          # To transform data or create new tables. Little
     |___ mac_requirements.txt
     |___ requirements_windows.txt
     |___ ignore             # a miscellaneous folder for files to ignore
     |___ .gitignore         # List of files to ignore especially credentials!
```
The folders and directories may get messy from time to time so some clean up may be needed a long the way. The directory is likely to change over time as the project progresses

## Table Naming Convention
This is still work in progress but it would be something like this

**For OLTP applications**
* *Staging* prefix would be added if it is raw data. This is data with no preprocessing and are usually taken directly from source. This table should ***NEVER*** be used directly for queries or analytics.

* *NF* prefix are tables that undergo normalization where the data is intentionally split to allow for better data update, deletion, and insertion

**For OLAP applications**

These are tables are designed for analysis. They are denormalize and are usually used for aggregations and reduction of joins. They have duplicated values in some rows by design

* *dim* prefix are information pertaining a something i.e 
* *fact* prefix are information that records a certain historical event such as transactional events