#the plotter of the ssim loss rate exp

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import json
import logging

def single_metric_loss_ssim_plot(exp_root, protocol_list, video_type, loss_rate_list, fig_root, plot_name):
    asize = 36
    bsize = 36
    dfs = []
    for protocol in protocol_list:
        csv_path = os.path.join(exp_root, protocol, ssim_prefix + str(jconfig["exp_id"]) + ".csv")
        logging.warning(csv_path)
        df = pd.read_csv(csv_path)
        dfs.append(df)
    ssim_suffix = "_ssim"

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
    ax.plot(loss_rate_list, np.array(dfs[0][video_type+ssim_suffix]),
            label= protocol_list[0])
    ax.plot(loss_rate_list, np.array(dfs[1][video_type + ssim_suffix]),
            label= protocol_list[1])
    ax.plot(loss_rate_list, np.array(dfs[2][video_type + ssim_suffix]),
            label= protocol_list[2])
    ax.set_ylabel('ssim', fontsize=asize)
    #ax.set_ylim(0, 100)
    ax.set_xlim(1,5)
    ax.set_xlabel('Packet Loss Rate(%)', fontsize=asize)
    plt.legend(loc='upper right', ncol=3, fontsize=asize)
    fig_path = os.path.join(fig_root, plot_name + '.pdf')
    plt.savefig(fig_path)
    plt.show()
    return 0

if __name__=="__main__":
    logging.basicConfig(level=logging.WARNING)
    exp_root = "exp_data"
    protocol_list = ["partial","udp","quic"]
    config_path = "exp_config.json"
    fig_root = "loss_figs"
    ssim_prefix = "ssim_"
    with open(config_path) as f1:
        jconfig = json.load(f1)
        video_types = jconfig["video_types"]
        loss_rate_list = jconfig["loss_rate"]
        video_type = video_types[0]
        single_metric_loss_ssim_plot(exp_root,protocol_list,video_type,loss_rate_list,fig_root,jconfig["exp_name"]+"_"+video_type)