import unittest
from folioforge.urls import delivery_url


class URLTests(unittest.TestCase):
    def test_path_encoding(self):
        self.assertEqual(delivery_url("demo", "logos/a b#c.svg"),
                         "https://res.cloudinary.com/demo/image/upload/logos/a%20b%23c.svg")

    def test_gray_requires_raster(self):
        self.assertIn("/e_colorize:100,co_rgb:808080/f_png/", delivery_url("demo", "a.svg", gray=True))

    def test_invalid_paths(self):
        for path in ("", "/a.svg", "../a.svg", "a//b.svg"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                delivery_url("demo", path)

    def test_cloud_cannot_inject_url(self):
        with self.assertRaises(ValueError):
            delivery_url("demo/other", "a.svg")
