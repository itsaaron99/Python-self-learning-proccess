""" 
STAGE 4: RPC & Snippets (System Control)
  - JSON-RPC Concepts (How Python talks to Java) 
  - Compiling and installing `mobly-bundled-snippets`
  - Calling Android System APIs (Wi-Fi, Settings, Telephony) via Python

  Execute: 
    - Write a test case that controls the phone's hardware: Turn Wi-Fi ON, 
      verify the state is "Enabled", then turn it OFF and verify it is "Disabled".

"""
import time
from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class WifiToggleTest(base_test.BaseTestClass):

    def setup_class(self):
        """
        Register Android device controller.
        The controller will read the config file and find the AndroidDevice.
        """
        self.ads = self.register_controller(android_device)

        """ Get the first DUT in list """
        self.dut = self.ads[0]

        """ Load the Mobly Bundled Snippets (MBS) to execute test_runner """
        self.dut.load_snippet('mbs', 'com.google.android.mobly.snippet.bundled')

    def test_get_device_info(self):
        """ Get device serial number and Android version """
        serial = self.dut.serial
        android_version = self.dut.adb.shell('getprop ro.build.version.release').decode('utf-8').strip()
        self.dut.log.info('Serial Number: %s', serial)
        self.dut.log.info('Android Version: %s', android_version)
        
    def test_wifi_toggle(self):
        """ Test toggling Wi-Fi on and off using Snippets. """
        """ Making toast, will show UI with messages """
        self.dut.mbs.makeToast('Starting Wi-Fi Test...')
        
        self.dut.log.info('Turning Wi-Fi ON...')
        """ Use ADB command because setWifiEnabled is deprecated/restricted in Java API on Android 10+ """
        self.dut.adb.shell('cmd wifi set-wifi-enabled enabled')
        
        """ Wait for the state change """
        time.sleep(3)
        
        """ Verify Wi-Fi is enabled using ADB """
        status_output = self.dut.adb.shell('cmd wifi status').decode('utf-8')
        
        """ Check if the string 'Wifi is enabled' exists in the output (Returns True/False) """
        is_wifi_on = 'Wifi is enabled' in status_output
        self.dut.log.info('Wi-Fi State after ON: %s', is_wifi_on)

        time.sleep(5)
        """ Show a toast using Snippet to prove Snippets are working """
        self.dut.mbs.makeToast('Mobly: Wi-Fi Test Completed')
        
        self.dut.log.info('Turning Wi-Fi OFF...')
        self.dut.adb.shell('cmd wifi set-wifi-enabled disabled')

if __name__ == '__main__':
    test_runner.main()
