
from PTFTestRail import *
from PTFJira import *

def test_demo1():
    x = 4
    if x == 4:
        assert x == 4  # is a successful assertion

def test_demo2(x=2,y=3,):
    sum=x+y
    if sum == 5:
        assert x == 2  # is a successful assertion

def test_demo3():
    y = 'abc'
    if y == 'abc':
        assert y == 'abc'  # is a successful assertion

case_id=1
result_flag=True
comments='Actual and expected result is not match'
project_name = CF.get('Default_TestRail', 'PROJECT_NAME')
test_run_name=CF.get('Default_TestRail', 'TEST_RUN_NAME')
project_id=get_project_id(project_name)
run_id=get_run_id(test_run_name,project_id)


update_test_result(run_id, case_id,result_flag,comments)
issue_dict = {
            'project': {'id': 10001},
            'summary': 'Unable to authenticate the account1',
            'description': 'Look into this one1',
            'issuetype': {'name': 'Bug'},
            }
create_bug(issue_dict, result_flag)