
from unittest import TestCase
from app.routes import app

class ProductTestCase (TestCase):
    # "initialize up a client to for testing"
    def setUp(self):
        self.client = app.test_client(self)
    def test_delete_product(self):
            with self.client:
                response = self.client.delete('/api/v1/products/1')
                self.assertEquals(response.status_code, 200)
    
        
        
                
