'''
Use %load_ext line_profiler to load the line_profiler within your IPython session.
press
1

    Use %lprun -f convert_units convert_units(heroes, hts, wts) to get line-by-line runtimes.

def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data
'''

