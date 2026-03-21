"""
Encapsulation App related bottom actions (ADB pm/am)
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
