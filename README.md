##     Linux Networking HW-2 Question 5 
###    Team 9:  Ramya Vijayakumar (rvijaya4) , Prashanth Mallyampatti (pmallya)


Question 5 has 3 parts and each of these parts have been implemeted as separate python scripts.

## **1) 5_1.py :** 
      script to display 5 host features such as - 
			a. Available memory in KB
			b. Host system info in XML format
			c. Number of CPUs
			d. CPU stats such as kenel info, idle info, user info, iowait info
			e. Host security model
			
## **Execution:**		
      python 5_1.py

## **Sample Execution:**

```
root@t11_vm8:~/HW_2# python 5_1.py

############### Host info 1: Available memory in KB ################

Free Memory on the Host is 293784 KB.

############## Host info 2: host system info in XML format #################

<sysinfo type='smbios'>
  <bios>
    <entry name='vendor'>SeaBIOS</entry>
    <entry name='version'>1.10.2-1ubuntu1</entry>
    <entry name='date'>04/01/2014</entry>
    <entry name='release'>0.0</entry>
  </bios>
  <system>
    <entry name='manufacturer'>QEMU</entry>
    <entry name='product'>Standard PC (i440FX + PIIX, 1996)</entry>
    <entry name='version'>pc-i440fx-bionic</entry>
    <entry name='serial'>Not Specified</entry>
    <entry name='uuid'>E6556E18-0974-4B33-A269-49EA8D1911D6</entry>
    <entry name='sku'>Not Specified</entry>
    <entry name='family'>Not Specified</entry>
  </system>
  <processor>
    <entry name='socket_destination'>CPU 0</entry>
    <entry name='type'>Central Processor</entry>
    <entry name='family'>Other</entry>
    <entry name='manufacturer'>QEMU</entry>
    <entry name='version'>pc-i440fx-bionic</entry>
    <entry name='external_clock'>Unknown</entry>
    <entry name='max_speed'>2000 MHz</entry>
    <entry name='status'>Populated, Enabled</entry>
    <entry name='serial_number'>Not Specified</entry>
    <entry name='part_number'>Not Specified</entry>
  </processor>
  <processor>
    <entry name='socket_destination'>CPU 1</entry>
    <entry name='type'>Central Processor</entry>
    <entry name='family'>Other</entry>
    <entry name='manufacturer'>QEMU</entry>
    <entry name='version'>pc-i440fx-bionic</entry>
    <entry name='external_clock'>Unknown</entry>
    <entry name='max_speed'>2000 MHz</entry>
    <entry name='status'>Populated, Enabled</entry>
    <entry name='serial_number'>Not Specified</entry>
    <entry name='part_number'>Not Specified</entry>
  </processor>
  <processor>
    <entry name='socket_destination'>CPU 2</entry>
    <entry name='type'>Central Processor</entry>
    <entry name='family'>Other</entry>
    <entry name='manufacturer'>QEMU</entry>
    <entry name='version'>pc-i440fx-bionic</entry>
    <entry name='external_clock'>Unknown</entry>
    <entry name='max_speed'>2000 MHz</entry>
    <entry name='status'>Populated, Enabled</entry>
    <entry name='serial_number'>Not Specified</entry>
    <entry name='part_number'>Not Specified</entry>
  </processor>
  <processor>
    <entry name='socket_destination'>CPU 3</entry>
    <entry name='type'>Central Processor</entry>
    <entry name='family'>Other</entry>
    <entry name='manufacturer'>QEMU</entry>
    <entry name='version'>pc-i440fx-bionic</entry>
    <entry name='external_clock'>Unknown</entry>
    <entry name='max_speed'>2000 MHz</entry>
    <entry name='status'>Populated, Enabled</entry>
    <entry name='serial_number'>Not Specified</entry>
    <entry name='part_number'>Not Specified</entry>
  </processor>
  <memory_device>
    <entry name='size'>16384 MB</entry>
    <entry name='form_factor'>DIMM</entry>
    <entry name='locator'>DIMM 0</entry>
    <entry name='bank_locator'>Not Specified</entry>
    <entry name='type'>RAM</entry>
    <entry name='type_detail'>Other</entry>
    <entry name='speed'>Unknown</entry>
    <entry name='manufacturer'>QEMU</entry>
    <entry name='serial_number'>Not Specified</entry>
    <entry name='part_number'>Not Specified</entry>
  </memory_device>
  <memory_device>
    <entry name='size'>8192 MB</entry>
    <entry name='form_factor'>DIMM</entry>
    <entry name='locator'>DIMM 1</entry>
    <entry name='bank_locator'>Not Specified</entry>
    <entry name='type'>RAM</entry>
    <entry name='type_detail'>Other</entry>
    <entry name='speed'>Unknown</entry>
    <entry name='manufacturer'>QEMU</entry>
    <entry name='serial_number'>Not Specified</entry>
    <entry name='part_number'>Not Specified</entry>
  </memory_device>
</sysinfo>


############## Host info 3: CPU map of host CPUs ##############

CPUs - 4
Availability - [True, True, True, True]

############## Host info 4: CPU stats #################

kernel info - 3396580000000
idle info - 2851774350000000
user info - 6134780000000
iowait info - 337910000000

############# Host info 5: Host security model ###############

apparmor0
```

