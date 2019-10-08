from __future__ import print_function
import sys
import libvirt

# Guest Host Name provided as an argument
domName = sys.argv[1]

conn = libvirt.open('qemu:///system')
if conn == None:
  print ("Connection open failed to qemu:///system")
  exit(1)

# Open connection to Guest Host
dom = conn.lookupByName(domName)
if dom == None:
  print ("Connection open failed to " + donName)
  exit(1)

# Guest Host info 1: Domain ID
print ("\n############### Guest Host info 1: Domain ID ################\n")
id = dom.ID()
if id == -1:
  print ("Domian currently not running")
else:
  print ("Guest host ID is " + str(id))

# Guest Host info 2: Domain UUID
print ("\n############## Guest Host info 2: UUID #################\n")
uuid = dom.UUIDString()
print ("UUID of the guest domain is " + uuid)

# Guest Host info 3: Determine if domain is persistent
print ("\n############## Guest Host info 3: Is domain persistent ##############\n")
flag = dom.isPersistent()
if flag == 1:
  print ("Guest domian is persistent")
elif flag == 0:
  print ("Guest domain is not persistent")
else:
  print ("Error")

# Guest Host info 4: Guest Host hostname
print ("\n############## Guest Host info 4: Domain name #################\n")
name = dom.name()
print ("Domain name is " + name)

# Guest Host info 5: Hardware info of the guest domain
print ("\n############# Guest Host info 5: Hardware Info ###############\n")
state, maxmem, mem, cpus, cput = dom.info()
print ("State - " + str(state))
print ("Max memory - " + str(maxmem))
print ("Memory available - " + str(mem))
print ("Number of CPUs - " + str(cpus))
print ("CPU time - " + str(cput))

conn.close()

exit(0)
