#  !/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#  agilent.py
"""
The lowest level interface to the Agilent MHDAC library.
"""
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import sys
import platform
import pathlib

import clr  # type: ignore

__all__ = ["DataAnalysis"]


if platform.architecture()[0] == "64bit":
	sys.path.append(str(pathlib.Path(__file__).parent / "x64"))
else:
	sys.path.append(str(pathlib.Path(__file__).parent / "x86"))

clr.AddReference("MassSpecDataReader")
clr.AddReference("BaseCommon")
clr.AddReference("BaseDataAccess")

import Agilent.MassSpectrometry.DataAnalysis

DataAnalysis = Agilent.MassSpectrometry.DataAnalysis