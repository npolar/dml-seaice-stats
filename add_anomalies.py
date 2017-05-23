#!/usr/bin/env python
import sys
import numpy
import netCDF4 as nc


def add_anomaly_var(dst):
    dst.CreateVariable('sic_anomaly',
                       numpy.float32,
                       dimensions=(dst.variables['seaice_conc_cdr'].dimensions))


def main():
    infile = sys.argv[1]
    ncfile = nc.Dataset(infile, 'a')
    add_anomaly_var(ncfile)
