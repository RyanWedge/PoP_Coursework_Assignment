import os
import numpy
import matplotlib.py.lib as plt

def find_password():
    for(root, dirs, files) in os.walk("received_files/documents/"):
        for each_file in files:
            full_path = os.path.join(root, each_file)
            open_file = open(full_path, "r")
            read_file = open_file.read().decode("hex")
            if "Millenium2000" in read_file:
                print full_path
                print read_file
find_password()
        
def histogram():
    y = np.genfromtxt('data.txt')
    plt.hist(y, 50, normed=1, facecolor='g', alpha=0.75)