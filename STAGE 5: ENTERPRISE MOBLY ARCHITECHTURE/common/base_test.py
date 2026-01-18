from mobly import base_test
from mobly.controllers import android_device
from libs.wifi_controller import WifiController

class EnterpriseBaseTest(base_test.BaseTestClass):
    """
    Base class for enterprise tests, handling device setup and controller injection.
    """

    def setup_class(self):
        """ Register the Android device controller """
        self.ads = self.register_controller(android_device)
        self.dut = self.ads[0]

        """ Load the snippet package (required for WifiController to function) """
        self.dut.load_snippet('mbs', 'com.google.android.mobly.snippet.bundled')

        """ Dependency Injection: Create WifiController instance with the device """
        self.wifi_controller = WifiController(self.dut)
