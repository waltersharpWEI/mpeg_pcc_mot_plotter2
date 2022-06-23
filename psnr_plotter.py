#the plotter of the psnr loss rate exp

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import json

def single_metric_loss_psnr_plot(df, video_type, loss_rate_list, fig_root, plot_name):
    asize = 36
    bsize = 36

    psnr_suffix = "_psnr"
    psnrs = np.array(df[video_type+psnr_suffix])

    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['hatch.linewidth'] = 3
    plt.rcParams["legend.handlelength"] = 1.0
    # set up the figure canvas
    figure = plt.figure(figsize=(16, 9), dpi=80)
    # set up the margin
    ax = figure.add_axes([0.115, 0.15, 0.8, 0.8])
    # set up the tick size
    ax.tick_params(pad=18, labelsize=bsize - 2)
    #draw lines
    ax.plot(loss_rate_list, psnrs)
    ax.set_ylabel('PSNR', fontsize=asize)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Packet Loss Rate(%)', fontsize=asize)
    #plt.legend(loc='upper right', ncol=3, fontsize=asize)
    fig_path = os.path.join(fig_root, plot_name + '.pdf')
    plt.savefig(fig_path)
    plt.show()
    return 0

if __name__=="__main__":
    exp_data_root = "exp_data"
    config_path = "exp_config.json"
    fig_root = "loss_figs"
    psnr_prefix = "psnr_"
    with open(config_path) as f1:
        jconfig = json.load(f1)
        csv_path = os.path.join(exp_data_root, psnr_prefix+str(jconfig["exp_id"]) + ".csv")
        video_types = jconfig["video_types"]
        loss_rate_list = jconfig["loss_rate"]
        df = pd.read_csv(csv_path)
        video_type = video_types[0]
        single_metric_loss_psnr_plot(df,video_type,loss_rate_list,fig_root,jconfig["exp_name"]+video_type)