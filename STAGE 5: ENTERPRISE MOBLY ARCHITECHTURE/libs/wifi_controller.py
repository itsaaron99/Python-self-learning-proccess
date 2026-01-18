"""
Encapsulation Wi-Fi related bottom actions (ADB / Snippet)
"""


from data_models.wifi_protos import WifiConfig

class WifiController:
    
    def __init__(self, ad_device):
        """ Connects to a Wi-Fi network using the provided configuration. """
        self.ad = ad_device

    def connect(self, config: WifiConfig):
        """
        Connects to the specified Wi-Fi network.

        Args:
            config: A WifiConfig data model containing SSID and password.
        """        
        self.ad.log.info('WifiController: Preparing to connect to %s...', config.ssid)
        self.ad.log.info('Note: Connection timeout is typically 2 minutes. Please wait if testing failure.')

        """ Use ADB to simulate/ensure Wi-Fi is enabled """
        self.ad.adb.shell('cmd wifi set-wifi-enabled enabled')

        """ Call Snippet to perform actual connection (if Snippet is loaded) """
        if hasattr(self.ad, 'mbs'):
            """ Handle password logic: empty string converts to None (Open Network) """
            pwd = config.password if config.password else None
            try:
                self.ad.mbs.wifiConnectSimple(config.ssid, pwd)
            except KeyboardInterrupt:
                self.ad.log.warning('Connection cancelled by user! (KeyboardInterrupt)')
                raise
            except Exception as e:
                self.ad.log.error('Connection Fail %s', e)
                raise e

        self.ad.log.info('WifiController: Successfully connected to SSID %s', config.ssid)