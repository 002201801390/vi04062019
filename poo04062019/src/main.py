import csv
import itertools
import numpy

from bokeh.plotting import figure, output_file, show

# colors
colors = itertools.cycle(["#FF6200", "#7B00FF", "#0056B8", "#00B333"])

# output to static HTML file
output_file("../result_set/ideb_f1.html")

# range of years
min_year = 2005
max_year = 2021

ano = range(min_year, max_year, 2)

# create a new plot
plot = figure(
    tools='pan, box_zoom, reset, save',
    title='Análise IDEB - Fundamental 1',
    plot_width=1280, plot_height=680,
    x_range=[min_year - 1, max_year + 4],
    y_axis_type="log",
    x_axis_label='Ano',
    y_axis_label='Nota do IDEB'
)

# Fundamental 1
# Goal
with open('../data_set/ideb_f1-META.csv') as ideb_f1_goal:
    readCSV = csv.reader(ideb_f1_goal, delimiter=',')

    for row in readCSV:
        # [0] - Entity
        # [1 - len] - Score

        entity = row[0]

        ideb_score_array = numpy.array(row[1:len(row)]).astype(numpy.float)

        c = next(colors)
        plot.line([2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021], ideb_score_array, legend=entity + " - META",
                  line_width=2, line_color=c)


# Result
with open('../data_set/ideb_f1-RESULTADO.csv') as ideb_f1_resultado:
    readCSV = csv.reader(ideb_f1_resultado, delimiter=',')

    for row in readCSV:
        # [0] - Entity
        # [1 - len] - Score

        entity = row[0]

        ideb_score_array = numpy.array(row[1:len(row)]).astype(numpy.float)

        years = [2005, 2007, 2009, 2011, 2013, 2015, 2017]

        c = next(colors)
        plot.line(years, ideb_score_array, legend=entity + " - RESULTADO", line_width=1, line_color=c)
        plot.circle(years, ideb_score_array, legend=entity + " - RESULTADO", fill_color=c, line_color=c, size=6)

# show the results
show(plot)

if __name__ == "__main__":
    print("")
