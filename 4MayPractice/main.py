import time
import pytz
import matplotlib.pyplot as plt
from datetime import datetime, timezone
from some_optimization import DateLoader
import pickle


if __name__ == '__main__':
    plot_map = True
    pth = 'data.h5'
    date_loader = DateLoader(pth)
    if not plot_map:
        timestamps, data = date_loader.get_series('arsk', 'G03', 'dtec_20_60')
        times = [datetime.fromtimestamp(t, pytz.utc) for t in timestamps]
        plt.scatter(times, data)
        plt.xlim(times[0], times[-1])
        plt.show()
    else:
        epoch = datetime(2020, 5, 20, 12, 30, 0, tzinfo=timezone.utc)
        before = time.time()
        data = date_loader.get_map_modified(epoch, 'dtec_20_60')
        print(f'It took {time.time() - before} sec. to retrieve a map')
        val = data[:, 0]
        x = data[:, 1]
        y = data[:, 2]
        plt.scatter(x, y, c=val)
        plt.xlim(-180, 180)
        plt.ylim(-90, 90)
        plt.show()