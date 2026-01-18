"""
Stage 6: Log Analysis & Debugging
  - Understanding Mobly Test Results (`test_summary.yaml`)
  - Analyzing `logcat` (Android system logs) captured by Mobly
  - Filtering logs for specific crash or error patterns

  Execute:
  - Intentionally write a failing test, run it,
    and locate the specific error trace and device logcat in the Mobly output directory.
"""

from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class WifiFailureTest(base_test.BaseTestClass):

    def setup_class(self):
        self.ads = self.register_controller(android_device)
        self.dut = self.ads[0]
        self.dut.load_snippet('mbs', 'com.google.android.mobly.snippet.bundled')

    def test_connect_failure(self):
        """
        Intentionally try to connect to a non-exist Wi-Fi network.
        Expect test fail and generate error logs.
        """

        """ Intentionally wrong SSID """
        wrong_ssid = "ThisWifiDoesNotExist_12345"

        self.dut.log.info('Attempting to connect to non-existent Wi-Fi: %s', wrong_ssid)
        self.dut.mbs.makeToast('Stage 6: Intentional Failure Test')

        """ This is expected to raise an exception (SnippetError or Timeout) """
        self.dut.mbs.wifiConnectSimple(wrong_ssid, None)

        assert False, "Test should have failed but didn't!"

        """command -> python3 "STAGE 6.py" -c config.yaml --log_path ./logs_stage6 """


if __name__ == '__main__':
    test_runner.main()