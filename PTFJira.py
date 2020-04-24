
from jira import JIRA
import config_reader_ip as CF

#Geting the JIRA client using basic uthentication (api_token)
def get_jira_client():
    # Get the JIRA Url
    my_api_token = CF.get('Default_Jira', 'MY_API_TOKEN')
    jira_user = CF.get('Default_Jira', 'JIRA_USER')
    password = CF.get('Default_Jira', 'JIRA_PWD')
    server = CF.get('Default_Jira', 'SERVER')
    options = {'server': server}
    jira = JIRA(options, basic_auth=(jira_user, my_api_token))
    return jira

#Create the bug in the JIRA using dictionary
def create_bug(issue_dict, result_flag):
    #Jira object to access the jira functions
    jira = get_jira_client()
    #Using flag fo success of the function
    update_flag = False
    if result_flag is False:
        try:
            jira.create_issue(fields=issue_dict)
        except jira as msg:
            print('Object value is %s' %(jira))
        else:
            print('Result flag value %s' %(result_flag))
    return update_flag


#Add an attachements in created or existing defect
def add_attachment(bug_key,filepath):
        #Initialising Jira object  from get_jira_client() function
        jira = get_jira_client()
        if bug_key is not None:
            try:
                jira.add_attachment(issue=bug_key, attachment=filepath)
            except OSError as err:
                print("OS error: {0}".format(err))
            else:
                print('Updated jira bug for bug_key: %s ' % (bug_key))





