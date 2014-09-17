
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import malt
import unittest


class TriangulationTest(unittest.TestCase):

    def test_simulation(self):
        sim = malt.Simulation(
            x_dim=100,
            y_dim=100,
            randomly_generate=True,
            num_nodes=5,
            time_noise=2,
            intensity_noise=0.1,
            confidence_noise=0.1
        )

        r_ref = 1
        l_ref = 50

        local_instance = sim.provide_stimulus(20, 50, r_ref, l_ref)

        res = local_instance.get_locations()
        print "Locations:", res
        print "Error:", local_instance.get_error(), "m"

        local_instance.plot()

if __name__ == "__main__":

    unittest.main()
