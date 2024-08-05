# importing libraries
import subprocess as sp
import optparse as opt
import re

# getting parameters from user at terminal
def get_parameters():
    parse_obj = opt.OptionParser()
    parse_obj.add_option("-i", "--interface", dest="interface", help="interface to change")
    parse_obj.add_option("-m", "--mac", dest="MAC_adress", help="new mac adress")
    #get MAC and interface from parameters
    (user_inputs, arguments) = parse_obj.parse_args()
    user_interface = user_inputs.interface
    user_new_mac = user_inputs.MAC_adress
    return user_interface, user_new_mac

# changing mac
def mac_change(user_interface, user_new_mac):
    sp.call(["ifconfig", user_interface, "down"])
    sp.call(["ifconfig", user_interface, "hw", "ether", user_new_mac])
    sp.call(["ifconfig", user_interface, "up"])

# controlling new mac adress to see if it is changed successfull
def mac_control(interface, MAC_adress):
    ifconfig_output = sp.check_output(["ifconfig", interface])
    new_mac = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)  #getting MAC from output of ifconfig
    new_mac_str = new_mac.group().decode("utf-8")
    if new_mac_str == MAC_adress:
        print("MAC changed successfully. Good anonymity.")
        print("New MAC: " + MAC_adress + " for " + interface)  # final message
    else:
        print("ERROR: new MAC does not match with current MAC. Sorry bro.")
        print(new_mac_str)

def __main__():
    print("MAC is changing ...") # start message
    interface = "wlan0"
    MAC_adress = "00:22:33:11:22:33"
    interface, MAC_adress = get_parameters()
    mac_change(interface, MAC_adress)
    mac_control(interface, MAC_adress)


__main__()



