import json
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures


class TestTemplatesApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.templates()

    def test_templates_api(self):
        client = Client()
        t1 = client.get('/api/templates')
        self.assertEquals(200, t1.status_code)
        res = json.loads(t1.content.decode('utf-8'))
        self.assertEqual(3, len(res['templates']))
        for r in res['templates']:
            self.assertTrue('id' in r)
            self.assertTrue('title' in r)
            self.assertTrue('sku' in r)
            self.assertTrue('price' in r)
            self.assertTrue('description' in r)

    def test_template_404_api(self):
        client = Client()
        t1 = client.get('/api/template', {'id': 10})
        self.assertEquals(404, t1.status_code)
        res = json.loads(t1.content.decode('utf-8'))
        self.assertEquals({}, res)

    def test_fields_template_detail_api(self):
        client = Client()
        t1 = client.get('/api/template', {'id': 2})
        self.assertEquals(200, t1.status_code)
        res = json.loads(t1.content.decode('utf-8'))
        self.assertTrue('id' in res['template'])
        self.assertTrue('title' in res['template'])
        self.assertTrue('sku' in res['template'])
        self.assertTrue('price' in res['template'])
        self.assertTrue('description' in res['template']),
        self.assertTrue('discount' in res['template'])
        self.assertTrue('thumbnails' in res['template'])
        self.assertTrue('originals' in res['template'])
        self.assertTrue('price_pay' in res['template']),
        self.assertTrue('gallery' in res['template'])

    def test_value_fields_template_detail_api(self):
        client = Client()
        t1 = client.get('/api/template', {'id': 2})
        self.assertEquals(200, t1.status_code)
        res = json.loads((t1.content.decode('utf-8')))
        self.assertEqual(2, res['template']['id'])
        self.assertEqual('TemplateOne', res['template']['title'])
        self.assertEqual('32.50', res['template']['price'])
        self.assertEqual('teste template', res['template']['description'])
        self.assertEqual('10.50', res['template']['discount'])
        self.assertEqual(['image3.jpg', 'image1.jpg'], res['template']['thumbnails'])
        self.assertEqual(['image4.jpg', 'image2.jpg'], res['template']['originals'])
        self.assertEqual('22.00', res['template']['price_pay'])
        self.assertEqual({'thumbnail': 'image3.jpg', 'original': 'image4.jpg'}, res['template']['gallery'][0])
        self.assertEqual({'thumbnail': 'image1.jpg', 'original': 'image2.jpg'}, res['template']['gallery'][1])
