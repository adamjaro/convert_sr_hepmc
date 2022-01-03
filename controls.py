#!/usr/bin/python3

from glob import glob
import math

from pandas import DataFrame, HDFStore, read_hdf
import matplotlib.pyplot as plt
import numpy as np

from pyHepMC3 import HepMC3 as hepmc

#_____________________________________________________________________________
def main():

    iplot = 6

    func = {}
    func[0] = plot_en
    func[1] = plot_theta
    func[2] = plot_phi
    func[3] = plot_xy
    func[4] = plot_x
    func[5] = plot_y
    func[6] = plot_z
    func[7] = plot_flux
    func[8] = plot_power
    func[9] = plot_zphi
    func[10] = plot_radius
    func[101] = create_df
    func[102] = create_df_all

    func[iplot]()

#main

#_____________________________________________________________________________
def plot_en():

    infile = "../10_std_highstatistics/hepmc_2484x.h5"

    inp = read_hdf(infile)

    nbins = 60

    #plt.style.use("dark_background")
    #col = "lime"
    col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    en_keV = inp["en"]*1e6

    plt.hist(en_keV, bins=nbins, color="blue", density=True, histtype="step", lw=2, range=(1,110))

    ax.set_xlabel("Energy (keV)")
    ax.set_ylabel("Normalized counts")

    ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_en

#_____________________________________________________________________________
def plot_theta():

    inp = read_hdf("sr.h5")

    nbins = 60

    #plt.style.use("dark_background")
    #col = "lime"
    col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(inp["theta"]*1e3, bins=nbins, color="blue", density=True, histtype="step", lw=2)

    ax.set_xlabel(r"$\theta$ (mrad)")
    ax.set_ylabel("Normalized counts")

    ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_theta

#_____________________________________________________________________________
def plot_phi():

    inp = read_hdf("sr.h5")

    nbins = 60

    #plt.style.use("dark_background")
    #col = "lime"
    col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(inp["phi"]+np.pi, bins=nbins, color="blue", density=True, histtype="step", lw=2)

    ax.set_xlabel(r"$\phi$ (rad)")
    ax.set_ylabel("Normalized counts")

    ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_phi

#_____________________________________________________________________________
def plot_xy():

    infile = "../10_std_highstatistics/hepmc_2484x.h5"

    inp = read_hdf(infile)

    nbins = 60

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist2d(inp["posx"], inp["posy"], bins=nbins)#, color="blue", density=True, histtype="step", lw=2)
    cbar = plt.colorbar()

    ax.set_xlabel("x (mm)")
    ax.set_ylabel("y (mm)")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_xy

#_____________________________________________________________________________
def plot_x():

    inp = read_hdf("sr.h5")

    nbins = 60

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(inp["posx"], bins=nbins, color="blue", density=True, histtype="step", lw=2)

    ax.set_xlabel("x (mm)")
    ax.set_ylabel("Normalized counts")

    #ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_x

#_____________________________________________________________________________
def plot_y():

    inp = read_hdf("sr.h5")

    nbins = 60

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(inp["posy"], bins=nbins, color="blue", density=True, histtype="step", lw=2)

    ax.set_xlabel("y (mm)")
    ax.set_ylabel("Normalized counts")

    #ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_y

#_____________________________________________________________________________
def plot_z():

    #infile = "../10_std_highstatistics/hepmc_2484x.h5"
    #infile = "../10_std_highstatistics/hepmc_1kevt.h5"
    #infile = "../10_std_highstatistics_2/hepmc_1kevt.h5"
    #infile = "../10_std_highstatistics_2/hepmc_2484x.h5"
    infile = "../10_standard_tail/hepmc_all.h5"
    #infile = "../10_optimistic/hepmc_all.h5"

    inp = read_hdf(infile)

    nbins = 60

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(inp["posz"]*1e-3, bins=nbins, color="blue", density=True, histtype="step", lw=2)

    ax.set_xlabel("Photon $z$ position (meters)")
    ax.set_ylabel("Normalized counts")

    #ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_z

#_____________________________________________________________________________
def plot_flux():

    inp = read_hdf("sr.h5")

    nbins = 60

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(inp["flux"], bins=nbins, color="blue", density=True, histtype="step", lw=2)

    ax.set_xlabel("Flux (photon/s)")
    ax.set_ylabel("Normalized counts")

    #ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_flux

#_____________________________________________________________________________
def plot_power():

    inp = read_hdf("sr.h5")

    nbins = 60

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(inp["power"], bins=nbins, color="blue", density=True, histtype="step", lw=2)

    ax.set_xlabel("Power (W)")
    ax.set_ylabel("Normalized counts")

    #ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_power

