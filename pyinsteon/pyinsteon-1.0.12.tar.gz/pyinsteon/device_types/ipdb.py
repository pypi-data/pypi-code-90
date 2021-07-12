"""Embodies the INSTEON Product Database static data and access methods."""
import collections
import logging

from . import (PLM, ClimateControl_Thermostat, ClimateControl_WirelessThermostat, DimmableLightingControl,
               DimmableLightingControl_DinRail,
               DimmableLightingControl_FanLinc,
               DimmableLightingControl_InLineLinc,
               DimmableLightingControl_KeypadLinc_6,
               DimmableLightingControl_KeypadLinc_8,
               DimmableLightingControl_LampLinc,
               DimmableLightingControl_OutletLinc,
               DimmableLightingControl_SwitchLinc,
               DimmableLightingControl_ToggleLinc, GeneralController,
               GeneralController_ControlLinc, GeneralController_MiniRemote_4,
               GeneralController_MiniRemote_8,
               GeneralController_MiniRemote_Switch,
               GeneralController_RemoteLinc, Hub, SecurityHealthSafety,
               SecurityHealthSafety_DoorSensor,
               SecurityHealthSafety_LeakSensor,
               SecurityHealthSafety_MotionSensor,
               SecurityHealthSafety_OpenCloseSensor,
               SecurityHealthSafety_Smokebridge, SensorsActuators,
               SensorsActuators_IOLink, SwitchedLightingControl,
               SwitchedLightingControl_ApplianceLinc,
               SwitchedLightingControl_DinRail,
               SwitchedLightingControl_InLineLinc,
               SwitchedLightingControl_KeypadLinc_6,
               SwitchedLightingControl_KeypadLinc_8,
               SwitchedLightingControl_OnOffOutlet,
               SwitchedLightingControl_OutletLinc,
               SwitchedLightingControl_SwitchLinc,
               SwitchedLightingControl_ToggleLinc, UnknownDevice,
               WindowCovering, X10Dimmable, X10OnOff, X10OnOffSensor)

_LOGGER = logging.getLogger(__name__)


Product = collections.namedtuple("Product", "cat subcat product_key description model deviceclass")


X10Product = collections.namedtuple("X10Product", "feature deviceclass")

