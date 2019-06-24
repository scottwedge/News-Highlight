import unittest
from models import source 
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behavior of the Source class
    '''

    def setUp(self):
      '''
      Set up method that will run before every Test
      '''
      self.new_source = Source('Ebola out-break scare','https://edition.cnn.com/2019/06/22/health/ebola-outbreak-congo-intl/index.html')from flask import render_template
from app import app

@app.errorhandler(404)
def four_Ow_four(error):
  '''
  Function to render the 404 error page
  '''
  return render_template('fourOwfour.html'),404

    def test_isSourceinstance(self):
      '''
      Function to test if the object created in the setup is indeed a Source Object
      '''
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unnittest.main()          