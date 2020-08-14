# stdlib
import os
import pathlib

# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus

# this package
from pyms_agilent.metadata import extract_metadata, is_datafile, prepare_filepath
from pyms_agilent.xml_parser.acq_method import AcqMethod
from pyms_agilent.xml_parser.contents import Contents
from pyms_agilent.xml_parser.default_mass_cal import CalibrationList
from pyms_agilent.xml_parser.device_config_info import DeviceConfigInfo
from pyms_agilent.xml_parser.devices import DeviceList
from pyms_agilent.xml_parser.ms_actual_defs import ActualsDef
from pyms_agilent.xml_parser.ms_time_segments import MSTimeSegments
from pyms_agilent.xml_parser.sample_info import SampleInfo


def test_is_datafile(monkeypatch):
	monkeypatch.chdir(pathlib.Path(__file__).parent)

	assert is_datafile("Propellant_Std_1ug_1_200124-0002.d")
	assert is_datafile(pathlib.Path("Propellant_Std_1ug_1_200124-0002.d"))
	assert is_datafile(PathPlus("Propellant_Std_1ug_1_200124-0002.d"))
	assert not is_datafile(pathlib.Path(".").parent)

	with pytest.raises(TypeError):
		is_datafile(1234)  # type: ignore
	with pytest.raises(TypeError):
		is_datafile([1234])  # type: ignore
	with pytest.raises(TypeError):
		is_datafile(["a file"])  # type: ignore
	with pytest.raises(TypeError):
		is_datafile([pathlib.Path("a file")])  # type: ignore


def test_prepare_filepath(monkeypatch, tmpdir):
	monkeypatch.chdir(tmpdir)

	with pytest.raises(TypeError):
		prepare_filepath(1234)  # type: ignore
	with pytest.raises(TypeError):
		prepare_filepath([1234])  # type: ignore
	with pytest.raises(TypeError):
		prepare_filepath(["a file"])  # type: ignore
	with pytest.raises(TypeError):
		prepare_filepath([pathlib.Path("a file")])  # type: ignore

	test_file = "directory/file.extension"

	assert not os.path.isfile(test_file)
	assert prepare_filepath(test_file) == pathlib.Path(test_file)
	assert os.path.exists("directory")

	pathlib.Path(test_file).parent.rmdir()

	assert not os.path.isfile(test_file)
	assert prepare_filepath(pathlib.Path(test_file)) == pathlib.Path(test_file)
	assert os.path.exists("directory")

	pathlib.Path(test_file).parent.rmdir()

	assert not os.path.isfile(test_file)
	assert prepare_filepath(PathPlus(test_file)) == pathlib.Path(test_file)
	assert os.path.exists("directory")

	pathlib.Path(test_file).parent.rmdir()


def test_extract_metadata(monkeypatch):
	monkeypatch.chdir(pathlib.Path(__file__).parent)
	datafile = pathlib.Path("Propellant_Std_1ug_1_200124-0002.d")

	metadata = extract_metadata(datafile)

	assert isinstance(metadata["AcqMethod"], AcqMethod)
	assert isinstance(metadata["Contents"], Contents)
	assert isinstance(metadata["DefaultMassCal"], CalibrationList)
	assert isinstance(metadata["DeviceConfigInfo"], DeviceConfigInfo)
	assert isinstance(metadata["Devices"], DeviceList)
	assert isinstance(metadata["MSActualDefs"], ActualsDef)
	assert isinstance(metadata["MSTS"], MSTimeSegments)
	assert isinstance(metadata["sample_info"], SampleInfo)

	with pytest.raises(ValueError):
		extract_metadata(pathlib.Path(__file__).parent)
