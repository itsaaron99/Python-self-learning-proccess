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

    def launch_app(self, config: AppConfig):
        """
        1. check if app is installed
        2. using try-except to execute the ABD command: 
            "adb shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1"
        3. call func is_app_in_foreground() to check if app has been activated.
        """
        self.ad.log.info('AppController: Launching %s...', config.target_app_pkg)
        if not self.is_installed(config):
            self.ad.log.error('AppController: %s is not installed, please try again.', config.target_app_pkg)
            return False
        
        try:
            self.ad.adb.shell(['monkey', '-p', config.target_app_pkg, '-c', 'android.intent.category.LAUNCHER', '1'])

        except Exception as e:
            error_msg = str(e).lower()
            if 'offline' in error_msg or 'not found' in error_msg or 'disconnected' in error_msg:
                self.ad.log.error(f'AppController: device disconnection, fail to launch {config.target_app_pkg}')
                raise RuntimeError(f"ADB connection error: {e}")

            self.ad.log.error('AppController: adb launch command failed. Error: %s', e)
            return False

        if self.is_app_in_foreground(config):
            return True
        self.ad.log.error('AppController: Fail to launch app %s, is not in foreground', config.target_app_pkg)
        return False

    def is_app_in_foreground(self, config: AppConfig) -> bool:
        """
        Check if app is in foreground, will not return errors.
        1. ADB command: adb shell dumpsys activity activities
        2. Catch log of config.target_app_pkg
        """
        self.ad.log.info('AppController: Checking if %s in foreground...', config.target_app_pkg)

        try:
            log_output = self.ad.adb.shell(['dumpsys', 'activity', 'activities'])
        
        except Exception as e:
            error_msg = str(e).lower()
            if 'offline' in error_msg or 'not found' in error_msg or 'disconnected' in error_msg:
                self.ad.log.error('AppController: device disconnection, fail to check if %s launching...', config.target_app_pkg)
                raise RuntimeError(f"ADB connection error: {e}")
            
            self.ad.log.error('AppController: adb dumpsys command failed. Error: %s', e)
            return False

        msg = log_output.decode('utf-8') if isinstance(log_output, bytes) else str(log_output)
        """ 
        Using .splitlines to capture both 'mResumedActivity' and config.target_app_pkg is in log or not 
        """
        for line in msg.splitlines():
            if 'mResumedActivity' in line and config.target_app_pkg in line:
                self.ad.log.info('AppController: %s is currently in foreground.', config.target_app_pkg)
                return True

        self.ad.log.error('AppController: %s is NOT in foreground.', config.target_app_pkg)
        return False

    def get_app_version(self, config: AppConfig) -> str | None:
        """
        1. ADB command: adb shell dumpsys package {package_name}, capturing "versionName=1.2.0"
        2. error handing by using try-except, call func is installed to do double check
        3. finally, check the version number in log
        """
        self.ad.log.info('AppController: Executing %s version checking process ...', config.target_app_pkg)
        if not self.is_installed(config):
            self.ad.log.error('AppController: %s is not installed, please check again.', config.target_app_pkg)
            return None

        try:
            log_output = self.ad.adb.shell(['dumpsys', 'package', config.target_app_pkg])
            
        except Exception as e:
            error_msg = str(e).lower()
            if 'offline' in error_msg or 'not found' in error_msg or 'disconnected' in error_msg:
                self.ad.log.error('AppController: device disconnection, fail to get %s version...', config.target_app_pkg)
                raise RuntimeError(f"ADB connection error: {e}")
            
            self.ad.log.error('AppController: adb dumpsys command failed. Error: %s', e)
            return None

        msg = log_output.decode('utf-8') if isinstance(log_output, bytes) else str(log_output)
        for line in msg.splitlines():
            if 'versionName=' in line:
                version = line.split('=')[1].strip()
                return version

        self.ad.log.error('AppController: Cannot get %s version, please try again', config.target_app_pkg)
        return None