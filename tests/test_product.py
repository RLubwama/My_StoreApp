import unittest
import pytest
import tests

class Test(unittest.TestCase):
    products = {}
    def product(self,product_id,name):
        self.product_id = product_id
        self.name = name
        if name != products:
            print ("product is out of stock")
            # if condition:
            #     pass
            else:
                if name = products:
                    print("product in stock")
                    return product


