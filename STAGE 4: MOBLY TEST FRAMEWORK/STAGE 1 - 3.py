"""
STAGE 1 - 3
The HelloWorldTest:
    - Register DUT through .yaml which will be read by the controller
    - Print hello world / serial number / android version(through ADB command)
"""

from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class HelloWorldTest(base_test.BaseTestClass):

    def setup_class(self):
        """
        Register Android device controller.
        The controller will read the config file and find the AndroidDevice.
        """
        self.ads = self.register_controller(android_device)

        """ Get the first DUT in list """
        self.dut = self.ads[0]

    def test_get_device_info(self):
        """ Get device serial number and Android version """
        serial = self.dut.serial

        """ Use ADB shell to get build info directly, 
            For reality DUT, can use:
            android_version = self.dut.build_info['build_version_release']
            adb.shell returns bytes, so we decode and strip whitespace
        """
            
        android_version = self.dut.adb.shell('getprop ro.build.version.release').decode('utf-8').strip()

        self.dut.log.info('Hello World! Device has been connected')
        self.dut.log.info('Serial Number: %s', serial)
        self.dut.log.info('Android Version: %s', android_version)
        
if __name__ == '__main__':
    test_runner.main()
