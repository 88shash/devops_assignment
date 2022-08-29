import random
import subprocess

def createuser(vmname):
    cmd = "/root/adduser.sh"
    rootuser = "root"
    subprocess.Popen(f"ssh {rootuser}@{vmname} {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    vmuser = subprocess.Popen(f"ssh {rootuser}@{vmname} whoami", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return vmuser
    

def allocatevm():
    ava_vm = ['vm1','vm2','vm3','vm4','vm5']
    used_vm = []
    if( request.method == 'GET'):
        if len(ava_vm) != 0:
            ## User Requested a VM and random VM is allocated from the list
            allocated_vm = random.choice(ava_vm)
            # Once the VM is allocated, it wil be removed from available vm list
            ava_vm.remove(allocated_vm)
            # Once allocated, the vm will move to the used vm list
            used_vm.append(allocated_vm)
            # Create User on allocated VM
            vm_user = createuser(allocated_vm)
        else:
            ## Inform User if no VM is available in the list 
            print("Sorry no VM available, try after sometime")
    return allocated_vm, ava_vm, used_vm, vm_user
    
    
def submitvm(vmname):
    allocated_vm, ava_vm, used_vm, vm_user = allocatevm()
    ava_vm.append(vmname)
    used_vm.remove(vmname)
    systemcleanup(allocated_vm, vm_user)
    return ava_vm, used_vm
    

def systemcleanup(vmname, vmuser):
    cmd = "/root/cleanup.sh"
    rootuser = "root"
    subprocess.Popen(f"ssh {rootuser}@{vmname} {cmd} {vmuser}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    

if __name__ == 'main':
    print("Get VM from the inventory")
    allocated_vm, ava_vm, used_vm, vm_user = allocatevm()
    print(f"Allocated VM -- {allocated_vm}")
    
    ## User will submit the VM once done
    vmname = input("Submit the VM: ")
    submitvm(vmname)
    print(f"Available VMs are - {ava_vm}")
