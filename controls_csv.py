#!/usr/bin/python3

from glob import glob
import math

from pandas import DataFrame, read_csv, concat
import matplotlib.pyplot as plt

#_____________________________________________________________________________
def main():

    iplot = 2

    func = {}
    func[0] = plot_z
    func[1] = plot_xy
    func[2] = plot_z_all
    func[3] = plot_xy_all

    func[iplot]()

#main

#_____________________________________________________________________________
def plot_z():

    inp = read_csv("../input/25098.csv")

    nbins = 60

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(inp["Pos_Z_[cm]"], bins=nbins, color="blue", density=True, histtype="step", lw=2)

    ax.set_xlabel("z (cm)")
    ax.set_ylabel("Normalized counts")

    #ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_z

#_____________________________________________________________________________
def plot_xy():

    inp = read_csv("../input/25098.csv")

    nbins = 60

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist2d(inp["Pos_X_[cm]"], inp["Pos_Y_[cm]"], bins=nbins)
    cbar = plt.colorbar()

    ax.set_xlabel("x (cm)")
    ax.set_ylabel("y (cm)")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_xy

#_____________________________________________________________________________
def plot_z_all():

    #infiles = "../input/?????.csv"
    infiles = "../10_standard_tail/?????.csv"

    inp_all = glob(infiles)
    print("All inputs:", len(inp_all))

    inp = concat([read_csv(i) for i in inp_all], ignore_index=True)

    nbins = 60

    plt.style.use("dark_background")
    col = "lime"
    #col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist(inp["Pos_Z_[cm]"], bins=nbins, color="blue", density=True, histtype="step", lw=2)

    ax.set_xlabel("z (cm)")
    ax.set_ylabel("Normalized counts")

    #ax.set_yscale("log")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_z_all

#_____________________________________________________________________________
def plot_xy_all():

    inp = concat([read_csv(i) for i in glob("../input/?????.csv")], ignore_index=True)

    nbins = 60

    #plt.style.use("dark_background")
    #col = "lime"
    col = "black"

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    #set_axes_color(ax, col)
    set_grid(plt, col)

    plt.hist2d(inp["Pos_X_[cm]"], inp["Pos_Y_[cm]"], bins=nbins)
    cbar = plt.colorbar()

    ax.set_xlabel("Pos_X_[cm]")
    ax.set_ylabel("Pos_Y_[cm]")

    fig.savefig("01fig.pdf", bbox_inches = "tight")
    plt.close()

#plot_xy_all

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


