## **2) 5_2.py :** 
      script that provides one of the guest domians information such as -
			a. Domain ID
			b. UUID
			c. Domain name
			d. Hardware Info such as State, Max memory, available memory, number of CPUs and CPU time

## **Execution:**		
        For more dynamic uses of this script, the script accepts an input in the form of guest domian name
				python 5_2.py <VM-name>
				
## **Sample Executions:**

**(a) root@t11_vm8:~/HW_2# python 5_2.py rvijaya4-VM1**

```
############### Guest Host info 1: Domain ID ################

Guest host ID is 124

############## Guest Host info 2: UUID #################

UUID of the guest domain is 9529451c-72ea-46e2-80df-2cf71968a2b1

############## Guest Host info 3: Is domain persistent ##############

Guest domian is persistent

############## Guest Host info 4: Domain name #################

Domain name is rvijaya4-VM1

############# Guest Host info 5: Hardware Info ###############

State - 1
Max memory - 2097152
Memory available - 2097152
Number of CPUs - 4
CPU time - 141870000000
```

**(b) root@t11_vm8:~/HW_2# python 5_2.py rvijaya4-VM2**

```
############### Guest Host info 1: Domain ID ################

Guest host ID is 129

############## Guest Host info 2: UUID #################

UUID of the guest domain is e08a3756-304c-4dc5-8327-00c72aab3212

############## Guest Host info 3: Is domain persistent ##############

Guest domian is persistent

############## Guest Host info 4: Domain name #################

Domain name is rvijaya4-VM2

############# Guest Host info 5: Hardware Info ###############

State - 1
Max memory - 2097152
Memory available - 2097152
Number of CPUs - 4
CPU time - 124010000000
```

## **3) 5_3.py :** 
                script that monitors the performance of all the guest domians in terms of CPU and Memory usage.

## **Execution:** 		
        python 5_3.py <CPU/MEM> <optional: value of T>
				where, T is a user specified threshold for vCPU usage. If the vCPU usage exceeds this value, an ALERT message is printed on the         screen. And also, ALERT message will be logged into the file ./5_3.log with the following info-
				a. Timestamp
				b. VM name
				c. VM's aggregate vCPU usage
				d. ALERT message

## **Sample Executions:**

**(a) Failed execution:** 

```
python 5_3.py
Execute the program as: 'python 5_3.py <CPU/MEM> <value of T>' 
```   

**(b) root@t11_vm8:~/HW_2# python 5_3.py CPU      -----------------------> lists the VMs in ascending order of their aggregate vCPU usage**

