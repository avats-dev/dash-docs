import dash_core_components as dcc
import dash_html_components as html

from dash_docs import tools
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)


layout = html.Div([
    html.H1('Advanced Callbacks'),

    rc.Markdown('''
    ## Catching errors with `PreventUpdate`

    In certain situations, you don't want to update the callback output. You can
    achieve this by raising a `PreventUpdate` exception in the callback function.
    '''),
    rc.Syntax(examples['prevent_update_button.py'][0]),
    rc.Example(examples['prevent_update_button.py'][1]),

    rc.Markdown('''
    ## Displaying errors with `dash.no_update`

    This example illustrates how you can show an error while keeping the previous
    input, using `dash.no_update` to update the output partially.
    '''),
    rc.Syntax(examples['prevent_update.py'][0]),
    rc.Example(examples['prevent_update.py'][1]),

    rc.Markdown('''
    ## Determining which `Input` has fired with `dash.callback_context`

    In addition to event properties like `n_clicks`
    that change whenever an event happens (in this case a click), there is a
    global variable `dash.callback_context`, available only inside a callback.
    It has properties:
    - `triggered`: list of changed properties. This will be empty on initial
      load, unless an `Input` prop got its value from another initial callback.
      After a user action it is a length-1 list, unless two properties of a
      single component update simultaneously, such as a value and a timestamp
      or event counter.
    - `inputs` and `states`: allow you to access the callback params
      by id and prop instead of through the function args. These have the form
      of dictionaries `{ 'component_id.prop_name': value }`

    Here's an example of how this can be done:'''),

    rc.Syntax(examples['last_clicked_button.py'][0]),
    rc.Example(examples['last_clicked_button.py'][1]),
    rc.Markdown('''
    ### Legacy behaviour: using timestamps

    Prior to v0.38.0, you needed to compare timestamp properties like
    `n_clicks_timestamp` to find the most recent click. While existing uses of
    `*_timestamp` continue to work for now, this approach is deprecated, and
    may be removed in a future update. The one exception is
    `modified_timestamp` from `dcc.Store`, which is safe to use, it is NOT
    deprecated.

    ------------------------
    '''),

    rc.Markdown('''
    ## Improving performance with memoization

    Memoization allows you to bypass long computations by storing the
    results of function calls.

    To better understand how memoization works, let's start with a simple example.

'''),

    rc.Syntax('''
import time
import functools32

@functools32.lru_cache(maxsize=32)
def slow_function(input):
    time.sleep(10)
    return 'Input was {}'.format(input)
    '''),

    rc.Markdown('''
    Calling `slow_function('test')` the first time will take 10 seconds.
    Calling it a second time with the same argument will take almost no time
    since the previously computed result was saved in memory and reused.

    The [Performance](/performance) section of the Dash docs delves a
    little deeper into leveraging multiple processes and threads in
    conjunction with memoization to further improve performance.
    ''')
])
