import pytest
import pynmea2

import datetime

def test_GGA():
    data = "$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D"
    msg = pynmea2.parse(data)
    assert msg.talker == 'GP'
    assert msg.type == 'GGA'

    # Timestamp
    assert msg.timestamp        == datetime.time(18, 43, 53)
    # Latitude
    assert msg.lat              == '1929.045'
    # Latitude Direction
    assert msg.lat_dir          == 'S'
    # Longitude
    assert msg.lon              == '02410.506'
    # Longitude Direction
    assert msg.lon_dir          == 'E'
    # GPS Quality Indicator
    assert msg.gps_qual         == '1'
    # Number of Satellites in use
    assert msg.num_sats         == '04'
    # Horizontal Dilution of Precision
    assert msg.horizontal_dil   == '2.6'
    # Antenna Alt above sea level (mean)
    assert msg.altitude         == 100.0
    # Units of altitude (meters)
    assert msg.altitude_units   == 'M'
    # Geoidal Separation
    assert msg.geo_sep          == '-33.9'
    # Units of Geoidal Separation (meters)
    assert msg.geo_sep_units    == 'M'
    # Age of Differential GPS Data (secs)
    assert msg.age_gps_data     == ''
    # Differential Reference Station ID
    assert msg.ref_station_id   == '0000'

    msg.altitude = 200.0
    assert str(msg) == "$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,200.0,M,-33.9,M,,0000*5E"

def test_rte():
    data = "$GPRTE,2,1,c,0,PBRCPK,PBRTO,PTELGR,PPLAND,PYAMBU,PPFAIR,PWARRN,PMORTL,PLISMR*73"
    msg = pynmea2.parse(data)
    assert msg.talker == 'GP'
    assert msg.type == 'RTE'
    assert "2" == msg.num_in_seq
    assert "1" == msg.sen_num
    assert "c" == msg.start_type
    assert "0" == msg.active_route_id
    assert msg.waypoint_list == [
        "PBRCPK", "PBRTO", "PTELGR", "PPLAND", "PYAMBU",
        "PPFAIR", "PWARRN", "PMORTL", "PLISMR"]

    msg.waypoint_list = ['ABC','DEF']
    assert str(msg) == "$GPRTE,2,1,c,0,ABC,DEF*03"

def test_r00():
    data = "$GPR00,A,B,C*29"
    msg = pynmea2.parse(data)
    assert msg.talker == 'GP'
    assert msg.type == 'R00'
    assert msg.waypoint_list == ['A','B','C']

    msg.waypoint_list = ['ABC','DEF']
    assert str(msg) == "$GPR00,ABC,DEF*42"