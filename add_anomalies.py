#!/usr/bin/env python
import sys
import numpy
import netCDF4 as nc


def add_anomaly_var(filepath, src_var='goddard_merged_seaice_conc_monthly'):
    dst = nc.Dataset(filepath, 'a')
    if 'sic_anomaly' in dst.variables.keys():
        pass
    else:
        try:
            dst.createVariable('sic_anomaly',
                           numpy.float32,
                           dimensions=(dst.variables[src_var].dimensions))
        except RuntimeError:
            raise Warning('Cannot use variable name {}'.format('sic_anomaly'))
    return dst


def compute_anomalies(array):
    mean = array.mean(axis=(0,))
    anomalies = array - mean
    return anomalies


def main():
    infile = sys.argv[1]
    dst = add_anomaly_var(infile)
    sic = dst.variables['goddard_merged_seaice_conc_monthly'][:]
    dst_anomalies = compute_anomalies(sic)
    with nc.Dataset(infile, 'a') as dst:
        dst.variables['sic_anomaly'][:] = dst_anomalies


if __name__ == "__main__":
    main()
