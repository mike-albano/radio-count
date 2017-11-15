#!/usr/bin/env python

#### the formula ####
# 1. Application Mbps / Device Capability Max MCS * .6 * 100 = % of airtime (per device)
# 2. % of airtime (per device) * # of devices = % of total airtime needed
# 3. % of total airtimes / 80 (rounded up to whole #) = # of radios
####
# device capability max MCS based on your expected max MCS rate.
# Default is MCS 8
# Last updated 2017-11-14 by Mike Albano
####

# define the formula
def df_formula():
    # mult. by 100 to turn result into percent of 100
    # get air-time usage for each device type & chan-width
    app_airtime_20 = (float(app_mbps) / ss_20_max) * 100
    app_airtime_2ss_20 = (float(app_mbps) / two_20_max) * 100
    app_airtime_3ss_20 = (float(app_mbps) / three_20_max) * 100
    app_airtime_40 = (float(app_mbps) / ss_40_max) * 100
    app_airtime_2ss_40 = (float(app_mbps) / two_40_max) * 100
    app_airtime_3ss_40 = (float(app_mbps) / three_40_max) * 100
    # add up the total amount of airtime used by all clients
    device_airtime = (app_airtime_20 * float(ss_devices_20)) + (app_airtime_2ss_20 * float(two_ss_devices_20)) + (app_airtime_3ss_20 * float(three_ss_devices_20)) + (app_airtime_40 * float(ss_devices_40)) + (app_airtime_2ss_40 * float(two_ss_devices_40)) + (app_airtime_3ss_40 * float(three_ss_devices_40))
    #determine # of radios and round up for # of AP's
    radios = device_airtime / 80.0
    print "you need %.2f radios" % (radios)

# Define default Max Mbps (MCS 8) of devices for 20 & 40MHz channel widths.
ss_20_max = 86.7 * .6
two_20_max = 173.3 * .6
three_20_max = 260 * .6
ss_40_max = 180 * .6
two_40_max = 360 * .6
three_40_max = 540 * .6

# Questions/Input from user
app_mbps = raw_input("Application(s) TCP/UDP throughput in Mbps [default 1]> ")
if not app_mbps:
    app_mbps = 1.0
chan_width = raw_input("What channel width (20/40) will you be supporting? [default 20] > ")
# if 40MHz chan-width in use, obtain number of capable clients
if chan_width == '40':
    ss_devices_40 = raw_input("How many concurrent 40MHz capable Single Stream devices(eg Smartphones) [default 100] > ")
    if not ss_devices_40:
      ss_devices_40 = 100.0
    two_ss_devices_40 = raw_input("How many concurrent 40MHz capable two Spatial Stream devices(eg tablets) [default 100] > ")
    if not two_ss_devices_40:
      two_ss_devices_40 = 100.0
    three_ss_devices_40 = raw_input("How many concurrent 40MHz capable three Spatial Stream devices(eg laptops)? [default 50] > ")
    if not three_ss_devices_40:
      three_ss_devices_40 = 50.0
elif chan_width != '40':
    ss_devices_40 = 0.0
    two_ss_devices_40 = 0.0
    three_ss_devices_40 = 0.0

# obtain number of 20MHz capable clients
ss_devices_20 = raw_input("How many concurrent 20MHz Single Stream devices(eg Smartphones) [default 100] > ")
if not ss_devices_20:
    ss_devices_20 = 100.0
two_ss_devices_20 = raw_input("How many concurrent 20MHz two Spatial Stream devices(eg tablets)? [default 100] > ")
if not two_ss_devices_20:
    two_ss_devices_20 = 100.0
three_ss_devices_20 = raw_input("How many concurrent 20MHz three Spatial Stream devices(eg laptops)? [default 50] > ")
if not three_ss_devices_20:
    three_ss_devices_20 = 50.0

modify_max = raw_input("Would you like to modify the max MCS [default 8]? Type 'help' for more info [yes,no,help] > ")
if modify_max == 'help':
    print "Default max MCS is MCS 8. You can enter a new value, which changes each clients max TCP/UDP capabilities (based on MCS value). For example, if you enter 0, the new MCS values will be 0, or 7.2Mbps (4.3Mbps IP tput)."
    modify_max = raw_input("Would you like to modify the max MCS? [yes,no] > ")

if modify_max == 'yes':
    max_factor = raw_input("what would you like the max MCS rate to be? [0-9] > ")
    # change the 'max tcp/udp' values, based on user input
    if max_factor == '0':
      ss_20_max /=  12.0
      two_20_max /=  12.0
      three_20_max /= 12.0
    elif max_factor == '1':
      ss_20_max /= 6.0
      two_20_max /= 6.0
      three_20_max /= 6.0
    elif max_factor == '2':
      ss_20_max /= 4.0
      two_20_max /= 4.0
      three_20_max /= 4.0
    elif max_factor == '3':
      ss_20_max /= 3.0
      two_20_max /= 3.0
      three_20_max /= 3.0
    elif max_factor == '4':
      ss_20_max /= 2.0
      two_20_max /= 2.0
      three_20_max /= 2.0
    elif max_factor == '5':
      ss_20_max /=  1.5
      two_20_max /= 1.5
      three_20_max /= 1.5
    elif max_factor == '6':
      ss_20_max /= 1.33
      two_20_max /= 1.33
      three_20_max /= 1.33
    elif max_factor == '7':
      ss_20_max /= 1.2
      two_20_max /= 1.2
      three_20_max /= 1.2
    elif max_factor == '9':
      ss_20_max *= 1.11
      two_20_max *= 1.11
      three_20_max *= 1.11
    # mult. by 2.08 for 40mhz
    ss_40_max = float(2.08 * ss_20_max)
    two_40_max = float(2.08 * two_20_max)
    three_40_max = float(2.08 * three_20_max)

    df_formula()
else:
    df_formula()
