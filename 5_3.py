from __future__ import print_function
import sys
import libvirt
import datetime
import logging

# declare local variables
aggr_cpu = {}
total_mem = 0
aggr_mem = {}
dom_list = []

# Create log file
logging.basicConfig(filename="5_3.log", level=logging.INFO)

# Check for input arguments
if ( len(sys.argv) == 1 or len(sys.argv) > 3 ):
  print ("Execute the program as: 'python 5_3.py <CPU/MEM> <value of T>'")
  exit(1)

conn = libvirt.open('qemu:///system')
if conn == None:
  print ("Connection open failed to qemu:///system")
  exit(1)

# Listing all active domians
print ("############# List of all active domains #############")
domIDs = conn.listDomainsID()
if domIDs == None:
  print ("Failed to list all active domains")

if len(domIDs) == 0:
  print ("No active domians")
else:
  for domId in domIDs:
    print ('Domain ID ' + str(domId))
    dom = conn.lookupByID(domId)
    if dom == None:
      print ("Failed to open connection to a domain")
      break

    # Sorting based on CPU usage
    if sys.argv[1] == 'CPU':
      cpu_stats = dom.getCPUStats(False)
      for (i, cpu) in enumerate(cpu_stats):
        print ('CPU ' + str(i) + ' Time ' + str((cpu['cpu_time']) / 1000000000))  # CPU stats are in nano seconds
      cpu_stats_aggr = dom.getCPUStats(True)
      aggr_cpu[str(domId)] = int(cpu_stats_aggr[0]['cpu_time'] / 1000000000)

      if (len(sys.argv) != 2):
        # Check if CPU usage exceeds the for user provided threshold for CPU usage
        if (aggr_cpu[str(domId)] > int(sys.argv[2])):
          print ("ALERT! CPU usage exceeds the threshold!")
          logging.info(' ' + str(datetime.datetime.now().time()) + ' ALERT! CPU usage exceeds the threshold of ' + sys.argv[2] + ' for ' + str(dom.name()) + ' ' + ' with CPU usage of ' + str(aggr_cpu[str(domId)]))
        #print (dom.hostname(), datetime.datetime.now().time(), aggr_cpu[str(domId)])

      print ('Average vCPU time (nano sec): ' + str(aggr_cpu[str(domId)]))
      print ("===================================")

      print ("\nListing VMs in ascending order of CPU usage\n")
      dom_list = sorted(aggr_cpu, key=aggr_cpu.get) # Lists the VMs in terms of domian ID
      print (sorted(aggr_cpu, key=aggr_cpu.get))
      print ('\n')

      # List VMs by name
      for item in dom_list:
        dom_i = conn.lookupByID(int(item))
        print (dom_i.name()+ '\n')

    # Sorting based on MEM usage
    elif sys.argv[1] == 'MEM':
      mem_stats = dom.memoryStats()
      num_mem_stats = len(mem_stats)

      print ("Mmeory used:")
      for stat in mem_stats:
        print (' ' + str(mem_stats[stat]))
        total_mem += int(mem_stats[stat])
      aggr_mem[str(domId)] = int(total_mem / num_mem_stats)

      print ("Average memory usage is: " + str(total_mem / num_mem_stats))
      print ("=================================")

      print ("\nListing VMs in ascending order of MEM usage\n")
      print (sorted(aggr_mem, key=aggr_mem.get)) # Lists the VMs in terms of domain ID
      print ('\n')
      dom_list = sorted(aggr_mem, key=aggr_mem.get)

      # List VMs by name
      for item in dom_list:
        dom_i = conn.lookupByID(int(item))
        print (dom_i.name() + '\n')

conn.close()

exit(0)
