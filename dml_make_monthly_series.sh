#!/bin/bash
set -e

# Handle the command line options
while [ "$#" -gt 0 ]; do
  case "$1" in
    -d) INPUT_DIR="$2"; shift 2;;
    -m) MONTH="$2"; shift 2;;
    -o) OUTPUT_DIR="$2"; shift 2;;
    -f) FORCE="yes"; shift ;;

    -*) echo "unknown option: $1" >&2; exit 1;;
    *) handle_argument "$1"; shift 1;;
  esac
done

# check if the output directory exists
if [ ! -d $OUTPUT_DIR ]; then
  if [ "$FORCE" == "yes" ]; then
    mkdir ${OUTPUT_DIR}
  else
    echo "$(date): Directory $OUTPUT_DIR does not exist, exiting"
  fi
fi

function make_monthly_mean() {
  input_dir=$1
  outdir=$2
  month=$3
  fileglob="seaice_conc_monthly_sh_???_????${month}_v02r00.nc"
  echo $fileglob $input_dir $outdir $month

  merged_monthly_ncfile=$outdir/merged_seaice_conc_monthly_${month}.nc
  monthly_mean_ncfile=$outdir/monthly_seaice_conc_${month}.nc

  # concatenate the entire series series to monthly files
  cdo mergetime ${input_dir}/${fileglob} $merged_monthly_ncfile
  cdo setdate,1978-${month}-15 -timmean ${merged_monthly_ncfile} ${monthly_mean_ncfile}.time.nc
}

MONTH=$(printf %02d $MONTH)
make_monthly_mean ${INPUT_DIR} ${OUTPUT_DIR} ${MONTH}

