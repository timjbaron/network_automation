# Branch template configuration script
t = open(r"switch_branch_template.txt", "r")
tempstr = t.read()
t.close()

# To debug file import, uncomment the following line
#print(tempstr)

print('What is the hostname of the device?')
HOSTNAME = input()

print('What is the branch IP number? Example: type 28 for 10.28.10.1')
IPXX = input()

print('What City is the branch in? Example: Paris')
CITY = input()

print('What State or Country is the branch in? Example: France')
STATE = input()

print('How many switches will the branch have?')
switch_number = int(input())

switch_dict = {}
for i in range(switch_number):
    switchnumber = i
    print("What is the serial number of switch ",i,"?")
    switch_dict.update( {switchnumber: input()})

add_sw_ports = ""
add_sw_vr_chass = ""

for k, v in switch_dict.items():
    if k > 1:
        k = str(k)
        add_sw_ports += ("set interfaces interface-range access_ports member-range ge-"+k+"/0/1 to ge-"+k+"/0/47\n")
        add_sw_vr_chass += ("set virtual-chassis member "+k+" serial-number "+v+" role line-card\n")

# Uncomment the below for debugging branch variables
#print(HOSTNAME)
#print(IPXX)
#print(CITY)
#print(STATE)
#print(switch_dict[0])
#print(switch_dict[1])
#print(switch_dict[2])

CITY_STATE = CITY + '-' + STATE

device_values = {
    '[HOSTNAME]': HOSTNAME,
    '[XX]': IPXX,
    '[Name]': CITY,
    '[Location]': CITY_STATE,
    '[Serial_1]': switch_dict[0],
    '[Serial_2]': switch_dict[1],
    '/*additional_swch_ports*/': add_sw_ports, 
    '/*additional_swch_vr_chas*/': add_sw_vr_chass,
    }

for key,val in device_values.items():
    tempstr = tempstr.replace(key,val)

print(tempstr)

    