```
############# List of all active domains #############
Domain ID 128
CPU 0 Time 16
CPU 1 Time 22
CPU 2 Time 13
CPU 3 Time 13
Average vCPU time (nano sec): 65
===================================

Listing VMs in ascending order of CPU usage

['128']


pmallyaVM5

Domain ID 124
CPU 0 Time 31
CPU 1 Time 39
CPU 2 Time 39
CPU 3 Time 35
Average vCPU time (nano sec): 145
===================================

Listing VMs in ascending order of CPU usage

['128', '124']


pmallyaVM5

rvijaya4-VM1

Domain ID 130
CPU 0 Time 102
CPU 1 Time 133
CPU 2 Time 130
CPU 3 Time 139
Average vCPU time (nano sec): 505
===================================

Listing VMs in ascending order of CPU usage

['128', '124', '130']


pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

Domain ID 127
CPU 0 Time 14
CPU 1 Time 12
CPU 2 Time 14
CPU 3 Time 23
Average vCPU time (nano sec): 65
===================================

Listing VMs in ascending order of CPU usage

['128', '127', '124', '130']


pmallyaVM5

pmallyaVM4

rvijaya4-VM1

rvijaya4-VM3

Domain ID 131
CPU 0 Time 31
CPU 1 Time 17
CPU 2 Time 19
CPU 3 Time 15
Average vCPU time (nano sec): 84
===================================

Listing VMs in ascending order of CPU usage

['128', '127', '131', '124', '130']


pmallyaVM5

pmallyaVM4

rvijaya4-VM4

rvijaya4-VM1

rvijaya4-VM3

Domain ID 49
CPU 0 Time 693
CPU 1 Time 747
CPU 2 Time 922
CPU 3 Time 802
Average vCPU time (nano sec): 3165
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '131', '124', '130', '49']


pmallyaVM4

pmallyaVM5

rvijaya4-VM4

rvijaya4-VM1

rvijaya4-VM3

pmallyalab2VM2

Domain ID 48
CPU 0 Time 770
CPU 1 Time 817
CPU 2 Time 954
CPU 3 Time 818
Average vCPU time (nano sec): 3361
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '131', '124', '130', '49', '48']


pmallyaVM4

pmallyaVM5

rvijaya4-VM4

rvijaya4-VM1

rvijaya4-VM3

pmallyalab2VM2

pmallyaVM1

Domain ID 80
CPU 0 Time 46
CPU 1 Time 52
CPU 2 Time 52
CPU 3 Time 46
Average vCPU time (nano sec): 197
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '131', '124', '80', '130', '49', '48']


pmallyaVM4

pmallyaVM5

rvijaya4-VM4

rvijaya4-VM1

pmallyaVMX

rvijaya4-VM3

pmallyalab2VM2

pmallyaVM1

Domain ID 129
CPU 0 Time 28
CPU 1 Time 35
CPU 2 Time 30
CPU 3 Time 31
Average vCPU time (nano sec): 126
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '131', '129', '124', '80', '130', '49', '48']


pmallyaVM4

pmallyaVM5

rvijaya4-VM4

rvijaya4-VM2

rvijaya4-VM1

pmallyaVMX

rvijaya4-VM3

pmallyalab2VM2

pmallyaVM1

```

**(c) root@t11_vm8:~/HW_2# python 5_3.py MEM			-------------------------------> Lists VMs in ascending order based on their Memory usage**

