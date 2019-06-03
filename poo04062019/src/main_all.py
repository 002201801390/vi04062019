import csv
import itertools
import numpy

from enum import Enum
from bokeh.palettes import Category20 as Palette
from bokeh.plotting import figure, output_file, show


class GeometricForm(Enum):
    NONE = 0
    CIRCLE = 1
    TRIANGLE = 2
    SQUARE = 4
    ASTERISK = 5
    CIRCLE_CROSS = 6
    CIRCLE_X = 7
    CROSS = 8
    DIAMOND = 9
    DIAMOND_CROSS = 10
    INVERTED_TRIANGLE = 11
    SQUARE_CROSS = 12
    SQUARE_X = 13
    X = 14


def ini():
    goal_years = [2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021]
    result_years = [2005, 2007, 2009, 2011, 2013, 2015, 2017]

    # Fundamental 1
    # Goal
    process_ideb_data('../data_set/ideb_f1-META.csv', 'META', 2, goal_years, GeometricForm.ASTERISK)

    # Result
    process_ideb_data('../data_set/ideb_f1-RESULTADO.csv', 'RESULTADO', 1, result_years, GeometricForm.CIRCLE)

    # Fundamental 2
    # Goal
    process_ideb_data('../data_set/ideb_f2-META.csv', 'META', 2, goal_years, GeometricForm.SQUARE)

    # Result
    process_ideb_data('../data_set/ideb_f2-RESULTADO.csv', 'RESULTADO', 1, result_years, GeometricForm.TRIANGLE)

    # Fundamental 2
    # Goal
    process_ideb_data('../data_set/ideb_em-META.csv', 'META', 2, goal_years, GeometricForm.DIAMOND)

    # Result
    process_ideb_data('../data_set/ideb_em-RESULTADO.csv', 'RESULTADO', 1, result_years, GeometricForm.X)


def process_ideb_data(file_name, sulfix, l_width, years, geometric_form):
    sulfix = str(sulfix)

    with open(file_name) as file:
        read_csv = csv.reader(file, delimiter=',')

        for row in read_csv:
            # [0] - Entity
            # [1 - len] - Score

            entity = row[0]

            score_array = numpy.array(row[1:len(row)]).astype(numpy.float)

            color = next(colors)

            plot.line(years, score_array, legend=entity + " - " + sulfix,
                      line_width=l_width, line_color=color)

            if geometric_form == GeometricForm.CIRCLE:
                plot.circle(years, score_array, legend=entity + " - " + sulfix,
                            fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.TRIANGLE:
                plot.triangle(years, score_array, legend=entity + " - " + sulfix,
                              fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.SQUARE:
                plot.square(years, score_array, legend=entity + " - " + sulfix,
                            fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.ASTERISK:
                plot.asterisk(years, score_array, legend=entity + " - " + sulfix,
                              fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.CIRCLE_CROSS:
                plot.circle_cross(years, score_array, legend=entity + " - " + sulfix,
                                  fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.CIRCLE_X:
                plot.circle_x(years, score_array, legend=entity + " - " + sulfix,
                              fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.CROSS:
                plot.cross(years, score_array, legend=entity + " - " + sulfix,
                           fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.DIAMOND:
                plot.diamond(years, score_array, legend=entity + " - " + sulfix,
                             fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.DIAMOND_CROSS:
                plot.diamond_cross(years, score_array, legend=entity + " - " + sulfix,
                                   fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.INVERTED_TRIANGLE:
                plot.inverted_triangle(years, score_array, legend=entity + " - " + sulfix,
                                       fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.SQUARE_CROSS:
                plot.square_cross(years, score_array, legend=entity + " - " + sulfix,
                                  fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.SQUARE_X:
                plot.square_x(years, score_array, legend=entity + " - " + sulfix,
                              fill_color=color, line_color=color, size=6)

            elif geometric_form == GeometricForm.X:
                plot.x(years, score_array, legend=entity + " - " + sulfix,
                       fill_color=color, line_color=color, size=6)


# colors
colors = itertools.cycle(Palette[20])

# output to static HTML file
output_file("../result_set/ideb_all.html")

# range of years
min_year = 2005
max_year = 2021

ano = range(min_year, max_year, 2)

# create a new plot
plot = figure(
    tools='pan, box_zoom, reset, save',
    title='Análise IDEB - Fundamental 1, Fundamental 2 e Ensino Médio',
    plot_width=1280, plot_height=680,
    x_range=[min_year - 1, max_year + 6],
    y_axis_type="log",
    x_axis_label='Ano',
    y_axis_label='Nota do IDEB'
)

# @author = Eduwardo Keizo Horibe Junior
# all data provided by http://ideb.inep.gov.br/
if __name__ == "__main__":
    ini()

    # show the results
    show(plot)
