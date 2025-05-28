from bokeh.plotting import figure, output_file, save, show, ColumnDataSource
from bokeh.models import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas 

# Read in CSV
df = pandas.read_csv('cars.csv')

#car = df['Car'].tolist()
#hp = df['Horsepower']

source = ColumnDataSource(df)


output_file('index.html')

car_list = source.data['Car'].tolist()
p = figure(
    y_range=car_list, 
    height=600,
    width=800,
    title='Cars with Top Horsepower',
    x_axis_label='Horsepower',
    tools="pan, box_select, zoom_in, zoom_out, save, reset"
)

p.hbar(
    y="Car", 
    right="Horsepower",
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'Car', 
        palette=Blues8, 
        factors=car_list
    ),
    fill_alpha=0.9,
    source=source,
    legend_field='Car'
)

p.legend.orientation = "vertical"
p.legend.location = "top_right"
p.legend.label_text_font_size = "10pt"

hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@Car</h3>
    <div><strong>Price: </strong>@Price</div>
    <div><strong>HP: </strong>@Horsepower</div>
    <div><img src="@Image" alt="" width="200" /></div>
  </div>
"""
p.add_tools(hover)

#show(p)
# This code creates a simple line plot using Bokeh and saves it to an HTML file.

save(p)

script, div = components(p)
print(div)
print(script)