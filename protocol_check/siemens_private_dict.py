# _private_dict.py
# This file is autogenerated by "make_private_dict_alt.py",
# from private elements list maintained by the GDCM project
# (http://gdcm.svn.sf.net/viewvc/gdcm/trunk/Source/DataDictionary/privatedicts.xml).
# Downloaded on 2010-01-22.
# See the license.txt file for license information on pydicom, and GDCM.

# This is a dictionary of DICOM dictionaries.
# The outer dictionary key is the Private Creator name ("owner"),
# the inner dictionary is a map of DICOM tag to
# (VR, type, name, is_retired)

# CAHMOD:  took everything out except Siemens MR


private_dictionaries = \
{
 'SIEMENS CSA HEADER': {'0029xx08': ('CS', '1', 'CSA Image Header Type', ''),
                        '0029xx09': ('LO',
                                     '1',
                                     'CSA Image Header Version',
                                     ''),
                        '0029xx10': ('OB', '1', 'CSA Image Header Info', ''),
                        '0029xx18': ('CS', '1', 'CSA Series Header Type', ''),
                        '0029xx19': ('LO',
                                     '1',
                                     'CSA Series Header Version',
                                     ''),
                        '0029xx20': ('OB', '1', 'CSA Series Header Info', '')},
 'SIEMENS MEDCOM HEADER': {'0029xx08': ('CS', '1', 'MedCom Header Type', ''),
                           '0029xx09': ('LO',
                                        '1',
                                        'MedCom Header Version',
                                        ''),
                           '0029xx10': ('OB', '1', 'MedCom Header Info', ''),
                           '0029xx20': ('OB',
                                        '1',
                                        'MedCom History Information',
                                        ''),
                           '0029xx31': ('LO', '1', 'PMTF Information 1', ''),
                           '0029xx32': ('UL', '1', 'PMTF Information 2', ''),
                           '0029xx33': ('UL', '1', 'PMTF Information 3', ''),
                           '0029xx34': ('CS', '1', 'PMTF Information 4', ''),
                           '0029xx35': ('UL', '1', 'PMTF Information 5', ''),
                           '0029xx40': ('SQ',
                                        '1',
                                        'Application Header Sequence',
                                        ''),
                           '0029xx41': ('CS',
                                        '1',
                                        'Application Header Type',
                                        ''),
                           '0029xx42': ('LO',
                                        '1',
                                        'Application Header ID',
                                        ''),
                           '0029xx43': ('LO',
                                        '1',
                                        'Application Header Version',
                                        ''),
                           '0029xx44': ('OB',
                                        '1',
                                        'Application Header Info',
                                        ''),
                           '0029xx50': ('LO',
                                        '8',
                                        'Workflow Control Flags',
                                        ''),
                           '0029xx51': ('CS',
                                        '1',
                                        'Arch. Management Flag Keep Online',
                                        ''),
                           '0029xx52': ('CS',
                                        '1',
                                        'Arch. Mgmnt Flag Do Not Archive',
                                        ''),
                           '0029xx53': ('CS',
                                        '1',
                                        'Image Location Status',
                                        ''),
                           '0029xx54': ('DS',
                                        '1',
                                        'Estimated Retrieve Time',
                                        ''),
                           '0029xx55': ('DS',
                                        '1',
                                        'Data Size of Retrieved Images',
                                        ''),
                           '0029xx70': ('SQ',
                                        '1',
                                        'Siemens Link Sequence',
                                        ''),
                           '0029xx71': ('AT', '1', 'Referenced Tag', ''),
                           '0029xx72': ('CS', '1', 'Referenced Tag Type', ''),
                           '0029xx73': ('UL',
                                        '1',
                                        'Referenced Value Length',
                                        ''),
                           '0029xx74': ('CS',
                                        '1',
                                        'Referenced Object Device Type',
                                        ''),
                           '0029xx75': ('OB',
                                        '1',
                                        'Referenced Object Device Location',
                                        ''),
                           '0029xx76': ('OB',
                                        '1',
                                        'Referenced Object ID',
                                        '')},
 'SIEMENS MEDCOM HEADER2': {'0029xx60': ('LO',
                                         '1',
                                         'Series Workflow Status',
                                         '')},
 'SIEMENS MR HEADER': {'0019xx08': ('CS', '1', 'CSA Image Header Type', ''),
                       '0019xx09': ('LO',
                                    '1',
                                    'CSA Image Header Version ??',
                                    ''),
                       '0019xx0a': ('US', '1', 'NumberOfImagesInMosaic', ''),
                       '0019xx0b': ('DS',
                                    '1',
                                    'SliceMeasurementDuration',
                                    ''),
                       '0019xx0c': ('IS', '1', 'B_value', ''),
                       '0019xx0d': ('CS', '1', 'DiffusionDirectionality', ''),
                       '0019xx0e': ('FD',
                                    '3',
                                    'DiffusionGradientDirection',
                                    ''),
                       '0019xx0f': ('SH', '1', 'GradientMode', ''),
                       '0019xx11': ('SH', '1', 'FlowCompensation', ''),
                       '0019xx12': ('SL', '3', 'TablePositionOrigin', ''),
                       '0019xx13': ('SL', '3', 'ImaAbsTablePosition', ''),
                       '0019xx14': ('IS', '3', 'ImaRelTablePosition', ''),
                       '0019xx15': ('FD', '3', 'SlicePosition_PCS', ''),
                       '0019xx16': ('DS', '1', 'TimeAfterStart', ''),
                       '0019xx17': ('DS', '1', 'SliceResolution', ''),
                       '0019xx18': ('IS', '1', 'RealDwellTime', ''),
                       '0019xx23': ('IS', '1', 'FMRIStimulInfo', ''),
                       '0019xx25': ('FD', '3', 'RBMoCoTrans', ''),
                       '0019xx26': ('FD', '3', 'RBMoCoRot', ''),
                       '0019xx27': ('FD', '6', 'B_matrix', ''),
                       '0019xx28': ('FD',
                                    '1',
                                    'BandwidthPerPixelPhaseEncode',
                                    ''),
                       '0019xx29': ('FD', '1', 'MosaicRefAcqTimes', ''),
                       '0051xx08': ('CS', '1', 'CSA Image Header Type', ''),
                       '0051xx09': ('LO',
                                    '1',
                                    'CSA Image Header Version ??',
                                    ''),
                       '0051xx0a': ('SH', '1', 'Unknown', ''),
                       '0051xx0b': ('SH', '1', 'AcquisitionMatrixText', ''),
                       '0051xx0c': ('SH', '1', 'Unknown', ''),
                       '0051xx0d': ('SH', '1', 'Unknown', ''),
                       '0051xx0e': ('SH', '1', 'Unknown', ''),
                       '0051xx0f': ('LO', '1', 'CoilString', ''),
                       '0051xx11': ('LO', '1', 'PATModeText', ''),
                       '0051xx12': ('SH', '1', 'Unknown', ''),
                       '0051xx13': ('SH', '1', 'PositivePCSDirections', ''),
                       '0051xx15': ('SH', '1', 'Unknown', ''),
                       '0051xx16': ('LO', '1', 'Unknown', ''),
                       '0051xx17': ('SH', '1', 'Unknown', ''),
                       '0051xx18': ('SH', '1', 'Unknown', ''),
                       '0051xx19': ('LO', '1', 'Unknown', '')}
 }