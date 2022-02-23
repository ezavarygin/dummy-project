import sys
import os
import numpy as np
from scipy.stats import normaltest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))

from dummy_src.distributions import clipped_normal_sample


class TestClippedNormalSample:

    def test_lower_clipping_works(self):

        lower = 8
        result = clipped_normal_sample(10, 5, 1000, lower=lower)

        assert lower <= np.min(result), 'Lower clipping failed!'

    def test_upper_clipping_works(self):

        upper = 18
        result = clipped_normal_sample(10, 5, 1000, upper=upper)

        assert np.min(result) <= upper, 'Upper clipping failed!'

    def test_both_clipping_work(self):

        lower = 8
        upper = 18
        result = clipped_normal_sample(10, 5, 1000, lower=lower, upper=upper)

        assert lower <= np.min(result) and np.max(result) <= upper, 'Simultaneous lower and upper clipping failed!'

    def test_normality(self):

        result = clipped_normal_sample(1, 5, 100000, lower=None, upper=None)

        k2, p = normaltest(result)

        assert p > 0.01, f'Normality test failed: p = {p}!'
