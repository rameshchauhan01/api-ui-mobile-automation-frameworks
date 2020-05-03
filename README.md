# TestRail Run Result Inegration with python 
Why :  
In most automated checks, we are able to judge the outcome as ‘pass’ or ‘fail’ by comparing the expected result to the actual result. Tracking, reporting and sharing the test results is important.
--------------------------------------
Steps
------------------------------------
1. Get the TestRail API : Download link http://docs.gurock.com/testrail-api2/bindings-python
2. Connect (authentication) to your TestRail instance : used bearer authentication
3. Write the logic to update test results to TestRail
4. Identify your test case id/test run id on TestRail
5. Modify your test script to report to TestRail

# JIRA Inegration with python 
Why :  
In most automated checks, we are able to judge the outcome as ‘pass’ or ‘fail’ by comparing the expected result to the actual result. raising the the defect is tedious task .
--------------------------------------
Steps
------------------------------------
1. Install the jira python package  : pip install jira Download link http://docs.gurock.com/testrail-api2/bindings-python
2. More details about the authenication and supprted rest api calls details available on https://community.atlassian.com/t5/Jira-questions/How-do-I-access-the-hosted-Jira-API-via-python/qaq-p/505632
3. Get the API tokens help :https://confluence.atlassian.com/cloud/api-tokens-938839638.html?_ga=2.19286129.830613724.1588491140-232173540.1587632071
4. Added the defect based on the flag and return the flag
5. Get the existing issue details and update with comments
-------------------
Repository details
-------------------
a) Directory structure of our current Templates

   ./
	|__config_reader_ip: Read all configurations and credential 
	|__config.ini: input data for credential and configurations
	|__PTFTestRail: Contains functions to intract with test rail  api end points	
	|__testrail: Provided by test rail
	|__test_sample_demo: Deno tests with pytest

	
