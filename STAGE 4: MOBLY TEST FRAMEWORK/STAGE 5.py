"""
Stage 5: Advanced Device Interaction
  - Android Debug Bridge (ADB) commands via Mobly
  - File Transfer (Pushing test data, pulling logs)
  - Network Interaction (Ping/HTTP requests from the device side)

  Execute:
  - Create a test that forces the phone to connect to a specific Wi-Fi network,
    and pings a public IP (e.g., 8.8.8.8) to validate internet connectivity.

"""

import time
from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class WifiConnectTest(base_test.BaseTestClass):

    def setup_class(self):
        self.ads = self.register_controller(android_device)
        self.dut = self.ads[0]
        self.dut.load_snippet('mbs', 'com.google.android.mobly.snippet.bundled')

    def test_connect_wifi_and_ping(self):
        """
        Connect to a specific Wi-Fi and verify internet.
        
        Read parameters from config.yaml
        usage: self.user_params.get('key', 'default_value')
        """
        ssid = self.user_params.get('wifi_ssid', 'AndroidWifi')
        pwd = self.user_params.get('wifi_pwd', '')

        self.dut.log.info('Connecting to Wi-Fi: %s', ssid)
        self.dut.mbs.makeToast('Connecting to %s...' % ssid)

        """ Turn on Wi-Fi via ADB first """
        self.dut.adb.shell('cmd wifi set-wifi-enabled enabled')
        time.sleep(5)

        """
        Use wifiConnectSimple() for simpler code.
        -> wifiConnectSimple(ssid, pwd)
        
        Pass None if pwd is empty so Java treats it as an Open network (null)
        Python None -> Java null
        """
        self.dut.mbs.wifiConnectSimple(ssid, pwd if pwd else None)

        """ Verify Internet: Ping 8.8.8.8 """
        self.dut.log.info('Pinging Google DNS (8.8.8.8)...')

        """ -c 1: count 1 packet, -w 5: wait max 5 seconds """
        ping_result = self.dut.adb.shell('ping -c 1 -w 5 8.8.8.8').decode('utf-8')
        self.dut.log.info('Ping Result: %s', ping_result)

        if '1 packets transmitted, 1 received' in ping_result:
            self.dut.mbs.makeToast('Ping Success!')
        else:
            self.dut.mbs.makeToast('Ping Failed!')

if __name__ == '__main__':
    test_runner.main()
