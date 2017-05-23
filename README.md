Dronning Maud Land sea ice climatology
--------------------------------------

To estimate the state of the sea ice cover (area and extent) we analyze sea ice concentration estimates that come from NSIDC.
This climatology is based on Goddard merged geophisycal product (NASA Team + Bootstrap).

The basic workflow goes as follows:

 * Obtain monthly sea ice concentration estimates from NSIDC FTP.
 * Merge records using Climate Data Operators
 * Produce mean estimates for each month across all years
 * Compute anomalies
 * Mask out everything but Dronning Maud Land, the area between 20 degrees West and 45 degrees East
 * Estimate sea ice area in square kilometers for all years
