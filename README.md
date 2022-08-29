Prerequisite

1. I am assuming the VM are already created via Terraform and the state file is stored on s3 bucket
2. There will be python parsar, which parsed the terraform state file and return the VM inventory in the form of python List


Note : Assignment is not 100% completed, as this requires a python API development and OOPS principles. And I've mostly worked on the Pythong Scripting and not the Application Development. However still I've tried to complete the assignment, please find details below


Solution 1:
1. Using Python Flask

How to Run
1. Open the command prompt and execute command
python solution_with_flask.py

2. This will Start the web Server, now from postman or curl you can send get Request to the url
example : 
GET Request
url : http://127.0.0.1:5000


Solution 2:
How to Run
1. Open the command prompt and execute command
python solution_without_flask.py

After assinging the VM, the script will further ask to submit the VM, please provide the VM name to the script
