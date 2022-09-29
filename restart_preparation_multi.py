import sys#, getopt
import numpy as np
#import matplotlib.pyplot as plt
#import h5py
import argparse
from pathlib import Path



def main():


    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--output_path',nargs='?',default='')
    parser.add_argument('-d','--input_delta_nu',nargs='?')
    parser.add_argument('-t','--input_theta_nu',nargs='?')
    parser.add_argument('-p','--input_pcb',nargs='?')
    parser.add_argument('-n','--streamnumber', type=int, nargs='?',default=1)
    parser.add_argument('-N','--Nstreams', type=int, nargs='?',default=10)
    parser.add_argument('-v','--verbose',action='store_true')
    args = parser.parse_args()

    #print(args)

    outputpath = args.output_path
    Path(outputpath).mkdir(parents=True,exist_ok=True)

    if args.verbose:
        myprint=pleaseprint
    else:
        myprint=dontprint

    if outputpath !='':
        if outputpath[-1]!='/':
            outputpath = outputpath + '/'



    streamno = args.streamnumber

    Nstreams = args.Nstreams

    if (hasattr(args,'input_delta_nu') and args.input_delta_nu != None):
        myprint('Processing delta_nu')
        delta_nu_dat = np.loadtxt(args.input_delta_nu,delimiter=',',usecols=range(0,51))
        k_delta = delta_nu_dat[:,0]
        delta = np.sum(delta_nu_dat[:,streamno:streamno+Nstreams],axis=1)/Nstreams
        deltasq = delta**2
        data_delta = np.array([k_delta,deltasq])
        np.savetxt(outputpath+'delta_nu.txt',data_delta.transpose())
        myprint('delta_nu done')

    if (hasattr(args,'input_theta_nu') and args.input_theta_nu != None):
        if hasattr(args,'input_delta_nu'):
            myprint('Processing growthrate')
            theta_nu_dat = np.loadtxt(args.input_theta_nu,delimiter=',',usecols=range(0,51))
            theta = np.sum(theta_nu_dat[:,streamno:streamno+Nstreams],axis=1)/Nstreams
            growthrate = theta/delta
            data_growthrate = np.array([k_delta,growthrate])
            np.savetxt(outputpath+'growthrate.txt',data_growthrate.transpose())
            myprint('growthrate done')
        else:
            raise UserWarning('Cannot calculate growthrate without delta')




    if (hasattr(args,'input_pcb')and args.input_pcb != None):
        myprint('Processing P_cb')
        Pcbdat = load_powerspec(args.input_pcb)
        np.savetxt(outputpath+'Pcb.txt',Pcbdat)
        myprint('P_cb done')







def load_powerspec(powerspecfile):
    header_length = 5
    with open(powerspecfile) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    numlines = int(lines[1])
    boxlength = float(lines[2])

    datalines = lines[header_length:header_length+numlines]

    data = np.zeros([numlines,5])

    for i, line in enumerate(datalines):
        data[i,:] = np.fromstring(line, dtype=float, sep=' ')

    k = data[:,0]
    pk = data[:,2]*boxlength**3 

    datarray = np.array([k,pk])

    return datarray.transpose()

def pleaseprint(str):
    print(str)

def dontprint(str):
    pass

if __name__ == "__main__":
   main()
