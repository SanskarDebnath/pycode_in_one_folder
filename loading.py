import time
from tqdm import tqdm

print('Downloading Package Name sanskar 1')
for _ in tqdm(range(5),#We can change this range according to our file size
    desc="downloading..",
    ascii = False): #ascii false means there will be no numeric values in progress bar like 
    time.sleep(0.5)#when i set the time.sleep in 5 it means after 5 sec 10% will be loaded
print("Waiting for installation Package name sanskar 1")
time.sleep(1)

print('Downloading Package Name sanskar 2')
for _ in tqdm(range(10),
    desc="downloading...",
    ascii=False):
    time.sleep(0.7)
print("Waiting for installation Package name sanskar 2")
time.sleep(2)

print("Downloading Package name sanskar 3")
for _ in tqdm(range(20),
    desc="downloading...",
    ascii=False):
    time.sleep(0.5)
print("Waiting for installation Package name sanskar 3")
time.sleep(2.5)

print('Downloading Package Name sanskar 4')
for _ in tqdm(range(50),
    desc="downloading..",
    ascii = False):
    time.sleep(0.7)
print("Waiting for installation Package name sanskar 4")
time.sleep(2.5)

print('Downloading Package Name sanskar 5')
for _ in tqdm(range(100),
    desc="downloading...",
    ascii=False):
    time.sleep(0.4)
print("Waiting for installation Package name sanskar 5")
time.sleep(2)

print("Installing All packages")
time.sleep(10)
print("done")
print("All packages are installed in"+"C:/Users/Acer/OneDrive/Desktop/all_py_code/pycode_in_one_folder")

