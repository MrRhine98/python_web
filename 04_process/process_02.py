# ----Queue---

import multiprocessing

def download_from_web(q):
    data = [11, 22, 33, 44]
    for temp in data:
        q.put(temp)
    print("Download complete")


def analysis_data(q):
    data_analysis = list()
    while not q.empty():
        data = q.get()
        data_analysis.append(data)
    print(data_analysis)

def main():
    '''q = multiprocessing.Queue(3)
    q.put('123')
    q.put(22)
    q.put([11, 22])
    q.get()
    q.get_nowait()
    q.full()
    q.empty()'''
    q = multiprocessing.Queue(4)
    p1 = multiprocessing.Process(target=download_from_web, args=(q, ))
    p2 = multiprocessing.Process(target=analysis_data, args=(q, ))
    p1.start()
    p2.start()



if __name__ == "__main__":
    main()
