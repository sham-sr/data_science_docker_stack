import altair as alt
from vega_datasets import data
import panel as pn

pn.extension('vega')

altair_logo = 'https://altair-viz.github.io/_static/altair-logo-light.png'
states = alt.topo_feature(data.us_10m.url, 'states')
states['url'] = 'https://raw.githubusercontent.com/vega/vega/master/docs/data/us-10m.json'
source = 'https://raw.githubusercontent.com/vega/vega/master/docs/data/population_engineers_hurricanes.csv'
variable_list = ['population', 'engineers', 'hurricanes']

variable = pn.widgets.Select(options=variable_list, name='Variable')

@pn.depends(variable.param.value)
def get_map(variable):
    return alt.Chart(states).mark_geoshape().encode(
        alt.Color(variable, type='quantitative')
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(source, 'id', [variable])
    ).properties(
        width=500,
        height=300
    ).project(
        type='albersUsa'
    ).repeat(
        row=[variable]
    )

pn.Row(
    pn.Column('# Altair Choropleth Maps', pn.panel(altair_logo, height=150), variable),
    get_map
).servable()