import sys
import os
import time

sys.path.insert(0, os.getcwd())

from mobly import test_runner
from mobly import asserts
from common.base_test import EnterpriseBaseTest
from data_models.wifi_protos import WifiConfig

class WifiConnectionTest(EnterpriseBaseTest):
    """
    Test class demonstrating the use of Dependency Injection and Datamodels.
    Inherits from EnterpriseBaseTest to access the injected WifiController.
    """

    def test_wifi_connection(self):
        """ 
        1. Instantiate WifiConfig object (Fill out the form/proto)
        Retrieve parameters from config.yaml
        """
        ssid = self.user_params.get('wifi_ssid', 'NoneExistWifi')
        pwd = self.user_params.get('wifi_pwd', '')

        """ Debug Log """
        self.dut.log.info('DEBUG: Target SSID from config is: %s',ssid)

        """ Create the data model (the Contract) """
        wifi_config = WifiConfig(ssid=ssid, password=pwd)

        """ 
        2. Call self.wifi_controller.connect() to execute connection
        The controller is already injected in the BaseTest setup
        """
        self.wifi_controller.connect(wifi_config)

        """
        3. Use asserts.assert_true to verify connection status
        Get current connection details from the snippet
        """

        conn_info = self.dut.mbs.wifiGetConnectionInfo()
        current_ssid = conn_info.get('SSID')

        self.dut.log.info('Current SSID on device: %s', current_ssid)

        """
        Verify that the current SSID matches the target SSID
        Note: Android might return SSID enclosed in quotes (e.g., "AndroidWifi")
        """

        is_connected = ssid in current_ssid if current_ssid else False

        asserts.assert_true(
            is_connected,
            'Connection failed. Expected SSID: %s, but connected to: %s' % (ssid, current_ssid)
        )

if __name__ == '__main__':
    # Remove the base class from the namespace to prevent Mobly from trying to run it
    del EnterpriseBaseTest
    test_runner.main()