"""
TODO:
1. Add clear_data() - done
2. Add launch_app()
3. Add get_app_version()
4. Add take_screenshot()
5. Add is_app_in_foreground()
"""
from data_models.app_protos import AppConfig

class AppController:

    def __init__(self, ad_device):
        self.ad = ad_device

    def is_installed(self, config: AppConfig) -> bool:
        """ Checks if the specified package is installed by ADB commands, 
        (list and filter by name) 
        """
        self.ad.log.info('AppController: Checking if %s is installed...', config.package_name)

        try:
            output = self.ad.adb.shell(f'pm list packages {config.package_name}')

            if isinstance(output, bytes):
                output = output.decode('utf-8')

            return f"package:{config.package_name}" in output
        
        except Exception as e:
            self.ad.log.error("AppController: Failed to check package %s", e)
            return False

    def force_stop(self, config: AppConfig):
        """ Force stops the specified package """
        self.ad.log.info('AppController: Force stopping %s ...', config.package_name)
        self.ad.adb.shell(f'am force-stop {config.package_name}')

    def install(self, config: AppConfig):
        """ install apk through ADB command and calls "is_installed" func to do double check """
        self.ad.log.info('AppController: Start installing APK %s', config.target_app_pkg)

        try:
            self.ad.adb.install(['-r', config.test_app_path])

        except Exception as e:
            error_msg = str(e).lower()
            if 'offline' in error_msg or 'not found' in error_msg or 'disconnected' in error_msg:
                self.ad.log.error(f"AppController: device disconnection, fail to install {config.target_app_pkg}")
                raise RuntimeError(f"ADB connection error: {e}")

            self.ad.log.error('AppController: Failed to install %s. Error: %s', config.target_app_pkg, e)
            return False

        return self.is_installed(config)

    def uninstall(self, config: AppConfig):
        """
        step 1: check if the apk doesn't exist, return True directly
        step 2: execute the adb command, using try-except to do error handing
        step 3: if the apk has been un-installed, return true, else false.
        """
        self.ad.log.info('AppController: Start uninstalling APK %s', config.target_app_pkg)
        if not self.is_installed(config):
            self.ad.log.info('AppController: %s is already been uninstalled', config.target_app_pkg)
            return True

        try:
            self.ad.adb.uninstall(config.test_app_name)

        except Exception as e:
            error_msg = str(e).lower()
            if 'offline' in error_msg or 'not found' in error_msg or 'disconnected' in error_msg:
                self.ad.log.error('AppController: device disconnection, fail to uninstall {config.target_app_pkg}')
                raise RuntimeError(f"ADB connection error: {e}")

            self.ad.log.error('AppController: adb uninstall command failed. Error: %s', e)
            return False

        """ Recheck if the app is uninstalled """
        is_still_present = self.is_installed(config)

        if is_still_present:
            self.ad.log.error('AppController: Failed to uninstall %s. It still exists.', config.target_app_pkg)
            return False

        self.ad.log.info('AppController: %s uninstalled successfully', config.target_app_pkg)
        return True
    
    def clear_data(self, config: AppConfig):
        """
        Step 1: call isinstalled(), if false, use log error
        Step 2: execute the ADB command, using try-except to do error handing
        Step 3: secure the success msg
        """
        self.ad.log.info('AppController: Executing %s data cleaning proccess...', config.target_app_pkg)
        if not self.is_installed(config):
            self.ad.log.info('AppController: %s is not installed, no need to clear data.', config.target_app_pkg)
            return True
        
        try:
            raw_output = self.ad.adb.shell(['pm', 'clear', config.target_app_pkg])

        except Exception as e:
            error_msg = str(e).lower()
            if 'offline' in error_msg or 'not found' in error_msg or 'disconnected' in error_msg:
                self.ad.log.error(f'AppController: device disconnection, fail to clear {config.target_app_pkg}')
                raise RuntimeError(f"ADB connection error: {e}")

            self.ad.log.error('AppController: adb clear command failed. Error: %s', e)
            return False

        """ Check log msg if the data of apk has been cleanned """
        msg = raw_output.decode('utf-8').lower() if isinstance(raw_output, bytes) else str(raw_output).lower()
        if 'success' in msg:
            self.ad.log.info('AppController: Data of %s has been cleared successfully.', config.target_app_pkg)
            return True

        self.ad.log.error('AppController: Fail to clear %s.', config.target_app_pkg)
        return False