
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import malt.localization as tri
import malt
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import unittest
from pprint import pprint
import time


class TriangulationTest(unittest.TestCase):

    def setUp(self):
        self.show_plot = True
        self.d_events = [
            malt.DetectionEvent(-9, -1, 0.9, 90, time.time()),
            malt.DetectionEvent(-2, 1, 0.3, 97, time.time() - 7),
            malt.DetectionEvent(1, 3, 0.5, 86, time.time() - 10),
            malt.DetectionEvent(0, -1, 0.6, 100, time.time() - 5)
        ]
        #pprint(self.d_events)

    def test_position_probability(self):

        l_ref = 65
        r_ref = 1

        test_x = 0
        test_y = 0

        print "\n=== Position Probability === :: (", test_x,
        print ",", test_y, ")  --> ",
        print tri.position_probability(
            test_x, test_y,
            r_ref, l_ref,
            self.d_events
        ), "\n"

    def test_optimization_list(self):

        l_ref = 100
        r_ref = 1

        res = tri.determine_source_position_list(
            r_ref, l_ref,
            self.d_events,
            disp=0
        )

        print "\n=== Optimization List === ::\n[ Xs, Ys ]  <--> ",
        pprint(res)
        print "\n"

    def test_optimization(self):

        l_ref = 65
        r_ref = 1

        res = tri.determine_source_locations(
            r_ref, l_ref,
            self.d_events,
            disp=0
        )

        print "\n=== Optimization === :: [ Xs, Ys ]  <--> ", res, "\n"

    def test_together(self):

        r_ref = 1
        l_ref = 65

        res = tri.determine_source_locations(
            r_ref, l_ref,
            self.d_events,
            disp=0
        )

        if self.show_plot:
            fig = plt.figure("All together test")
            ax = Axes3D(fig)
            ax.set_title("Source location probability density function")
            ax.set_xlabel("X Location")
            ax.set_ylabel("Y Location")
            ax.set_zlabel("Probability")

            v_min = -10
            v_max = 10
            v_step = 0.05

            x = y = np.arange(v_min, v_max, v_step)
            X, Y = np.meshgrid(x, y)
            zs = np.array(
                [
                    tri.position_probability(
                        x_i, y_i, r_ref, l_ref, self.d_events
                    )
                    for x_i, y_i in zip(np.ravel(X), np.ravel(Y))
                ]
            )

            Z = zs.reshape(X.shape)

            ax.plot_surface(X, Y, Z, cmap=cm.jet)
            ax.scatter(
                [p.x for p in res],
                [p.y for p in res],
                [
                    tri.position_probability(
                        p.x, p.y,
                        r_ref, l_ref,
                        self.d_events
                    ) for p in res
                ],
                marker="D",
                linewidths=10
            )

            print "\n=== All Together ===\n"
            plt.show()


if __name__ == "__main__":

    print "\n=== Triangulation Testing ===\n"
    unittest.main()
