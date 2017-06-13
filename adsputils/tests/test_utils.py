#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

import unittest
import json
import inspect
from mock import patch

import adsputils

class TestAdsOrcidCelery(unittest.TestCase):
    """
    Tests the appliction's methods
    """
    def setUp(self):
        unittest.TestCase.setUp(self)
    
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_load_config(self):
        with patch('adsputils.load_module') as load_module:
            c = adsputils.load_config()
            self.assertEquals(('/dvt/workspace2/ADSPipelineUtils/adsputils/config.py',), 
                              load_module.call_args_list[0][0])
            self.assertEquals(('/dvt/workspace2/ADSPipelineUtils/adsputils/local_config.py',), 
                              load_module.call_args_list[1][0])
            f = os.path.dirname(inspect.getsourcefile(adsputils))
            self.assertEqual(c['PROJ_HOME'], f)
            
        with patch('adsputils.load_module') as load_module:
            adsputils.load_config('/tmp')
            self.assertEquals(('/tmp/config.py',), 
                              load_module.call_args_list[0][0])
            self.assertEquals(('/tmp/local_config.py',), 
                              load_module.call_args_list[1][0])

    
    def test_load_module(self):
        f = os.path.abspath(os.path.join(os.path.dirname(inspect.getsourcefile(adsputils)), './tests/config_sample.py'))
        x = adsputils.load_module(f)
        self.assertEquals(x, {'FOO': {'bar': ['baz', 1]}})

    
    def test_setup_logging(self):
        with patch('adsputils.ConcurrentRotatingFileHandler') as cloghandler:
            adsputils.setup_logging('app')
            f = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
            self.assertEqual("call(backupCount=5, encoding='UTF-8', filename='{filename}/logs/app.log', maxBytes=2097152, mode='a')".format(filename=f),
                             str(cloghandler.call_args))
            
    
    def test_get_date(self):
        """Check we always work with UTC dates"""
        
        d = adsputils.get_date()
        self.assertTrue(d.tzname() == 'UTC')
        
        d1 = adsputils.get_date('2009-09-04T01:56:35.450686Z')
        self.assertTrue(d1.tzname() == 'UTC')
        self.assertEqual(d1.isoformat(), '2009-09-04T01:56:35.450686+00:00')
        
        d2 = adsputils.get_date('2009-09-03T20:56:35.450686-05:00')
        self.assertTrue(d2.tzname() == 'UTC')
        self.assertEqual(d2.isoformat(), '2009-09-04T01:56:35.450686+00:00')
        
        d3 = adsputils.get_date('2009-09-03T20:56:35.450686')
        self.assertTrue(d3.tzname() == 'UTC')
        self.assertEqual(d3.isoformat(), '2009-09-03T20:56:35.450686+00:00')



if __name__ == '__main__':
    unittest.main()
