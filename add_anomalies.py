#!/usr/bin/env python
import sys
import numpy
import netCDF4 as nc


def add_anomaly_var(filepath, src_var='goddard_merged_seaice_conc_monthly'):
    dst = nc.Dataset(filepath, 'a')
    try:
        dst.createVariable('sic_anomaly',
                           numpy.float32,
                           dimensions=(dst.variables[src_var].dimensions))
    except RuntimeError:
        raise ValueError('Cannot user variable name {}'.format('sic_anomaly'))


def main():
    infile = sys.argv[1]
    add_anomaly_var(infile)
    dst_anomalies = compute_anomalies(infile)
    with nc.Dataset(infile, 'a') as dst:
        dst.variables['sic_anomaly'][:] = dst_anomalies


if __name__ == "__main__":
    main()
