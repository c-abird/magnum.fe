import unittest
from dolfin import *
from magnumfe import *
import numpy


class MesherTest(unittest.TestCase):
    def test_create_shell(self):
      mesher = Mesher()
      # create and mesh sample
      mesher.create_cuboid((3.0, 2.0, 1.0), (15, 10, 5))

      # create and mesh shell
      mesher.create_shell(1);
      mesh_with_shell = mesher.mesh()
      self.assertEqual(mesh_with_shell.num_cells(), 5640)
      self.assertEqual(mesh_with_shell.num_vertices(), 1188)

    def test_get_sample_size(self):
      mesher = Mesher()
      mesher.create_cuboid((3.0, 2.0, 1.0), (15, 10, 5))
      size = mesher.get_sample_size()

      self.assertEqual(size[0], 3.0)
      self.assertEqual(size[1], 2.0)

    def test_get_scaled_sample_size(self):
      mesher = Mesher()
      mesher.create_cuboid((3.0, 2.0, 1.0), (15, 10, 5))
      size = mesher.get_sample_size(scale = 10)

      self.assertEqual(size[0], 30.0)
      self.assertEqual(size[1], 20.0)


    def test_scale(self):
      mesher = Mesher()
      mesher.create_cuboid((3.0, 2.0, 1.0), (15, 10, 5))

      mesh1 = mesher.mesh()
      mesh2 = mesher.mesh(10.0)

      self.assertAlmostEqual(mesh1.hmax()*10.0, mesh2.hmax())
      self.assertAlmostEqual(mesh1.hmin()*10.0, mesh2.hmin())

if __name__ == '__main__':
    unittest.main()
