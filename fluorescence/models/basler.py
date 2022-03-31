from experimentor.models.devices.cameras.basler.basler import BaslerCamera as OriginalBasler


class BaslerCamera(OriginalBasler):
    def configure_DIO(self):
        """Configures the Digital input-output of the camera based on a simple configuration dictionary that should be
        stored on the config parameters of the camera.
        """
        self.logger.info(f"{self} - Configure Digital input output")
        DIO = self.initial_config['DIO']
        for settings in DIO:
            self.logger.debug(settings)
            self._driver.LineSelector.SetValue(DIO[settings]['line'])
            self._driver.LineMode.SetValue(DIO[settings]['mode'])
            self._driver.LineSource.SetValue(DIO[settings]['source'])
