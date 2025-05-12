import pebblenet as pbn

def main():
    """
    Original source code can be found at:
    https://github.com/dawnandrew100/pebblenet/blob/main/pebblenet/Maryland/noaa_data.py

    This module processes NOAA data for Maryland's Chesapeake Bay stations.
    """
    print(pbn.process_noaa_data())

if __name__ == "__main__":
    main()
