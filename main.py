import csv
import matplotlib.pyplot as plt
import sys
from typing import List


def read_csv_file(file_name: str) -> List[List[str]]:
    lines = csv.reader(open(file_name))
    data = list(lines)
    return data


# we follow the format as present below:
#   1. sepal length in cm
#   2. sepal width in cm
#   3. petal length in cm
#   4. petal width in cm
#   5. class:
#      -- Iris Setosa
#      -- Iris Versicolour
#      -- Iris Virginica
def parse_csv_data(data:List[List[str]]) -> dict:
    format_data = {"Iris-setosa": [],
                   "Iris-versicolor": [],
                   "Iris-virginica": []}


    for x in data:
        try:
            temp = [float(x[0]), float(x[1]), float(x[2]), float(x[3])]
        except:
            print("csv file has wrong format, please check the readme!")
            exit(1)

        if x[4] == "Iris-setosa":
            format_data["Iris-setosa"].append(temp)
        elif x[4] == "Iris-versicolor":
            format_data["Iris-versicolor"].append(temp)
        elif x[4] == "Iris-virginica":
            format_data["Iris-virginica"].append(temp)

    return format_data


# advance function it would not limit to the only class provided in data.csv
def parse_csv_data_adv(data:List[List[str]]) -> dict:
    format_data = {}

    for x in data:
        try:
            temp = [float(x[0]), float(x[1]), float(x[2]), float(x[3])]
        except:
            print("csv file has wrong format, please check the readme!")
            exit(1)

        print(temp, format_data.get(x[4]))
        # if the key class is not there create the arr
        if format_data.get(x[4]) == None:
            format_data[x[4]] = []
        #     format_data[x[4]].append(temp)
        # else:

        format_data[x[4]].append(temp)

        print(format_data)
    return format_data



# loop over what we fetch in csv and return the average of sepal length
# petal length and corrospond to class
def proccess_data(data:dict) -> (List[float], List[float], List[str]):
    sepal_arr = []
    petal_arr = []
    class_arr = []

    for cla in data:
        sepal_length = 0
        # sepal_width = 0
        petal_length = 0
        # petal_width = 0
        for x in data[cla]:
            sepal_length += x[0]
            # sepal_width += x[1]
            petal_length += x[2]
            # petal_width += x[3]

        # get avg
        count = len(data[cla])
        sepal_avg = 0
        petal_avg = 0

        # if we dont have target class
        if count != 0:
            sepal_avg = round(sepal_length / count, 3)
            petal_avg = round(petal_length / count, 3)

        # output the result
        print("Class: ", cla)
        print("Average sepal length: ", sepal_avg)
        print("Average petal length: ", petal_avg)
        print("\n")

        # push into arr
        sepal_arr.append(sepal_avg)
        petal_arr.append(petal_avg)
        class_arr.append(cla)

    return sepal_arr, petal_arr, class_arr


def plot_graph(sepal_arr:List[float], petal_arr:List[float], class_arr:List[str]):
    # create plot
    fig = plt.figure()
    fig.subplots_adjust(hspace=.5)

    ax = fig.add_subplot(211)
    ax.set_title("Average Sepal Length")
    plt.xlabel("Class Type")
    plt.ylabel("Average(cm)")

    # set the x-axis with string
    x = []
    for i in range(len(class_arr)):
        x.append(i + 1)
    plt.xticks(x, class_arr)

    # set range
    plt.ylim(min(sepal_arr) - 0.5, max(sepal_arr) + 0.5)
    plt.xlim(0.5, len(class_arr) + 0.5)

    plt.plot(x, sepal_arr, x, sepal_arr, 'ro')
    # label the point val
    for i in range(len(sepal_arr)):
        ax.annotate(sepal_arr[i], (x[i], sepal_arr[i]))

    plt.grid()

    # another plot
    ax = fig.add_subplot(212)
    ax.set_title("Average Petal Length")
    plt.xlabel("Class Type")
    plt.ylabel("Average(cm)")

    # set range
    plt.ylim(min(petal_arr) - 0.5, max(petal_arr) + 0.5)
    plt.xlim(0.5, len(class_arr) + 0.5)

    plt.xticks(x, class_arr)
    plt.plot(x, petal_arr, x, petal_arr, 'ro')
    # label the point val
    for i in range(len(petal_arr)):
        ax.annotate(petal_arr[i], (x[i], petal_arr[i]))

    plt.grid()
    # plt.show()
    plt.savefig("data.png")


def do_polt(file_name: str):
    # read file from target csv
    data = read_csv_file(file_name)

    # sort the data for three class
    format_data = parse_csv_data(data)
    # format_data = parse_csv_data_adv(data)

    # get the average data
    sepal_arr, petal_arr, class_arr = proccess_data(format_data)

    # use average data to plot
    plot_graph(sepal_arr, petal_arr, class_arr)

    return

def main():
    # Default file
    file_name = "data.csv"
    if len(sys.argv) > 1:
        file_name = sys.argv[1]


    do_polt(file_name)


if __name__ == '__main__':
    main()