import numpy as np
import pandas as pd

FILE_PATH = 'day1.csv'

def get_inputs():
    df = pd.read_csv('day1.csv', header=None, names=['a', 'b'], dtype='Int64')
    return (df['a'].sort_values(), df['b'].sort_values())

def part1():
    a, b = get_inputs()
    if len(a) == len(b):
        distance = sum(abs(a-b))
    else:
        raise IndexError("Lists are of different lengths")
    return distance

def part2():
    a, b = get_inputs()
    b_freq = b.value_counts().reset_index()
    sim_df = pd.merge(a, b_freq, how='left', left_on='a', right_on='b')
    sim_df.fillna(0, inplace=True)
    sim_score = sum(sim_df['a']*sim_df['count'])
    return sim_score
    

if __name__ == "__main__":
    ans1 = part1()
    print(f"Answer 1: {ans1}")
    ans2 = part2()
    print(f"Answer 2: {ans2}")
