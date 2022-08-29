from flask import Flask, jsonify, request
import random


# Creating a Flask app

app = Flask(_name_)

@app.route('/', methods = ['GET', 'POST'])
def allocatevm():
    ava_vm = ['vm1','vm2','vm3','vm4','vm5']
    used_vm = []
    if( request.method == 'GET'):
        if len(ava_vm) != 0:
            ## User Requested a VM and random VM is allocated from the list
            user_vm = random.choice(ava_vm)
            # Once the VM is allocated, it wil be removed from available vm list
            ava_vm.remove(user_vm)
            # Once allocated, the vm will move to the used vm list
            used_vm.append(user_vm)
            # Create User on allocated VM
            vm_user = createuser(allocated_vm)
        else:
            ## Inform User if no VM is available in the list 
            print("Sorry no VM available, try after sometime")
    return user_vm
    

@app.route('/'<string:vm_name>'. methods = ['POST'])
def submitvm(vm_name):
    return(vm_name)
    
    
if __name__ == 'main':
    app.run(debug = True)