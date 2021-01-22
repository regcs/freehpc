# ############################## LICENSE BLOCK ###############################
#
# MIT License
#
# Copyright © 2021 Yann Vernier, Christian Stolze
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ############################################################################

import freehpc
import ctypes
from math import *

# initialize free HoloPlayCore
hpc = freehpc.freeHoloPlayCoreAPI()
errco = hpc.InitializeApp('Test', hpc.license_type.LICENSE_NONCOMMERCIAL.value)
if errco == 0:

    # allocate string buffer
    buffer = ctypes.create_string_buffer(1000)

    # get HoloPlay Core SDK version
    hpc.GetHoloPlayCoreVersion(buffer, 1000)
    print(" # Free HoloPlay Core version: " + buffer.value.decode('ascii').strip())

    # get HoloPlay Service Version
    hpc.GetHoloPlayServiceVersion(buffer, 1000)
    print(" # HoloPlay Service version: " + buffer.value.decode('ascii').strip())

    # get number of devices
    print(" # Number of connected displays: " + str(hpc.GetNumDevices()))

    for i in range(hpc.GetNumDevices()):
        print(" # Device %i" % i)

        # get device HDMI name
        hpc.GetDeviceHDMIName(i, buffer, 1000)
        dev_hdmi = buffer.value.decode('ascii').strip()

        # get device serial
        hpc.GetDeviceSerial(i, buffer, 1000)
        dev_serial = buffer.value.decode('ascii').strip()

        # get device type
        hpc.GetDeviceType(i, buffer, 1000)
        dev_type = buffer.value.decode('ascii').strip()

        print("  - hdmi:", dev_hdmi)
        print("  - serial:", dev_serial)
        print("  - type:", dev_type)
        # Calibration information
        print("  - x:", hpc.GetDevicePropertyWinX(i))
        print("  - y:", hpc.GetDevicePropertyWinY(i))
        print("  - width:", hpc.GetDevicePropertyScreenW(i))
        print("  - height:", hpc.GetDevicePropertyScreenH(i))
        print("  - aspect:", hpc.GetDevicePropertyDisplayAspect(i))
        print("  - pitch:", hpc.GetDevicePropertyPitch(i))
        print("  - tilt:", hpc.GetDevicePropertyTilt(i))
        print("  - center:", hpc.GetDevicePropertyCenter(i))
        print("  - subp:", hpc.GetDevicePropertySubp(i))
        print("  - fringe:", hpc.GetDevicePropertyFringe(i))
        print("  - ri:", hpc.GetDevicePropertyRi(i))
        print("  - bi:", hpc.GetDevicePropertyBi(i))
        print("  - invView:", hpc.GetDevicePropertyInvView(i))
        print("  - viewCone:", hpc.GetDevicePropertyFloat(i, b"/calibration/viewCone/value"))

    hpc.CloseApp()
