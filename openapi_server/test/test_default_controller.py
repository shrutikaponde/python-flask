# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.employee import Employee  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_employees_get(self):
        """Test case for employees_get

        
        """
        query_string = [('bodyLimit', 15),
                        ('pageLimit', 2)]
        headers = { 
            'Accept': 'aplication/json',
        }
        response = self.client.open(
            '/employees',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employees_id_get(self):
        """Test case for employees_id_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/employees/{id}'.format(id=54),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employees_post(self):
        """Test case for employees_post

        
        """
        employee = {
  "employee name" : "Ryan Pinkham",
  "id" : 4,
  "employee title" : "Market Manager"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/employees',
            method='POST',
            headers=headers,
            data=json.dumps(employee),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