```
############# List of all active domains #############
Domain ID 128
Mmeory used:
 0
 1881604
 1691100
 2097152
 199
 0
 1570570085
 1742416
 177931
 513616
Average memory usage is: 157867410
=================================

Listing VMs in ascending order of MEM usage

['128']


pmallyaVM5

Domain ID 124
Mmeory used:
 0
 1883072
 1686900
 2097152
 199
 0
 1570570422
 1741468
 176318
 569308
Average memory usage is: 315739894
=================================

Listing VMs in ascending order of MEM usage

['128', '124']


pmallyaVM5

rvijaya4-VM1

Domain ID 130
Mmeory used:
 0
 2047940
 1801704
 2097152
 157
 0
 1570572170
 1780128
 321471
 2239040
Average memory usage is: 473825870
=================================

Listing VMs in ascending order of MEM usage

['128', '124', '130']


pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

Domain ID 127
Mmeory used:
 0
 1881604
 1694272
 2097152
 197
 0
 1570570084
 1746496
 174218
 534120
Average memory usage is: 631695684
=================================

Listing VMs in ascending order of MEM usage

['128', '124', '130', '127']


pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

pmallyaVM4

Domain ID 131
Mmeory used:
 0
 2047940
 1804196
 2097152
 156
 0
 1570573080
 1782528
 322671
 1142296
Average memory usage is: 789672686
=================================

Listing VMs in ascending order of MEM usage

['128', '124', '130', '127', '131']


pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

pmallyaVM4

rvijaya4-VM4

Domain ID 49
Mmeory used:
 0
 1881600
 1695580
 2097152
 196
 0
 1570478082
 1747620
 175646
 2094272
Average memory usage is: 947689701
=================================

Listing VMs in ascending order of MEM usage

['128', '124', '130', '127', '131', '49']


pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

pmallyaVM4

rvijaya4-VM4

pmallyalab2VM2

Domain ID 48
Mmeory used:
 0
 1881600
 1687904
 2097152
 194
 0
 1570477487
 1739788
 174546
 1313348
Average memory usage is: 1105626903
=================================

Listing VMs in ascending order of MEM usage

['128', '124', '130', '127', '131', '49', '48']


pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

pmallyaVM4

rvijaya4-VM4

pmallyalab2VM2

pmallyaVM1

Domain ID 80
Mmeory used:
 0
 1881604
 1686760
 2097152
 168
 0
 1570556868
 1730552
 180787
 595284
Average memory usage is: 1263499820
=================================

Listing VMs in ascending order of MEM usage

['128', '124', '130', '127', '131', '49', '48', '80']


pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

pmallyaVM4

rvijaya4-VM4

pmallyalab2VM2

pmallyaVM1

pmallyaVMX

Domain ID 129
Mmeory used:
 0
 1883072
 1701364
 2097152
 177
 0
 1570570479
 1757204
 172093
 804752
Average memory usage is: 1421398450
=================================

Listing VMs in ascending order of MEM usage

['128', '124', '130', '127', '131', '49', '48', '80', '129']


pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

pmallyaVM4

rvijaya4-VM4

pmallyalab2VM2

pmallyaVM1

pmallyaVMX

rvijaya4-VM2

```

**(d) root@t11_vm8:~/HW_2# python 5_3.py CPU 130				---------------------------> Lists VMs in ascending order based on their vCPU usage and also alerts about a usage higher than the threshold 130**

