# -*- coding: utf-8 -*-
# Copyright (c) 2004-2014 Alterra, Wageningen-UR
# Allard de Wit (allard.dewit@wur.nl), April 2014
"""PCSE configuration file for testing lintul3.

This configuration file defines the crop.
"""

from pcse.lintul.lintul3 import Lintul3
from pcse.lintul.lintul3soil import Lintul3Soil
from pcse.agromanagement import AgroManagementSingleCrop

# Module to be used for water balance
SOIL = Lintul3Soil

# Module to be used for the crop simulation itself
CROP = Lintul3

# Module to use for AgroManagement actions
AGROMANAGEMENT = AgroManagementSingleCrop

# variables to save at OUTPUT signals
# Set to an empty list if you do not want any OUTPUT
OUTPUT_VARS = ["CUMPAR", "DVS", "TGROWTH", "LAI", "NUPTT", "PEVAP", "TDRAIN", "TEVAP",
               "TEXPLO", "TIRRIG", "TNSOIL", "TRAIN", "TRANRF", "TRUNOF", "TSUM",
               "TTRAN", "WA", "WLVD", "WLVG", "WRT", "WSO", "WST"]

# interval for OUTPUT signals, either "daily"|"dekadal"|"monthly"                                    
# For daily output you change the number of days between successive
# outputs using OUTPUT_INTERVAL_DAYS. For dekadal and monthly
# output this is ignored.
OUTPUT_INTERVAL = "daily"
OUTPUT_INTERVAL_DAYS = 1
OUTPUT_WEEKDAY = 0

# variables to save at SUMMARY_OUTPUT signals
# Set to an empty list if you do not want any SUMMARY_OUTPUT
SUMMARY_OUTPUT_VARS = []