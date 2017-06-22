# -*- coding: utf-8 -*-

from adsputils import ADSCelery
import unittest


class TestUpdateRecords(unittest.TestCase):

    def test_config(self):
        app = ADSCelery('test',local_config={
            'FOO': ['bar', {}]
            })
        self.assertEqual(app._config['FOO'], ['bar', {}])
        self.assertEqual(app.conf['FOO'], ['bar', {}])
        
        self.assertEqual(app.conf['CELERY_RESULT_SERIALIZER'], 'adsmsg')
        self.assertFalse(app._config.get('CELERY_RESULT_SERIALIZER', None))
        

if __name__ == '__main__':
    unittest.main()
