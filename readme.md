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
    
    ``````

    **3.6** To download the packages from requirements.txt, run 
    
    ```pip install -r work/requirements.txt```

    [ I have pre-installed some packages for you to run ```jupyter lab``` or ```jupyter notebook``` ]

## Organization

We practice good file organization. We can be [hardcore](https://www.kdnuggets.com/2018/07/cookiecutter-data-science-organize-data-project.html) but at this point we keep it simple:

```
ESG_responsible_investing
|___ data              # Stores the data
|___ src               # Runs scripts if needed
|___ notebook          # For experimentation and rapid prototyping
|___ requirements.txt
|___ ignore            # a miscellaneous folder for files to ignore
|___ .gitignore        # List of files to ignore especially credentials!
```
The folders and directories may get messy from time to time so some clean up may be needed a long the way. The directory is likely to change over time as the project progresses
