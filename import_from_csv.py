import csv
import numpy
fieldnames = ['id', 'gestational_age', 'abdominal_circumference']
from matplotlib import pyplot

def open_csv(file):
    feature_string=''
    result_string=''
    x_axis = []
    y_axis = []

    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            x_axis.append(row['gestational_age'])
            y_axis.append(row['abdominal_circumference'])
            feature_string += row['gestational_age'] + ';'
            result_string += row['abdominal_circumference'] + ';'

        #Strings used for creating the matrix using the string populated from the csv file.

        feature_string = feature_string[0:len(feature_string)-1]
        result_string = result_string[0:len(result_string) - 1]
        feature_vector = numpy.matrix(feature_string)
        result_vector = numpy.matrix(result_string)



        show_plot(x_axis,y_axis)

        return (feature_vector, result_vector)


def show_plot(x_axis, y_axis):
    linear_regression_model = numpy.linspace(0, 100, 100)

    pyplot.plot(x_axis, y_axis, 'r.')
    pyplot.axis()

    pyplot.plot(8.49189782 * linear_regression_model)

    pyplot.xlabel('Gestational Age')
    pyplot.ylabel('Abdominal Circumference')
    pyplot.show()


