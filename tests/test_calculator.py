import pytest
from datetime import datetime


@pytest.mark.feb
def test_add():
    assert 'a' + 'b' == 'ab'
    
    
def divide(a , b): 
    try:
        return a  / b 
    except:
        print(f"b should not be zero")
        return None 
    
def get_test_data():
    return [(2,2,1),(4,2,2),(55,0,None),(220,2,110),(30,6,5),(22,-11,-2),(0,33,0)]


@pytest.mark.parametrize('param1,param2,expeted_result',get_test_data())
@pytest.mark.regression
def test_division(param1, param2, expeted_result):
    assert divide(param1,param2) == expeted_result
   
    
@pytest.mark.skip(reason="function is not ready , we test it in the next release ")
@pytest.mark.regression
def test_to_lower():
    assert 'AHMED'.lower() == 'ahmed' 

print(datetime.now())
@pytest.mark.skipif((datetime.now() > datetime(2022, 12, 31, 15, 30, 0)),reason="it should be run on 2023-12-12")
@pytest.mark.prod
def test_to_upper():
    assert 'ahmed'.upper() == 'AHMED' 
    


@pytest.mark.parametrize("input,output",[('engineer','Engineer'),('doctor','Doctor'),('teacher','Teacher')])
def test_titles(input,output):
    assert input.title() == output
    
#open db connection
@pytest.fixture(autouse=True,name='myF')
def set_up_tear_down():
      print("Openning DB Connectionn") 
      print('Open url from browser')
      yield
      print("Connection of DB is closing ...")
      print("Close browser")
      print("Bye")
      
 #open db connection
@pytest.fixture()
def clear_cache():
      print("clear browser cache") 
      
      
 
      
        


#@pytest.mark.usefixtures('clear_cache','myF')
def test_student_name_from_db():
    print('Start execution of testing the name')
    name = 'ahmed'
    assert name == 'ahmed'
    
    


    
    
    

    
    