#_____________________________________________________________________________
def plot_zphi():

    inp = read_hdf("sr.h5")

    nbins = 80

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist2d(inp["posz"]*1e-3, inp["phi"]+math.pi, bins=nbins)
    cbar = plt.colorbar()

    ax.set_xlabel("z (m)")
    ax.set_ylabel("phi (rad)")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_zphi

#_____________________________________________________________________________
def plot_radius():

    inp = read_hdf("sr.h5")

    nbins = 60

    #plt.style.use("dark_background")
    #col = "lime"
    col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(np.sqrt(inp["posx"]**2+inp["posy"]**2), bins=nbins, color="blue", density=True, histtype="step", lw=2, range=(29.375, 29.5))

    ax.set_xlabel("Photon radial position (mm)")
    ax.set_ylabel("Normalized counts")

    ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_radius

#_____________________________________________________________________________
def create_df():

    #input hepmc
    #inp = "build/sr.hepmc"
    inp = "../hepmc/25118.hepmc"
    read = hepmc.ReaderAscii(inp)

    #output dataframe
    col = ["posx", "posy", "posz", "en", "theta", "phi", "flux", "power"]
    val = []

    #event loop
    while(True):

        mc = hepmc.GenEvent(hepmc.Units.GEV, hepmc.Units.MM)
        read.read_event(mc)
        if( read.failed() ): break

        lin = []

        pos = mc.event_pos()
        lin.append( pos.x() )
        lin.append( pos.y() )
        lin.append( pos.z() )

        vec = mc.particles()[0].momentum()
        lin.append( vec.e() )
        lin.append( vec.theta() )
        lin.append( vec.phi() )

        lin.append( float(mc.attribute("Flux_[photon/s]")) )
        lin.append( float(mc.attribute("Power_[W]")) )

        val.append( lin )

    df = DataFrame(val, columns=col)

    print(df)

    out = HDFStore("sr.h5")
    out["sr"] = df
    out.close()

    read.close()

#create_df

#_____________________________________________________________________________
def create_df_all():

    #input hepmc
    #inp = glob("../10_std_highstatistics/hepmc/?????.hepmc")
    #outname = "../10_std_highstatistics/hepmc_1kevt.h5"

    #inp = glob("../10_std_highstatistics_2/hepmc/2484?.hepmc")
    #outname = "../10_std_highstatistics_2/hepmc_2484x.h5"

    #inp = glob("../10_standard_tail/hepmc/?????.hepmc")
    #outname = "../10_standard_tail/hepmc_all.h5"

    inp = glob("../10_optimistic/hepmc/?????.hepmc")
    outname = "../10_optimistic/hepmc_all.h5"

    #nmax = 1000

    #output dataframe
    col = ["posx", "posy", "posz", "en", "theta", "phi", "flux", "power"]
    val = []

    #input loop
    for ih in inp:

        print(ih)

        read = hepmc.ReaderAscii(ih)

        #event loop
        while(True):
        #for iev in range(nmax):

            mc = hepmc.GenEvent(hepmc.Units.GEV, hepmc.Units.MM)
            read.read_event(mc)
            if( read.failed() ): break

            lin = []

            pos = mc.event_pos()
            lin.append( pos.x() )
            lin.append( pos.y() )
            lin.append( pos.z() )

            vec = mc.particles()[0].momentum()
            lin.append( vec.e() )
            lin.append( vec.theta() )
            lin.append( vec.phi() )

            lin.append( float(mc.attribute("Flux_[photon/s]")) )
            lin.append( float(mc.attribute("Power_[W]")) )

            val.append( lin )

    #input loop

    df = DataFrame(val, columns=col)

    print(df)

    out = HDFStore(outname)
    out["sr"] = df
    out.close()

    read.close()

#create_df_all

#_____________________________________________________________________________
def set_axes_color(ax, col):

    ax.xaxis.label.set_color(col)
    ax.yaxis.label.set_color(col)
    ax.tick_params(which = "both", colors = col)
    ax.spines["bottom"].set_color(col)
    ax.spines["left"].set_color(col)
    ax.spines["top"].set_color(col)
    ax.spines["right"].set_color(col)

#set_axes_color

#_____________________________________________________________________________
def set_grid(px, col="lime"):

    px.grid(True, color = col, linewidth = 0.5, linestyle = "--")

#set_grid

#_____________________________________________________________________________
if __name__ == "__main__":

    main()













