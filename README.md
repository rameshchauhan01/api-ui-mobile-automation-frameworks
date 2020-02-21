# SeleniumAutomation
UI Automation
How to find the frame/iframe:
Below are the ways to find the iframe/frame:

Using ID
Using Name
Using Element (widely used)
Using Index
Example:
<iframe id="ifr" name="demo" src="demo.html" height="200" width="300"></iframe>

# switchong to a rame which has id as 'ifr'
driver.switch_to_frame("ifr")

<iframe id="ifr" name="demo" src="demo.html" height="200" width="300"></iframe>
<iframe id="ifr" name="demo" class='second' src="width.html" height="200" width="300"></iframe>
<iframe id="ifr" name="demo" src="width.html" height="200" width="300"></iframe>

# switch to 1st frame
driver.switch_to_frame(1)
switcht name o the frame based on the name 
def frame_switch(name):
  driver.switch_to.frame(driver.find_element_by_name(name))
 To switch back to the main window, you can use   
  driver.switch_to.default_content()
