"""
Testcase_1: Check the initial app exists and force stop
    - define the proto:
        1. set target app name in yaml(user_params)
        2. setup into the proto(AppConfig)
    - execute the test logic:
        1. use / prior the functions in app_controller(is_installed(), force_stop())
"""
import sys
import os

sys.path.insert(0, os.getcwd())
from mobly import test_runner
from mobly import asserts
from common.base_test import EnterpriseBaseTest
from data_models.app_protos import AppConfig

class AppManagementTest(EnterpriseBaseTest):

    def test_builtin_app_exists_and_force_stop(self):
        """ Update the proto """
        pkg_name = self.user_params.get('target_app_pkg', 'com.android.settings')
        app_config = AppConfig(package_name = pkg_name)

        """ Check if app is installed through controller """
        is_installed = self.app_controller.is_installed(app_config)
        asserts.assert_true(is_installed, f"Expected app {pkg_name} to be installed, but None")

        """ Force stop """
        self.app_controller.force_stop(app_config)
        self.dut.log.info("Test passed: %s is intalled and forced stopped", pkg_name)

    def test_fake_app_not_installed(self):
        fake_config = AppConfig(package_name='com.ghost.app.not.exist')

        is_installed = self.app_controller.is_installed(fake_config)
        asserts.assert_false(is_installed, f"Ghost app shouldn't be installed")
        self.dut.log.info("Test passed: Ghost app is correctly identified as not installed")

if __name__ == '__main__':
    del EnterpriseBaseTest
    test_runner.main()


