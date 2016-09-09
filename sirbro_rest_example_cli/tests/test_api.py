
import os, sys, inspect

# use this if you want to include modules from a subfolder
def include_module_path(path):
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],path)))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
include_module_path("..")



from sirbro_app.app import app, appconfig, run_app
from nose.tools import assert_equal
from nose.tools import assert_not_equal



class TestApp(object):

    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
        pass

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""
        pass

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        #app['TESTING'] = True
        self.test_app = app.test_client()

    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        pass

    def test_get_slash(self):
        rv = self.test_app.get('/')
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 201)

    def test_get_api(self):
        rv = self.test_app.get('/api')
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 201)
        
    def test_get_api_v1(self):
        rv = self.test_app.get('/api/v1')
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 201)


    def test_get_api_v1_alive(self):
        rv = self.test_app.get('/api/v1/alive')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)

    def test_get_api_v1_info(self):
        rv = self.test_app.get('/api/v1/info')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)

    def test_get_api_v1_config(self):
        rv = self.test_app.get('/api/v1/config')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)


