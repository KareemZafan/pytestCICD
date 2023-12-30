import pytest
from src import myfile

p =  Person('kareem',30,'Cairo',"Egyptian")

class PersonTests:
     def test_get_name(self):
        assert p.get_name() == 'kareem'
        

     def test_get_address(self):
        assert  p.get_name() == 'Cairo'
    
        
    
    
    