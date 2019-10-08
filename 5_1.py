from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
  print ("Connection open failed to qemu:///system")
  exit(1)

# Host info 1: Available memory in KiloBytes
print ("\n############### Host info 1: Available memory in KB ################\n")
mem = conn.getFreeMemory()
mem = mem/1024
print ("Free Memory on the Host is " + str(mem) + " KB.")

# Host info 2: system info in XML format
print ("\n############## Host info 2: host system info in XML format #################\n")
sysinfo = conn.getSysinfo()
print (sysinfo)

# Host info 3: CPU map of Host CPUs
print ("\n############## Host info 3: CPU map of host CPUs ##############\n")
map = conn.getCPUMap()
print ("CPUs - " + str(map[0]))
print ("Availability - " + str(map[1]))

# Host info 4: Print CPU stats of all the host CPUs
print ("\n############## Host info 4: CPU stats #################\n")
stats = conn.getCPUStats(0)
print ("kernel info - " + str(stats['kernel']))
print ("idle info - " + str(stats['idle']))
print ("user info - " + str(stats['user']))
print ("iowait info - " + str(stats['iowait']))

# Host info 5: Host security model
print ("\n############# Host info 5: Host security model ###############\n")
model = conn.getSecurityModel()
print (model[0] + "" + model[1])

conn.close()

exit(0)
