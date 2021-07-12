"""Somfy Smoke Detector"""
from typing import cast

from somfy_protect_api.api.devices.base import SomfyProtectDevice


class SomfySmokeDetector(SomfyProtectDevice):
    """Class to represent a Somfy Smoke Detector."""

    def get_rlink_quality(self) -> float:
        """Link Quality in %

        Returns:
            float: Link Quality percentage
        """
        return cast(float, self.get_status("rlink_quality_percent"))

    def get_battery_level(self) -> float:
        """Battery Level

        Returns:
            float: Battery Level percentage
        """
        return cast(float, self.get_status("battery_level"))

    def is_battery_low(self) -> bool:
        """Battery Low Level

        Returns:
            float: Battery Low Level
        """
        return cast(bool, self.get_status("battery_low"))

    def smoke_detected(self) -> bool:
        """Somke Detected

        Returns:
            float: Smoke detection
        """
        return cast(bool, self.get_status("sp_smoke_detector_smoke_detection"))

    def smoke_detector_role(self) -> bool:
        """Somke Detector Role

        Returns:
            float: Smoke detector role
        """
        return cast(bool, self.get_status("sp_smoke_detector_role"))
