# stdlib
import pathlib
import sys

# 3rd party
import numpy  # type: ignore
import pytest
from domdf_python_tools.testing import check_file_output
from pyms.GCMS.Class import GCMS_data  # type: ignore  # TODO
from pytest_regressions.data_regression import DataRegressionFixture
from pytest_regressions.file_regression import FileRegressionFixture

# this package
from pyms_agilent.metadata import is_datafile
from pyms_agilent.reader import agilent_reader

pytestmark = pytest.mark.skipif(condition=sys.platform != "win32", reason="Only supported on Windows.")


@pytest.fixture(scope="session")
def datafile():
	file = pathlib.Path(__file__).parent / "example1.d"
	assert file.is_dir()
	assert is_datafile(file)

	return file


@pytest.fixture(scope="module")
def data(datafile) -> GCMS_data:
	return agilent_reader(datafile)


def test_len(data):
	assert len(data) == 1333


def test_info(data, capsys):
	data.info()

	assert capsys.readouterr().out.splitlines() == [
			" Data retention time range: 0.047 min -- 14.998 min",
			" Time step: 0.673 s (std=0.001 s)",
			" Number of scans: 1333",
			" Minimum m/z measured: 40.001",
			" Maximum m/z measured: 999.194",
			" Mean number of m/z values per scan: 5771",
			" Median number of m/z values per scan: 6000",
			]


@pytest.mark.parametrize("scan_no", [1, 3, 5, 7, 9, 18, 27, 36, 45, 90, 180, 360])
def test_scan_list(data, data_regression: DataRegressionFixture, scan_no):
	# Workaround for https://github.com/ESSS/pytest-regressions/issues/26
	scan = data.scan_list[scan_no]
	data_regression.check({
			"intensity_list": list(map(float, scan.intensity_list)),
			"mass_list": list(map(float, scan.mass_list)),
			})


def test_time_list(data, data_regression: DataRegressionFixture):
	data_regression.check(data.time_list)


def test_tic(data, data_regression: DataRegressionFixture):
	data_regression.check(data.tic.intensity_array.tolist())


def test_min_rt(data):
	assert data.min_rt == 2.8329999999999997


def test_max_rt(data):
	assert data.max_rt == 899.859


def test_time_step(data):
	assert data.time_step == 0.6734429429429429


def test_time_step_std(data):
	assert numpy.isclose(data.time_step_std, 0.0005459174077273709)


@pytest.mark.parametrize("filename", [
		"agilent_data.I.csv",
		"agilent_data.mz.csv",
		])
def test_write(tmp_pathplus, data, file_regression: FileRegressionFixture, filename):
	data.write(tmp_pathplus / "agilent_data")
	assert (tmp_pathplus / filename).is_file()

	check_file_output(tmp_pathplus / filename, file_regression)


def test_write_intensities_stream(tmp_pathplus, data, file_regression: FileRegressionFixture):
	data.write_intensities_stream(tmp_pathplus / "agilent_data.dat")
	assert (tmp_pathplus / "agilent_data.dat").is_file()

	check_file_output(tmp_pathplus / "agilent_data.dat", file_regression)
