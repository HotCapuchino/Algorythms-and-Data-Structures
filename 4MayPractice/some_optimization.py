import h5py
import numpy as np
import os
import pickle


class DateLoader:
    file = None
    __written = None

    def __init__(self, pth):
        self.file = h5py.File(pth, 'r')

    # can be problematic
    def __get_sites(self):
        sites = []
        for site in self.file:
            sites.append(site)
        return sites

    # can be problematic
    def __get_sats(self, site, fhdf=None):
        file = self.file if not fhdf else fhdf
        if site in file:
            sats = [sat for sat in file[site]]
        return sats

    # can be problematic
    def __get_data(self, site, sat, field, fhdf=None):
        file = self.file if not fhdf else fhdf
        if site in file and sat in file[site]:
            times = file[site][sat][field][:]
        return times

    def get_series(self, site, sat, field):
        ts = self.__get_data(site, sat, 'timestamp')
        data = self.__get_data(site, sat, field)
        return ts, data

#
    def __save_data(self, path, site, field):
        data_dictionary = {
            'lat': None,
            'lon': None,
            'sats_data': None
        }
        with open(path, 'wb') as f:
            lat = self.file[site].attrs['lat']
            lon = self.file[site].attrs['lon']
            pickle.dump(lat, f)
            pickle.dump(lon, f)
            sats = [sat for sat in self.file[site]]
            sats_data = []
            for sat in sats:
                timestamps, data = self.get_series(site, sat, field)
                sats_data.append((timestamps, data))
            pickle.dump(sats_data, f)
            data_dictionary.update({'lat': lat})
            data_dictionary.update({'lon': lon})
            data_dictionary.update({'sats_data': sats_data})
        return data_dictionary

    def __read_data(self, path):
        data_dictionary = {
            'lat': None,
            'lon': None,
            'sats_data': None
        }
        with open(path, 'rb') as f:
            data_dictionary.update({'lat': pickle.load(f)})
            data_dictionary.update({'lon': pickle.load(f)})
            data_dictionary.update({'sats_data': pickle.load(f)})
        return data_dictionary
#

    def get_map(self, time, field):
        result = []
        timestamp = time.timestamp()
        start = timestamp
        end = timestamp
        sites = self.file.keys()
        for site in sites:
            lat = np.degrees(self.file[site].attrs['lat'])
            lon = np.degrees(self.file[site].attrs['lon'])
            # it can be trouble
            sats = self.__get_sats(site, fhdf=self.file)
            print(site, end=', amount of satellites: ')
            print(len(sats))
            #
            for sat in sats:
                # it can be trouble
                timestamps, data = self.get_series(site, sat, field)
                #
                match = np.where((timestamps >= start) & (timestamps <= end))
                data_match = data[match]
                for d in data_match:
                    result.append((d, lon, lat))
        if not result:
            return None
        else:
            return np.array(result)

    def get_map_modified(self, time, field):
        result = []
        timestamp = time.timestamp()
        start = timestamp
        end = timestamp
        sites = self.file.keys()
        if os.path.exists(f'./res/{field}'):
            self.__written = [f for f in os.listdir(f'./res/{field}') if os.path.isfile(os.path.join(f'./res/{field}', f))]
        else:
            os.mkdir(f'./res/{field}')
            self.__written = []
        for site in sites:
            data_dictionary = None
            if not f'./res/{field}/{site}.dat' in self.__written:
                data_dictionary = self.__save_data(f'./res/{field}/{site}.dat', site, field)
            else:
                data_dictionary = self.__read_data(f'./res/{field}/{site}.dat')
            sats_data = data_dictionary.get('sats_data')
            for sat_data in sats_data:
                match = np.where((sat_data[0] >= start) & (sat_data[0] <= end))
                data_match = sat_data[1][match]
                for d in data_match:
                    result.append((d, data_dictionary.get('lon'), data_dictionary.get('lat')))
        if not result:
            return None
        else:
            return np.array(result)

    def __del__(self):
        self.file.close()
