import h5py
import numpy as np


class DateLoader:
    file = None

    def __init__(self, pth):
        self.file = h5py.File(pth, 'r')

    def __get_sites(self):
        sites = []
        for site in self.file:
            sites.append(site)
        return sites

    def __get_sats(self, site, fhdf=None):
        file = self.file if not fhdf else fhdf
        if site in file:
            sats = [sat for sat in file[site]]
        return sats

    def __get_data(self, site, sat, field, fhdf=None):
        file = self.file if not fhdf else fhdf
        if site in file and sat in file[site]:
            times = file[site][sat][field][:]
        return times

    def get_series(self, site, sat, field):
        ts = self.__get_data(site, sat, 'timestamp')
        data = self.__get_data(site, sat, field)
        return ts, data

    def get_map(self, time, field):
        result = []
        timestamp = time.timestamp()
        start = timestamp
        end = timestamp
        sites = self.__get_sites()
        for site in sites:
            lat = np.degrees(self.file[site].attrs['lat'])
            lon = np.degrees(self.file[site].attrs['lon'])
            sats = self.__get_sats(site, fhdf=self.file)
            for sat in sats:
                timestamps = self.__get_data(site, sat, 'timestamp', fhdf=self.file)
                data = self.__get_data(site, sat, field, fhdf=self.file)
                match = np.where((timestamps >= start) & (timestamps <= end))
                data_match = data[match]
                for d in data_match:
                    result.append((d, lon, lat))
        if not result:
            return None
        else:
            return np.array(result)

    def __del__(self):
        self.file.close()
