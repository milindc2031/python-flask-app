 def test_home_page(self):
     response = self.client.get('/home')
     assert response.status_code == 200
     html = response.get_data(as_text=True)
