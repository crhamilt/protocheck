# protocheck
Imaging Collective protocol checker

This program reads a CSV file containing a list of DICOM elements, with expected values and ranges, and compares those values to the values in the header of a DICOM image.  The CSV file should be created as a copy of "template.CSV" and then edited as desired.  Lines can be removed for elements that you are not interested in checking. Lines can be added by looking in _dicom_dict.py to determine the proper spelling of elements.  This dictionary was copied from pydicom, which is used to read the DICOM file.

Usage:

  > python protocheck specfile.csv 000001.DCM
  
Output:

                             Element    Value Expected      Max      Min       Status
         --------------------------- -------- -------- -------- -------- ------------
                                Rows   288.00   128.00    64.00   320.00           OK
                           FlipAngle    15.00    15.00    10.00    20.00           OK
                      SliceThickness     4.00     5.00     3.00     8.00           OK
                      PixelBandwidth   130.00   120.00   100.00   150.00           OK
                    NumberOfAverages     2.00     2.00     2.00     2.00           OK
                       PixelSpacingY     0.73     0.73     0.60     1.00           OK
                      RepetitionTime    26.96   100.00    95.00   110.00   OutOfRange
                            EchoTime     8.32     8.00     6.00    10.00           OK
                       PixelSpacingX     0.73     0.73     0.60     1.00           OK
       InPlanePhaseEncodingDirection      COL      COL      COL      COL           OK
