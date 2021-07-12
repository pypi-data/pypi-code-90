"""AS RF configuration."""
from copy import deepcopy as _dcopy

# NOTE: absolute imports are necessary here due to how
# CONFIG_TYPES in __init__.py is built.
from siriuspy.clientconfigdb.types.global_config import _pvs_as_rf


def get_dict():
    """Return configuration type dictionary."""
    module_name = __name__.split('.')[-1]
    _dict = {
        'config_type_name': module_name,
        'value': _dcopy(_template_dict),
        'check': False,
    }
    return _dict


# When using this type of configuration to set the machine,
# the list of PVs should be processed in the same order they are stored
# in the configuration. The second numeric parameter in the pair is the
# delay [s] the client should wait before setting the next PV.


_pvs_bo_rf = [
    ['BR-RF-DLLRF-01:LIMIT:REVSSA1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:REVSSA2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:REVSSA3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:REVSSA4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:REVCAV:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:VCAV:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:FWCAV:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:FWSSA1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:RFIN7:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:RFIN8:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:RFIN9:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:RFIN10:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:RFIN11:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:RFIN12:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:RFIN13:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:RFIN14:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:LIMIT:RFIN15:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:SWITCHES:S', 0, 0.0],
    ['BR-RF-DLLRF-01:TRIPINVERT:S', 0, 0.0],
    ['BR-RF-DLLRF-01:VACINVERT:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:REVSSA1:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:REVSSA2:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:REVSSA3:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:REVSSA4:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:REVCAV:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:MAN:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:PLC:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:LLRF1:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:LLRF2:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:LLRF3:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:PLG1:UP:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:PLG1:DN:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:PLG2:UP:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:PLG2:DN:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:VCAV:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:FWCAV:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:FWSSA1:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:RFIN7:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:RFIN8:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:RFIN9:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:RFIN10:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:RFIN11:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:RFIN12:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:RFIN13:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:RFIN14:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:RFIN15:S', 0, 0.0],
    ['BR-RF-DLLRF-01:ILK:BEAM:TRIP:S', 0, 0.0],
    ['BR-RF-DLLRF-01:mV:AMPREF:MIN:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:PHSREF:MIN:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLGAIN:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:SL:PILIMIT:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:SL:KI:S', 0, 0.0],
    ['BR-RF-DLLRF-01:SL:KP:S', 0, 0.0],
    ['BR-RF-DLLRF-01:FL:PILIMIT:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FL:KI:S', 0, 0.0],
    ['BR-RF-DLLRF-01:FL:KP:S', 0, 0.0],
    ['BR-RF-DLLRF-01:AL:KI:S', 0, 0.0],
    ['BR-RF-DLLRF-01:AL:KP:S', 0, 0.0],
    ['BR-RF-DLLRF-01:PL:KI:S', 0, 0.0],
    ['BR-RF-DLLRF-01:PL:KP:S', 0, 0.0],
    ['BR-RF-DLLRF-01:MODE:S', 0, 0.0],
    ['BR-RF-DLLRF-01:PHSCORR:S', 0, 0.0],
    ['BR-RF-DLLRF-01:QUAD:SEL:S', 0, 0.0],
    ['BR-RF-DLLRF-01:AMPREF:INCRATE:S', 0, 0.0],
    ['BR-RF-DLLRF-01:PHSREF:INCRATE:S', 0, 0.0],
    ['BR-RF-DLLRF-01:FWMIN:AMPPHS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:PHSH:CAV:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:PHSH:FWDCAV:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:GAIN:FWDCAV:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:PHSH:FWDSSA1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:GAIN:FWDSSA1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:PHSH:ADC:S', 0, 0.0],
    ['BR-RF-DLLRF-01:PHSH:DAC:S', 0, 0.0],
    ['BR-RF-DLLRF-01:RmpTs1-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:RmpTs2-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:RmpTs3-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:RmpTs4-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:RmpIncTs-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:RmpPhsTop-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:RmpPhsBot-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:MARGIN:HI:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:MARGIN:LO:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:FWMIN:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:DTune-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:DELAY:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:POS:S', 0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:FILT:S', 0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:TOPRAMP:S', 0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:TRIG:S', 0, 0.0],
    ['BR-RF-DLLRF-01:mV:AL:REF:S.DRVH', 0.0, 0.0],
    ['BR-RF-DLLRF-01:mV:AL:REF:S.DRVL', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLGAIN:S.DRVH', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLGAIN:S.DRVL', 0.0, 0.0],
    ['BR-RF-DLLRF-01:SL:KP:S.DRVH', 0, 0.0],
    ['BR-RF-DLLRF-01:SL:KP:S.DRVL', 0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCAV:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:MO:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVSSA1:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL2:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL4:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL1:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL5:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:INPRE:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDPRE:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVPRE:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCIRC:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCIRC:Const:OFS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:U-Raw:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:U-Raw:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:U-Raw:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:U-Raw:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CAV:Const:U-Raw:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCAV:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCAV:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCAV:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCAV:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCAV:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:MO:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:MO:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:MO:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:MO:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:MO:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL2:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL2:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL2:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL2:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL2:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL4:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL4:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL4:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL4:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL4:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL1:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL1:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL1:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL1:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL1:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL5:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL5:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL5:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL5:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:CELL5:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:INPRE:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:INPRE:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:INPRE:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:INPRE:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:INPRE:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDPRE:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDPRE:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDPRE:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDPRE:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDPRE:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVPRE:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVPRE:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVPRE:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVPRE:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVPRE:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCIRC:Const:Raw-U:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCIRC:Const:Raw-U:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCIRC:Const:Raw-U:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCIRC:Const:Raw-U:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:REVCIRC:Const:Raw-U:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:CAV:Const:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:CAV:Const:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:CAV:Const:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:CAV:Const:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:CAV:Const:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDCAV:Const:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDCAV:Const:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDCAV:Const:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDCAV:Const:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDCAV:Const:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDSSA1:Const:C4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDSSA1:Const:C3:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDSSA1:Const:C2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDSSA1:Const:C1:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:OLG:FWDSSA1:Const:C0:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FF:POS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FF:DEADBAND:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FF:GAIN:CELL2:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FF:GAIN:CELL4:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FDL:RAW:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FL:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:AL:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:PL:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:SL:SEL:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FL:SEL:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:AL:SEL:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:PL:SEL:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:PULSE:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:AUTOCOND:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:freq:cond:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:freq:duty:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:TUNE:PULSE:FREQ:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FF:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:RmpEnbl-Sel', 0.0, 0.0],
    ['BR-RF-DLLRF-01:mV:RAMP:AMP:BOT-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:mV:RAMP:AMP:TOP-SP', 0.0, 0.0],
    ['BR-RF-DLLRF-01:DisableRampDown:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:EPS:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:FIM:S', 0.0, 0.0],
    ['BR-RF-DLLRF-01:mV:RAMP:AMP:TOP-SP.DRVH', 0.0, 0.0],
    ['BR-RF-DLLRF-01:mV:RAMP:AMP:TOP-SP.DRVL', 0.0, 0.0],
    ['BR-RF-DLLRF-01:mV:RAMP:AMP:BOT-SP.DRVH', 0.0, 0.0],
    ['BR-RF-DLLRF-01:mV:RAMP:AMP:BOT-SP.DRVL', 0.0, 0.0],
    ]


_pvs_si_rf = [
    ['SR-RF-DLLRF-01:LIMIT:REVSSA1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:REVSSA2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:REVSSA3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:REVSSA4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:REVCAV:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:VCAV:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:FWCAV:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:FWSSA1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:RFIN7:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:RFIN8:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:RFIN9:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:RFIN10:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:RFIN11:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:RFIN12:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:RFIN13:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:RFIN14:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:LIMIT:RFIN15:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:SWITCHES:S', 0, 0.0],
    ['SR-RF-DLLRF-01:TRIPINVERT:S', 0, 0.0],
    ['SR-RF-DLLRF-01:VACINVERT:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:REVSSA1:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:REVSSA2:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:REVSSA3:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:REVSSA4:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:REVCAV:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:MAN:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:PLC:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:LLRF1:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:LLRF2:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:LLRF3:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:PLG1:UP:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:PLG1:DN:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:PLG2:UP:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:PLG2:DN:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:VCAV:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:FWCAV:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:FWSSA1:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:RFIN7:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:RFIN8:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:RFIN9:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:RFIN10:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:RFIN11:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:RFIN12:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:RFIN13:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:RFIN14:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:RFIN15:S', 0, 0.0],
    ['SR-RF-DLLRF-01:ILK:BEAM:TRIP:S', 0, 0.0],
    ['SR-RF-DLLRF-01:mV:AMPREF:MIN:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:mV:AL:REF:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PL:REF:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PHSREF:MIN:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLGAIN:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:SL:PILIMIT:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:SL:KI:S', 0, 0.0],
    ['SR-RF-DLLRF-01:SL:KP:S', 0, 0.0],
    ['SR-RF-DLLRF-01:FL:PILIMIT:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FL:KI:S', 0, 0.0],
    ['SR-RF-DLLRF-01:FL:KP:S', 0, 0.0],
    ['SR-RF-DLLRF-01:AL:KI:S', 0, 0.0],
    ['SR-RF-DLLRF-01:AL:KP:S', 0, 0.0],
    ['SR-RF-DLLRF-01:PL:KI:S', 0, 0.0],
    ['SR-RF-DLLRF-01:PL:KP:S', 0, 0.0],
    ['SR-RF-DLLRF-01:MODE:S', 0, 0.0],
    ['SR-RF-DLLRF-01:PHSCORR:S', 0, 0.0],
    ['SR-RF-DLLRF-01:QUAD:SEL:S', 0, 0.0],
    ['SR-RF-DLLRF-01:AMPREF:INCRATE:S', 0, 0.0],
    ['SR-RF-DLLRF-01:PHSREF:INCRATE:S', 0, 0.0],
    ['SR-RF-DLLRF-01:FWMIN:AMPPHS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PHSH:CAV:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PHSH:FWDCAV:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:GAIN:FWDCAV:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PHSH:FWDSSA1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:GAIN:FWDSSA1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PHSH:ADC:S', 0, 0.0],
    ['SR-RF-DLLRF-01:RmpTs1-SP', 0.0, 0.0],
    ['SR-RF-DLLRF-01:RmpTs2-SP', 0.0, 0.0],
    ['SR-RF-DLLRF-01:RmpTs3-SP', 0.0, 0.0],
    ['SR-RF-DLLRF-01:RmpTs4-SP', 0.0, 0.0],
    ['SR-RF-DLLRF-01:RmpIncTs-SP', 0.0, 0.0],
    ['SR-RF-DLLRF-01:RmpPhsTop-SP', 0.0, 0.0],
    ['SR-RF-DLLRF-01:RmpPhsBot-SP', 0.0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:MARGIN:HI:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:MARGIN:LO:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:FWMIN:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:DTune-SP', 0.0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:DELAY:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:POS:S', 0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:FILT:S', 0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:TOPRAMP:S', 0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:TRIG:S', 0, 0.0],
    ['SR-RF-DLLRF-01:mV:AL:REF:S.DRVH', 0.0, 0.0],
    ['SR-RF-DLLRF-01:mV:AL:REF:S.DRVL', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLGAIN:S.DRVH', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLGAIN:S.DRVL', 0.0, 0.0],
    ['SR-RF-DLLRF-01:SL:KP:S.DRVH', 0, 0.0],
    ['SR-RF-DLLRF-01:SL:KP:S.DRVL', 0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVCAV:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:MO:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA2:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA1:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA2:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL2:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL6:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE1:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE2:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE1:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE2:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCIRC:Const:OFS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:U-Raw:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:U-Raw:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:U-Raw:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:U-Raw:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CAV:Const:U-Raw:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCAV:Const:U-Raw:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA1:Const:U-Raw:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA1:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA2:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA2:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA2:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA2:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVSSA2:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVCAV:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVCAV:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVCAV:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVCAV:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:REVCAV:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA2:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA2:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA2:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA2:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDSSA2:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:MO:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:MO:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:MO:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:MO:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:MO:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL2:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL2:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL2:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL2:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL2:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL6:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL6:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL6:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL6:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:CELL6:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE1:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE1:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE1:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE1:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE1:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE2:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE2:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE2:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE2:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:INPRE2:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE1:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE1:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE1:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE1:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE1:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE2:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE2:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE2:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE2:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDPRE2:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FWDCIRC:Const:Raw-U:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:CAV:Const:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:CAV:Const:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:CAV:Const:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:CAV:Const:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:CAV:Const:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDCAV:Const:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDCAV:Const:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDCAV:Const:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDCAV:Const:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDCAV:Const:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDSSA1:Const:C4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDSSA1:Const:C3:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDSSA1:Const:C2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDSSA1:Const:C1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:OLG:FWDSSA1:Const:C0:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PHSH:SSA1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PHSH:SSA2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:GAIN:SSA1:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:GAIN:SSA2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FF:POS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FF:DEADBAND:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FF:GAIN:CELL2:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FF:GAIN:CELL4:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FDL:RAW:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FL:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:AL:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PL:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:SL:SEL:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FL:SEL:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:AL:SEL:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PL:SEL:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:PULSE:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:AUTOCOND:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:COND:DC:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:TUNE:PULSE:FREQ:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FF:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:RmpEnbl-Sel', 0.0, 0.0],
    ['SR-RF-DLLRF-01:DisableRampDown:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:EPS:S', 0.0, 0.0],
    ['SR-RF-DLLRF-01:FIM:S', 0.0, 0.0],
    ]


_template_dict = {
    'pvs':
    _pvs_as_rf + _pvs_bo_rf + _pvs_si_rf
    }
