import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file via the following link:
    https://www.dropbox.com/s/xcn0u2uxm8c4n6l/baseball_data.csv
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """
    df = pandas.read_csv(filename)
    left_handed = df[df['handedness'] == 'L']['avg']
    right_handed = df[df['handedness'] == 'R']['avg']
    (test_statistic, p_value) =  scipy.stats.ttest_ind(left_handed, right_handed, equal_var=False)
    if (p_value < 0.05):
        return (False, (test_statistic, p_value))
    return (True, (test_statistic, p_value))


if __name__ == '__main__':
    filename = "baseball_data.csv"
    result = compare_averages(filename)
    print result