```
############# List of all active domains #############
Domain ID 128
CPU 0 Time 16
CPU 1 Time 23
CPU 2 Time 13
CPU 3 Time 13
Average vCPU time (nano sec): 67
===================================

Listing VMs in ascending order of CPU usage

['128']


pmallyaVM5

Domain ID 124
CPU 0 Time 31
CPU 1 Time 39
CPU 2 Time 39
CPU 3 Time 36
ALERT! CPU usage exceeds the threshold!
Average vCPU time (nano sec): 147
===================================

Listing VMs in ascending order of CPU usage

['128', '124']


pmallyaVM5

rvijaya4-VM1

Domain ID 130
CPU 0 Time 104
CPU 1 Time 134
CPU 2 Time 130
CPU 3 Time 140
ALERT! CPU usage exceeds the threshold!
Average vCPU time (nano sec): 509
===================================

Listing VMs in ascending order of CPU usage

['128', '124', '130']


pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

Domain ID 127
CPU 0 Time 14
CPU 1 Time 12
CPU 2 Time 15
CPU 3 Time 23
Average vCPU time (nano sec): 66
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '124', '130']


pmallyaVM4

pmallyaVM5

rvijaya4-VM1

rvijaya4-VM3

Domain ID 131
CPU 0 Time 32
CPU 1 Time 18
CPU 2 Time 19
CPU 3 Time 15
Average vCPU time (nano sec): 86
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '131', '124', '130']


pmallyaVM4

pmallyaVM5

rvijaya4-VM4

rvijaya4-VM1

rvijaya4-VM3

Domain ID 49
CPU 0 Time 693
CPU 1 Time 747
CPU 2 Time 922
CPU 3 Time 802
ALERT! CPU usage exceeds the threshold!
Average vCPU time (nano sec): 3165
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '131', '124', '130', '49']


pmallyaVM4

pmallyaVM5

rvijaya4-VM4

rvijaya4-VM1

rvijaya4-VM3

pmallyalab2VM2

Domain ID 48
CPU 0 Time 770
CPU 1 Time 817
CPU 2 Time 954
CPU 3 Time 818
ALERT! CPU usage exceeds the threshold!
Average vCPU time (nano sec): 3361
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '131', '124', '130', '49', '48']


pmallyaVM4

pmallyaVM5

rvijaya4-VM4

rvijaya4-VM1

rvijaya4-VM3

pmallyalab2VM2

pmallyaVM1

Domain ID 80
CPU 0 Time 46
CPU 1 Time 52
CPU 2 Time 53
CPU 3 Time 46
ALERT! CPU usage exceeds the threshold!
Average vCPU time (nano sec): 199
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '131', '124', '80', '130', '49', '48']


pmallyaVM4

pmallyaVM5

rvijaya4-VM4

rvijaya4-VM1

pmallyaVMX

rvijaya4-VM3

pmallyalab2VM2

pmallyaVM1

Domain ID 129
CPU 0 Time 29
CPU 1 Time 37
CPU 2 Time 31
CPU 3 Time 32
Average vCPU time (nano sec): 129
===================================

Listing VMs in ascending order of CPU usage

['127', '128', '131', '129', '124', '80', '130', '49', '48']


pmallyaVM4

pmallyaVM5

rvijaya4-VM4

rvijaya4-VM2

rvijaya4-VM1

pmallyaVMX

rvijaya4-VM3

pmallyalab2VM2

pmallyaVM1
```

**5_3.log snippet**

```
INFO:root: 22:52:35.856525 ALERT! CPU usage exceeds the threshold of 130 for rvijaya4-VM1  with CPU usage of 147
INFO:root: 22:52:35.858480 ALERT! CPU usage exceeds the threshold of 130 for rvijaya4-VM3  with CPU usage of 508
INFO:root: 22:52:35.864951 ALERT! CPU usage exceeds the threshold of 130 for pmallyalab2VM2  with CPU usage of 3165
INFO:root: 22:52:35.867461 ALERT! CPU usage exceeds the threshold of 130 for pmallyaVM1  with CPU usage of 3361
INFO:root: 22:52:35.870147 ALERT! CPU usage exceeds the threshold of 130 for pmallyaVMX  with CPU usage of 199
INFO:root: 22:53:06.321332 ALERT! CPU usage exceeds the threshold of 130 for rvijaya4-VM1  with CPU usage of 147
INFO:root: 22:53:06.323853 ALERT! CPU usage exceeds the threshold of 130 for rvijaya4-VM3  with CPU usage of 509
INFO:root: 22:53:06.329865 ALERT! CPU usage exceeds the threshold of 130 for pmallyalab2VM2  with CPU usage of 3165
INFO:root: 22:53:06.332080 ALERT! CPU usage exceeds the threshold of 130 for pmallyaVM1  with CPU usage of 3361
INFO:root: 22:53:06.334415 ALERT! CPU usage exceeds the threshold of 130 for pmallyaVMX  with CPU usage of 199
```
