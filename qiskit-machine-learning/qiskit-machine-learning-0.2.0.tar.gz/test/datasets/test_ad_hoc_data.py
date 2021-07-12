# This code is part of Qiskit.
#
# (C) Copyright IBM 2020, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" Test Ad Hoc Data """

import unittest
from test import QiskitMachineLearningTestCase
import numpy as np
from qiskit_machine_learning.datasets import ad_hoc_data


class TestAdHocData(QiskitMachineLearningTestCase):
    """Ad Hoc Data tests."""

    def test_ad_hoc_data(self):
        """Ad Hoc Data test."""

        training_features, training_labels, _, test_labels = ad_hoc_data(
            training_size=20, test_size=10, n=2, gap=0.3, plot_data=False, one_hot=False
        )
        np.testing.assert_array_equal(training_features.shape, (40, 2))
        np.testing.assert_array_equal(training_labels.shape, (40,))
        np.testing.assert_array_almost_equal(
            test_labels, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        )

        _, _, _, test_labels = ad_hoc_data(
            training_size=20, test_size=10, n=2, gap=0.3, plot_data=False, one_hot=True
        )

        np.testing.assert_array_equal(test_labels.shape, (20, 2))
        np.testing.assert_array_equal(
            test_labels,
            [
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1],
            ],
        )


if __name__ == "__main__":
    unittest.main()