# flake8: noqa
class IPDB:
    """Embodies the INSTEON Product Database static data and access methods."""

    _products = [
        Product(None, None, None, "Unknown Device", "", UnknownDevice),
        Product(0x00, None, None, "Generic General Controller", "", GeneralController),
        Product(0x00, 0x04, None, "ControLinc", "2430", GeneralController_ControlLinc),
        Product(0x00, 0x05, 0x000034, "RemoteLinc", "2440", GeneralController_RemoteLinc),
        Product(0x00, 0x06, None, "ICON Tabletop Controller", "2830", GeneralController_ControlLinc,),
        Product(0x00, 0x08, None, "EZBridge/EZServer", "", GeneralController),
        Product(0x00, 0x09, None, "SignaLinc", "2442", GeneralController),
        Product(0x00, 0x0A, 0x000007, "Poolux LCD Controller", "", GeneralController),
        Product(0x00, 0x0B, 0x000022, "Range Extender", "2443", GeneralController),
        Product(0x00, 0x0C, 0x000028, "IES Color Touchscreen", "", GeneralController),
        Product(0x00, 0x10, None, "Mini Remote - 4 Scene", "2444A2WH4", GeneralController_MiniRemote_4,),
        Product(0x00, 0x11, None, "Mini Remote - Switch", "2444A3", GeneralController_MiniRemote_Switch,),
        Product(0x00, 0x12, None, "Mini Remote - 8 Scene", "2444A2WH8", GeneralController_MiniRemote_8,),
        Product(0x00, 0x14, None, "Mini Remote - 4 Scene", "2342-432", GeneralController_MiniRemote_4,),
        Product(0x00, 0x15, None, "Mini Remote - Switch", "2342-442", GeneralController_MiniRemote_Switch,),
        Product(0x00, 0x16, None, "Mini Remote - 8 Scene", "2342-422", GeneralController_MiniRemote_8,),
        Product(0x00, 0x17, None, "Mini Remote - 4 Scene", "2342-532", GeneralController_MiniRemote_4,),
        Product(0x00, 0x18, None, "Mini Remote - 8 Scene", "2342-522", GeneralController_MiniRemote_8,),
        Product(0x00, 0x19, None, "Mini Remote - Switch", "2342-542", GeneralController_MiniRemote_Switch,),
        Product(0x00, 0x1A, None, "Mini Remote - 8 Scene", "2342-222", GeneralController_MiniRemote_8,),
        Product(0x00, 0x1B, None, "Mini Remote - 4 Scene", "2342-232", GeneralController_MiniRemote_4,),
        Product(0x00, 0x1C, None, "Mini Remote - Switch", "2342-242", GeneralController_MiniRemote_Switch,),
        Product(0x00, 0x1D, 0x000022, "Range Extender", "2992-222", GeneralController),
        Product(0x01, None, None, "Generic Dimmable Lighting Control", "", DimmableLightingControl,),
        Product(0x01, 0x00, None, "LampLinc Dimmer", "2456D3", DimmableLightingControl_LampLinc,),
        Product(0x01, 0x01, None, "SwitchLinc Dimmer", "2476D", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x02, None, "In-LineLinc Dimmer", "2475D", DimmableLightingControl_InLineLinc,),
        Product(0x01, 0x03, None, "ICON Dimmer Switch", "2876D", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x04, None, "SwitchLinc Dimmer", "2476DH", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x05, 0x000041, "Keypad Countdown Timer", "2484DWH8", DimmableLightingControl,),
        Product(0x01, 0x06, None, "LampLinc", "2456D2", DimmableLightingControl_LampLinc),
        Product(0x01, 0x07, None, "ICON LampLinc", "2856D2", DimmableLightingControl_LampLinc,),
        Product(0x01, 0x07, None, "ICON LampLinc", "2856D2B", DimmableLightingControl_LampLinc,),
        Product(0x01, 0x09, 0x000037, "KeypadLinc Dimmer", "2486DWH6", DimmableLightingControl_KeypadLinc_6,),
        Product(0x01, 0x0A, None, "ICON In-Wall Controller", "", DimmableLightingControl_InLineLinc,),
        Product(0x01, 0x0B, None, "Dimmer Module", "2632-422", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x0C, 0x00001D, "KeypadLinc Dimmer", "2486DWH8", DimmableLightingControl_KeypadLinc_8,),
        Product(0x01, 0x0D, None, "SocketLinc", "2454D", DimmableLightingControl_LampLinc),
        Product(0x01, 0x0E, None, "LampLinc Dimmer", "2457D2", DimmableLightingControl_LampLinc,),
        Product(0x01, 0x0F, None, "Dimmer Module", "2632-432", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x11, None, "Dimmer Module", "2632-442", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x12, None, "Dimmer Module", "2632-522", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x13, 0x000032, "SwitchLinc Dimmer (Lixar)", "2676D-B", DimmableLightingControl,),
        Product(0x01, 0x17, None, "ToggleLinc Dimmer", "2466DW", DimmableLightingControl_ToggleLinc,),
        Product(0x01, 0x18, None, "ICON SwitchLinc Dimmer In-line Companion", "2474D", DimmableLightingControl_InLineLinc,),
        Product(0x01, 0x19, None, "SwitchLinc Dimmer", "2476D", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x1A, None, "In-LineLinc Dimmer", "2475D", DimmableLightingControl_InLineLinc,),
        Product(0x01, 0x1B, None, "KeypadLinc Dimmer", "2486DWH6", DimmableLightingControl_KeypadLinc_6,),
        Product(0x01, 0x1B, 0x00001D, "KeypadLinc Dimmer", "2486DWH6", DimmableLightingControl_KeypadLinc_6,),
        Product(0x01, 0x1C, None, "KeypadLinc Dimmer", "2486DWH8", DimmableLightingControl_KeypadLinc_8,),
        Product(0x01, 0x1D, None, "SwitchLinc Dimmer", "2476DH", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x1E, None, "ICON Dimmer Switch", "2876D", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x1F, 0x0000000, "ToggleLinc Dimmer", "2466DW", DimmableLightingControl_ToggleLinc,),
        Product(0x01, 0x20, None, "SwitchLinc Dimmer", "2477D", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x20, 0x00006B, "SwitchLinc Dimmer", "2477D", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x21, None, "OutletLinc Dimmer", "2472DWH", DimmableLightingControl_OutletLinc,),
        Product(0x01, 0x22, None, "LampLinc Dimmer", "2457D2X", DimmableLightingControl_LampLinc,),
        Product(0x01, 0x23, None, "LampLinc EZ", "2457D2", DimmableLightingControl_LampLinc),
        Product(0x01, 0x24, None, "SwitchLinc 2-Wire Dimmer", "2474DWH", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x25, None, "INSTEON Ballast Dimmer", "2475DA2", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x27, 0x000087, "Wall Dimmer", "4701", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x29, 0x000089, "Wall Keypad Dimmer", "4703", DimmableLightingControl),  # KPL
        Product(0x01, 0x2A, 0x00008B, "Plug-in Dimmer", "4705", DimmableLightingControl_LampLinc,),
        Product(0x01, 0x2B, 0x000091, "Wall Dimmer - 1000W", "4711", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x2C, 0x000092, "In-Line Dimmer", "4712", DimmableLightingControl_InLineLinc,),
        Product(0x01, 0x2D, 0x00009E, "SwitchLinc Dimmer", "2477DH", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x2E, None, "FanLinc", "2475F", DimmableLightingControl_FanLinc),
        Product(0x01, 0x2F, None, "KeypadLinc Schedule Timer with Dimmer", "2484DST6", DimmableLightingControl,),  # KPL
        Product(0x01, 0x30, None, "SwitchLinc Dimmer", "2476D", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x31, None, "SwitchLinc Dimmer", "2478D", DimmableLightingControl_SwitchLinc,),
        Product(0x01, 0x32, None, "In-LineLinc Dimmer", "2475DA1", DimmableLightingControl_InLineLinc,),
        Product(0x01, 0x34, None, "DIN Rail Dimmer", "2252-222", DimmableLightingControl_DinRail,),
        Product(0x01, 0x35, None, "Micro Dimmer", "2442-222", DimmableLightingControl),
        Product(0x01, 0x36, None, "DIN Rail Dimmer", "2452-422", DimmableLightingControl_DinRail,),
        Product(0x01, 0x37, None, "DIN Rail Dimmer", "2452-522", DimmableLightingControl_DinRail,),
        Product(0x01, 0x38, None, "Micro Dimmer", "2442-422", DimmableLightingControl),
        Product(0x01, 0x39, None, "Micro Dimmer", "2442-522", DimmableLightingControl),
        Product(0x01, 0x3A, None, "LED Bulb", "2672-222", DimmableLightingControl),
        Product(0x01, 0x3B, None, "LED Bulb", "2672-422", DimmableLightingControl),
        Product(0x01, 0x3C, None, "LED Bulb", "2672-522", DimmableLightingControl),
        Product(0x01, 0x3D, None, "Ballast Dimmer", "2446-422", DimmableLightingControl_InLineLinc,),
        Product(0x01, 0x3E, None, "Ballast Dimmer", "2446-522", DimmableLightingControl_InLineLinc,),
        Product(0x01, 0x3F, None, "Fixture Dimmer", "2447-422", DimmableLightingControl_InLineLinc,),
        Product(0x01, 0x40, None, "Fixture Dimmer", "2447-522", DimmableLightingControl),
        Product(0x01, 0x41, None, "Keypad Dimmer", "2334-222", DimmableLightingControl_KeypadLinc_8,),
        Product(0x01, 0x42, None, "Keypad Dimmer", "2334-232", DimmableLightingControl_KeypadLinc_6,),
        Product(0x01, 0x42, None, "Keypad with Dimmer", "2334-232", DimmableLightingControl_KeypadLinc_6,),
        Product(0x01, 0x49, None, "LED PAR38 Bulb", "2674-222", DimmableLightingControl),
        Product(0x01, 0x4A, None, "LED PAR38 Bulb", "2674-422", DimmableLightingControl),
        Product(0x01, 0x4B, None, "LED PAR38 Bulb", "2672-522", DimmableLightingControl),
        Product(0x01, 0x4C, None, "LED Bulb", "2672-522", DimmableLightingControl),
        Product(0x01, 0x4D, None, "LED Bulb", "2672-522", DimmableLightingControl),
        Product(0x01, 0x4E, None, "LED PAR38 Bulb", "2674-422", DimmableLightingControl),
        Product(0x01, 0x4F, None, "LED PAR38 Bulb", "2672-522", DimmableLightingControl),
        Product(0x02, None, None, "Generic Switched Lighting Control", "", SwitchedLightingControl,),
        Product(0x02, 0x05, None, "KeypadLinc On/Off", "2486SWH8", SwitchedLightingControl_KeypadLinc_8,),
        Product(0x02, 0x06, None, "Outdoor ApplianceLinc", "2456S3E", SwitchedLightingControl_ApplianceLinc,),
        Product(0x02, 0x07, None, "TimerLinc", "2456S3T", SwitchedLightingControl),
        Product(0x02, 0x08, 0x000023, "OutletLinc Relay", "2473SWH", SwitchedLightingControl_OutletLinc,),
        Product(0x02, 0x09, None, "ApplianceLinc", "2456S3", SwitchedLightingControl_ApplianceLinc,),
        Product(0x02, 0x0A, None, "SwitchLinc Relay", "2476S", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x0B, None, "ICON On/Off Switch", "2876S", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x0C, None, "ICON Appliance Module", "2856S3B", SwitchedLightingControl_ApplianceLinc,),
        Product(0x02, 0x0D, None, "ToggleLinc On/Off", "2466SW", SwitchedLightingControl_ToggleLinc,),
        Product(0x02, 0x0E, None, "SwitchLinc Relay Countdown Timer", "2476ST", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x0F, 0x000036, "KeypadLinc On/Off", "2486SWH6", SwitchedLightingControl_KeypadLinc_6,),
        Product(0x02, 0x10, 0x00001B, "In-LineLinc Relay", "2475S", SwitchedLightingControl_InLineLinc,),
        Product(0x02, 0x11, None, "EZSwitch30", "", SwitchedLightingControl),
        Product(0x02, 0x12, 0x00003E, "ICON In-LineLinc Relay", "2474S", SwitchedLightingControl_InLineLinc,),
        Product(0x02, 0x13, None, "Icon SwitchLinc Relay (Lixar)", "2676R-B", SwitchedLightingControl,),
        Product(0x02, 0x14, None, "In-LineLinc Relay with Sense", "2475S2", SwitchedLightingControl_InLineLinc,),
        Product(0x02, 0x15, None, "SwitchLinc Relay with Sense", "2476S", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x16, None, "ICON On/Off Switch", "2876S", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x17, None, "ICON Appliance Module", "2856S3B", SwitchedLightingControl_ApplianceLinc,),
        Product(0x02, 0x18, 0x000060, "SwitchLinc 220V Relay", "2494S220", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x19, None, "SwitchLinc 220V Relay", "2494S220", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x1A, 0x0000000, "ToggleLinc On/Off", "2466SW", SwitchedLightingControl_ToggleLinc,),
        Product(0x02, 0x1C, None, "SwitchLinc Relay", "2476S", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x1E, None, "KeypadLinc On/Off", "2487S", SwitchedLightingControl_KeypadLinc_6,),  # KPL
        Product(0x02, 0x1F, None, "In-LineLinc On/Off", "2475SDB", SwitchedLightingControl_InLineLinc,),
        Product(0x02, 0x20, 0x00008A, "Wall Keypad Switch", "4704", SwitchedLightingControl),  # KPL
        Product(0x02, 0x21, 0x00008C, "Outlet Switch", "4707", SwitchedLightingControl_OutletLinc,),
        Product(0x02, 0x22, 0x000093, "In-Line Switch", "4713", SwitchedLightingControl_InLineLinc,),
        Product(0x02, 0x23, 0x000088, "Wall Switch", "4702", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x24, 0x0000A1, "Wall Keypad Switch 277V", "4102", SwitchedLightingControl,),  # KPL
        Product(0x02, 0x25, None, "Keypad Countdown Timer 8-button", "2484SWH8", SwitchedLightingControl,),
        Product(0x02, 0x26, None, "KeypadLinc Schedule Timer On/Off Switch", "2485SWH6", SwitchedLightingControl,),
        Product(0x02, 0x29, None, "SwitchLinc Relay Countdown Timer", "2476ST", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x2A, None, "SwitchLinc Relay (Dual-Band)", "2477S", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x2B, None, "In-LineLinc On/Off", "2475SDB-50", SwitchedLightingControl_InLineLinc,),
        Product(0x02, 0x2C, None, "KeypadLinc On/Off", "2487S", SwitchedLightingControl_KeypadLinc_6,),
        Product(0x02, 0x2D, None, "On/Off Module", "2633-422", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x2E, None, "DIN Rail On/Off", "2453-222", SwitchedLightingControl_DinRail,),
        Product(0x02, 0x2F, None, "Micro On/Off", "2443-222", SwitchedLightingControl),
        Product(0x02, 0x30, None, "On/Off Module", "2633-432", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x31, None, "Micro On/Off", "2443-422", SwitchedLightingControl),
        Product(0x02, 0x32, None, "Micro On/Off", "2443-522", SwitchedLightingControl),
        Product(0x02, 0x33, None, "DIN Rail On/Off", "2453-422", SwitchedLightingControl_DinRail,),
        Product(0x02, 0x34, None, "DIN Rail On/Off", "2453-522", SwitchedLightingControl_DinRail,),
        Product(0x02, 0x35, None, "On/Off Module", "2633-442", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x36, None, "On/Off Module", "2633-522", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x37, None, "On/Off Module", "2635-222", SwitchedLightingControl_SwitchLinc,),
        Product(0x02, 0x38, None, "On/Off Outdoor Module", "2634-222", SwitchedLightingControl_ApplianceLinc,),
        Product(0x02, 0x39, None, "On/Off Outlet", "2663-222", SwitchedLightingControl_OnOffOutlet,),
        Product(0x03, None, None, "Generic Network Bridge Controller", "", PLM),
        Product(0x03, 0x01, None, "PowerLinc Serial", "2414S", PLM),
        Product(0x03, 0x02, None, "PowerLinc USB", "2414U", PLM),
        Product(0x03, 0x03, None, "ICON PLC Serial", "", PLM),
        Product(0x03, 0x04, None, "ICON PLC USB", "", PLM),
        Product(0x03, 0x05, 0x00000C, "PowerLinc Serial Modem", "2412S", PLM),
        Product(0x03, 0x06, None, "IRLinc Receiver", "2411R", PLM),
        Product(0x03, 0x07, None, "IRLinc Transmitter", "2411T", PLM),
        Product(0x03, 0x0B, 0x000030, "PowerLinc USB Modem", "2412U", PLM),
        Product(0x03, 0x0D, 0x000035, "SimpleHomeNet EZX10RF", "", PLM),
        Product(0x03, 0x0F, 0x00003B, "EZX10IR", "", PLM),
        Product(0x03, 0x10, None, "SmartLinc", "2412N", PLM),
        Product(0x03, 0x11, None, "PowerLinc Serial Modem", "2413S", PLM),
        Product(0x03, 0x13, 0x000030, "PowerLinc USB Modem", "2412UH", PLM),
        Product(0x03, 0x14, 0x00000C, "PowerLinc Serial Modem", "2412SH", PLM),
        Product(0x03, 0x15, None, "PowerLinc USB Modem", "2413U", PLM),
        Product(0x03, 0x18, None, "Central Controller", "2243-222", PLM),
        Product(0x03, 0x19, None, "PowerLinc Serial Modem", "2413SH", PLM),
        Product(0x03, 0x1A, None, "PowerLinc USB Modem", "2413UH", PLM),
        Product(0x03, 0x1B, None, "iGateway", "2423A4", PLM),
        Product(0x03, 0x1F, 0x00007E, "USB Adapter", "2448A7", PLM),
        Product(0x03, 0x20, 0x00007E, "USB Adapter", "2448A7", PLM),
        Product(0x03, 0x21, 0x00008E, "USB Adapter", "2448A7H", PLM),
        Product(0x03, 0x22, 0x00008F, "Central Controller Interface", "4706A", PLM),
        Product(0x03, 0x23, 0x00008E, "USB Adapter", "2448A7H", PLM),
        Product(0x03, 0x24, 0x0000A2, "TouchLinc", "2448A7T", PLM),
        Product(0x03, 0x27, 0x0000A2, "TouchLinc", "2448A7T", PLM),
        Product(0x03, 0x2B, None, "Hub", "2242-222", Hub),
        Product(0x03, 0x2C, None, "Central Controller", "2243-422", Hub),
        Product(0x03, 0x2C, None, "Central Controller", "2243-442", Hub),
        Product(0x03, 0x2D, None, "Central Controller", "2243-522", Hub),
        Product(0x03, 0x2E, None, "Hub", "2242-422", Hub),
        Product(0x03, 0x2F, None, "Hub", "2242-522", Hub),
        Product(0x03, 0x30, None, "Hub", "2242-442", Hub),
        Product(0x03, 0x31, None, "Hub", "2242-232", Hub),
        Product(0x03, 0x32, None, "Hub", "2242-222", Hub),
        Product(0x03, 0x33, None, "Hub", "2245-555", Hub),
        Product(0x03, 0x34, None, "Hub", "2245-442", Hub),
        Product(0x03, 0x35, None, "Hub", "2245-422", Hub),
        Product(0x03, 0x36, None, "Hub", "2245-522", Hub),
        Product(0x03, 0x37, None, "Hub", "", Hub),
        Product(0x04, None, None, "Generic Irrigation Controler", "", UnknownDevice),
        Product(0x04, 0x00, 0x000001, "Compacta EZRain Sprinkler Controller", "31270", UnknownDevice,),
        Product(0x05, None, None, "Generic Climate Controller", "", UnknownDevice),
        Product(0x05, 0x00, None, "Broan SMSC080 Exhaust Fan", "", UnknownDevice),
        Product(0x05, 0x01, 0x000002, "EZTherm", "", UnknownDevice),
        Product(0x05, 0x02, None, "Broan SMSC110 Exhaust Fan", "", UnknownDevice),
        Product(0x05, 0x03, 0x00001F, "Thermostat Adapter", "2441V", ClimateControl_Thermostat),
        Product(0x05, 0x04, 0x000024, "EZTherm", "", UnknownDevice),
        Product(0x05, 0x05, 0x000038, "Broan, Venmar, BEST Rangehoods", "", UnknownDevice),
        Product(0x05, 0x07, None, 'Wireless Thermostat', '2441ZTH', ClimateControl_WirelessThermostat),
        Product(0x05, 0x08, None, 'Thermostat', '2441TH', ClimateControl_Thermostat),
        Product(0x05, 0x09, 0x000094, "7 Day Thermostat", "4715", UnknownDevice),
        Product(0x05, 0x0A, None, 'Wireless Thermostat', '2441ZTH', ClimateControl_WirelessThermostat),
        Product(0x05, 0x0B, None, 'Thermostat', '2441TH', ClimateControl_Thermostat),
        Product(0x05, 0x0E, None, "Integrated Remote Control Thermostat", "2491T1E", UnknownDevice,),
        Product(0x05, 0x0F, None, "Thermostat", "2732-422", ClimateControl_Thermostat),
        Product(0x05, 0x10, None, "Thermostat", "2732-522", ClimateControl_Thermostat),
        Product(0x05, 0x11, None, "Wireless Thermostat", "2732-432", ClimateControl_WirelessThermostat),
        Product(0x05, 0x12, None, "Wireless Thermostat", "2732-532", ClimateControl_WirelessThermostat),
        Product(0x05, 0x13, None, "Thermostat Heat Pump", "2732-232", ClimateControl_Thermostat),
        Product(0x05, 0x14, None, "Thermostat Heat Pump", "2732-432", ClimateControl_Thermostat),
        Product(0x05, 0x15, None, "Thermostat Heat Pump", "2732-532", ClimateControl_Thermostat),
        Product(0x05, 0x16, None, 'Insteon Thermostat', '2441TH', ClimateControl_Thermostat),
        Product(0x05, 0x17, None, "Insteon Thermostat", "2732-422", ClimateControl_Thermostat),
        Product(0x05, 0x18, None, "Insteon Thermostat", "2732-522", ClimateControl_Thermostat),
        Product(0x06, None, None, "Generic Pool Controller", "", UnknownDevice),
        Product(0x06, 0x00, 0x000003, "EZPool", "", UnknownDevice),
        Product(0x07, None, None, "Generic Sensor Actuator", "", SensorsActuators),
        Product(0x07, 0x00, None, "I/O Linc", "2450", SensorsActuators_IOLink),
        Product(0x07, 0x01, 0x000004, "EZSns1W", "", SensorsActuators),
        Product(0x07, 0x02, 0x0000012, "EZIO8T I/O Module", "", SensorsActuators),
        Product(0x07, 0x03, 0x0000005, "EZIO2X4", "", SensorsActuators),
        Product(0x07, 0x04, 0x0000013, "EZIO8SA", "", SensorsActuators),
        Product(0x07, 0x05, 0x0000014, "EZSnsRF", "", SensorsActuators),
        Product(0x07, 0x06, 0x0000015, "EZISnsRf", "", SensorsActuators),
        Product(0x07, 0x07, 0x0000014, "EZIO6I", "", SensorsActuators),
        Product(0x07, 0x08, 0x0000014, "EZIO4O", "", SensorsActuators),
        Product(0x07, 0x09, 0x0000000, "SynchroLinc", "2423A5", SensorsActuators),
        Product(0x07, 0x0D, None, "I/O Linc", "2450-50-60", SensorsActuators_IOLink),
        Product(0x07, 0x0E, None, "I/O Module", "2248-222", SensorsActuators),
        Product(0x07, 0x0F, None, "I/O Module", "2248-422", SensorsActuators),
        Product(0x07, 0x10, None, "I/O Module", "2248-442", SensorsActuators),
        Product(0x07, 0x11, None, "I/O Module", "2248-522", SensorsActuators),
        Product(0x09, None, None, "Generic Energy Management Controller", "", UnknownDevice),
        Product(0x09, 0x00, 0x0000006, "EZEnergy", "", UnknownDevice),
        Product(0x09, 0x01, 0x0000020, "OnSitePro Leak Detector", "", UnknownDevice),
        Product(0x09, 0x02, 0x0000021, "OnSitePro Control Valve", "", UnknownDevice),
        Product(0x09, 0x07, 0x0000000, "iMeter Solo", "2423A1", UnknownDevice),
        Product(0x09, 0x07, 0x000006C, "iMeter Solo", "2423A1", UnknownDevice),
        Product(0x09, 0x0A, 0x0000000, "220V/240V 30 AMP Load Controller Normally Open", "2477SA1", UnknownDevice,),
        Product(0x09, 0x0B, 0x0000000, "220V/240V 30 AMP Load Controller Normally Closed", "2477SA2", UnknownDevice,),
        Product(0x09, 0x0D, None, "Energy Display", "2441TH", UnknownDevice),
        Product(0x09, 0x10, 0x0000090, "Network Hub", "4700", UnknownDevice),
        Product(0x0E, None, None, "Generic Window Coverings", "", UnknownDevice),
        Product(0x0E, 0x00, 0x000000B, "Somfy Drape Controller RF Bridge", "", UnknownDevice),
        Product(0x0E, 0x01, 0x0000000, "Micro Open/Close", "2444-222", WindowCovering),
        Product(0x0E, 0x02, 0x0000000, "Micro Open/Close", "2444-422", WindowCovering),
        Product(0x0E, 0x03, 0x0000000, "Micro Open/Close", "2444-522", WindowCovering),
        Product(0x0F, None, None, "Generic Plumbing Controller", "", UnknownDevice),
        Product(0x0F, 0x00, 0x000000E, "Weiland Doors Central Drive and Controller", "", UnknownDevice,),
        Product(0x0F, 0x01, 0x000000F, "Weiland Doors Secondary Central Drive", "", UnknownDevice,),
        Product(0x0F, 0x02, 0x0000010, "Weiland Doors Assist Drive", "", UnknownDevice),
        Product(0x0F, 0x03, 0x0000011, "Weiland Doors Elevation Drive", "", UnknownDevice),
        Product(0x0F, 0x04, 0x0000000, "GarageHawk Garage Unit", "", UnknownDevice),
        Product(0x0F, 0x05, 0x0000000, "GarageHawk Remote Unit", "", UnknownDevice),
        Product(0x0F, 0x06, 0x0000000, "MorningLinc", "2458A1", UnknownDevice),
        Product(0x0F, 0x07, None, "Deadbolt", "2863-222", UnknownDevice),
        Product(0x0F, 0x08, None, "Deadbolt", "2863-422", UnknownDevice),
        Product(0x0F, 0x09, None, "Deadbolt", "2863-522", UnknownDevice),
        Product(0x0F, 0x0A, 0x0000000, "Lock Controller", "2862-222", UnknownDevice),
        Product(0x10, None, None, "Generic Security, Heath and Safety Device", "", SecurityHealthSafety,),
        Product(0x10, 0x01, None, "Motion Sensor", "2420M", SecurityHealthSafety_MotionSensor,),
        Product(0x10, 0x01, None, "Motion Sensor", "2842-222", SecurityHealthSafety_MotionSensor,),
        Product(0x10, 0x02, None, "Open/Close Sensor", "2843-222", SecurityHealthSafety_OpenCloseSensor,),
        Product(0x10, 0x03, None, "Motion Sensor", "4716", SecurityHealthSafety_MotionSensor),
        Product(0x10, 0x04, None, "Motion Sensor", "2842-422", SecurityHealthSafety_MotionSensor,),
        Product(0x10, 0x05, None, "Motion Sensor", "2842-522", SecurityHealthSafety_MotionSensor,),
        Product(0x10, 0x06, None, "Open/Close Sensor", "2843-422", SecurityHealthSafety_OpenCloseSensor,),
        Product(0x10, 0x07, None, "Open/Close Sensor", "2843-522", SecurityHealthSafety_OpenCloseSensor,),
        Product(0x10, 0x08, None, "Leak Sensor", "2852-222", SecurityHealthSafety_LeakSensor),
        Product(0x10, 0x09, None, "Door Sensor", "2843-232", SecurityHealthSafety_DoorSensor),
        Product(0x10, 0x0A, None, "Smoke Bridge", "2982-222", SecurityHealthSafety_Smokebridge,),
        Product(0x10, 0x11, None, "Door Sensor", "2845-222", SecurityHealthSafety_DoorSensor),
        Product(0x10, 0x14, None, "Door Sensor", "2845-422", SecurityHealthSafety_DoorSensor),
        Product(0x10, 0x15, None, "Door Sensor", "2845-522", SecurityHealthSafety_DoorSensor),
        Product(0x10, 0x16, None, "Motion Sensor II", "2844-222", SecurityHealthSafety_MotionSensor,),
        Product(0xFF, 0x00, None, "Unrecognized INSTEON Device", "", UnknownDevice),
        Product(0xFF, 0x01, None, "Unknown Device", "", UnknownDevice),
    ]

    _x10_products = [
        X10Product("on_off", X10OnOff),
        X10Product("dimmable", X10Dimmable),
        X10Product("sensor", X10OnOffSensor),
    ]

    def __len__(self):
        """Return the length of the product database."""
        return len(self._products) + len(self._x10_products)

    def __iter__(self):
        """Iterate through the product database."""
        for product in self._products:
            yield product

    def __getitem__(self, key):
        """Return an item from the product database."""
        cat, subcat = key

        device_product = None

        for product in self._products:
            if cat == product.cat and subcat == product.subcat:
                device_product = product

        # We failed to find a device in the database, so we will make a best
        # guess from the cat and return the generic class
        if not device_product:
            for product in self._products:
                if cat == product.cat and product.subcat is None:
                    return product

        # We did not find the device or even a generic device of that category
        if not device_product:
            device_product = Product(cat, subcat, None, "", "", UnknownDevice)

        return device_product

    def x10(self, feature):
        """Return an X10 device based on a feature.

        Current features:
        - on_off
        - dimmable
        - sensor
        """
        x10_product = None
        for product in self._x10_products:
            if feature.lower() == product.feature:
                x10_product = product

        if not x10_product:
            x10_product = X10Product(feature, None)

        return x10_product
