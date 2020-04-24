import testrail
import config_reader_ip as CF

#get the test rail client object
def get_testrail_client():

    # Get the TestRail Url
    testrail_url = CF.get('Default_TestRail', 'TESTRAIL_URL')
    client = testrail.APIClient(testrail_url)
    # Get and set the TestRail User and Password
    client.user = CF.get('Default_TestRail', 'TESTRAIL_USER')
    client.password = CF.get('Default_TestRail', 'TESTRAIL_PASSWORD')
    return client

#Adds a new test result,status, comment or assigns a test (for a test run and case combination).
def update_test_result(run_id, case_id,result_flag,comments):
    # Create the client objects
    client = get_testrail_client()
    #"Update TestRail for a given run_id and case_id"
    update_flag = False
    # Update the result in TestRail using send_post function.
    # Parameters for add_result_for_case is the combination of runid and case id.
    # status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
    status_id = 1 if result_flag is True else 5
    if run_id is not None:
        try:
            result = client.send_post(
                'add_result_for_case/{}/{}'.format(run_id, case_id),
                {'status_id': int(status_id), 'comment': str(comments)}
            )
            print(result)
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            print('Updated test result for case: %s in test run: %s with msg:%s' % (case_id, run_id, comments))

    return update_flag
def add_results(run_id, result_flag,comments):
    # Create the client objects
    client = get_testrail_client()
    #"Update TestRail for a given run_id"
    update_flag = False
    # Update the result in TestRail using send_post function.
    # Parameters for add_result_for_case is the runid.
    # status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
    status_id = 1 if result_flag is True else 5
    if run_id is not None:
        try:
            result = client.send_post(
                'add_results/{}'.format(run_id),
                {'status_id': int(status_id), 'comment': str(comments)}
            )
            print(result)
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            print('Updated test results for test run: %s  with msg:%s' % (run_id, comments))

    return update_flag
#Attaching the file in created test results
def update_testresult_attachement(result_id,attachements_ptha):
    # Create the client objects
    client = get_testrail_client()
    update_flag = False
    # Update the result in TestRail using send_post function.
    # Parameters for add_result_for_case is the runid.
    # status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
    if result_id is not None:
        try:
            client.send_post('add_attachment_to_result/{}'.format(result_id), attachements_ptha)
        except (FileNotFoundError, IOError):
            print("Wrong file or file path")
        else:
            print('Attachements added for: %s in existing test run' %(result_id))
    return update_flag


#Fetch the test case details from test rail and retuns in a key value paire
def get_test_data(case_id):
    # Create the client objects
    client = get_testrail_client()
    tc_case_info = client.send_get('get_case/{}'.format(case_id))
    return tc_case_info
#"Get the project ID using project name"
def get_project_id(project_name):
    # Create the client objects
    client = get_testrail_client()
    project_id=None
    projects = client.send_get('get_projects')
    project_name_list = [name['name'] for name in projects]
    project_id_list = [id['id'] for id in projects]
    for i in range(len(project_name_list)):
        if project_name_list[i] == project_name:
            project_id = project_id_list[i]
            break
    return project_id

def get_run_id(test_run_name,project_id):
        "Get the run ID using test name and project name"
        run_id=None
        # Create the client objects
        client = get_testrail_client()
        try:
            test_runs = client.send_get('get_runs/%s'%(project_id))
        except OSError as err:
            print("OS error: {0}".format(err))

        else:
            for test_run in test_runs:
                 if test_run['name'] == test_run_name:
                     run_id = test_run['id']
                     break
            return run_id

