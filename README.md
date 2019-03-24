

# Analysis Data
Parse CSV data


# Geting Start

The program use the Python3 to process all the data, to install Python3:
```
	$ sudo apt-get update
	$ sudo apt-get install python3.6
```

To make sure the python-matplotlib is installed:
```
	$ sudo apt-get install python-matplotlib
```

To run the program and get the graph, type below in the terminal:
```
	$ python3.5 main.py <your-csv-file>
```

in default, the program would use the data in `data.csv`, as user does not input csv file:
```
	$ python3.5 main.py
```
And output image would like:
<img src="https://github.com/colorzzr/indoc_research/image/sample.png" />


# Function

Below are the detail of each function
---

## def do_polt(file_name: str):

The function take the user input calls all functions below to process the data in csv file and output the png for the user
---

## def read_csv_file(file_name: str) -> List[List[str]]:

function would take the arg in the terminal and open it for the function `parse_csv_data`
---

## def parse_csv_data(data:List[List[str]]) -> dict:

function read line by line throughout the file and put the required data into the dictionary. the key of dictionary is the class of the flower. The format of scv must follow below:

	- Attribute 1: sepal length in cm
	- Attribute 2: sepal width in cm
	- Attribute 3: petal length in cm
	- Attribute 4: petal width in cm
	- Attribute 5: class:
		-- Iris Setosa
      	-- Iris Versicolour
      	-- Iris Virginica

### Error Shooting:
---


## def proccess_data(data:dict) -> (List[float], List[float], List[str]):

Function takes the analysised data.It calculate and return the array containning the average of sepal length, petal length and corresponding to each class

## def plot_graph(sepal_arr:List[float], petal_arr:List[float], class_arr:List[str]):

Function using `python-matplotlib` to plot the graph and output png file called `data.png`








