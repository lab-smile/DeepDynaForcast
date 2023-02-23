#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
config.py: 
"""
import argparse


def get_arguments():
    description = "Implementation of DeepPhyTree"
    parser = argparse.ArgumentParser(description=description)

    # General options
    general = parser.add_argument_group("General options")
    general.add_argument("-s", "--seed", type=float, default=123)
    general.add_argument("--num_gpus", type=int, default=1)
    general.add_argument("--vis_cuda", type=int, default=0)
    general.add_argument("--mode", type=str, default="train", choices=["train", "eval"], help="Train or predict")
    general.add_argument("--restore", type=bool, default=False, help="Restore model weight or not.")
    #general.add_argument("--local_rank", type=int)
    general.add_argument("--restore_metric", type=str, default="loss", help="The metric used for restoring the weight",
                         choices=["loss"])
    general.add_argument("--log_level", type=str, default="info")
    general.add_argument("--log_train_freq", type=int, default=1)
    general.add_argument("--log_valid_freq", type=int, default=1)

    # Data Options
    data = parser.add_argument_group("Data specific options")
    data.add_argument("--ds_name", type=str, default="ddf_resp+TB_20230222", help="The name of dataset")
    data.add_argument("--ds_dir", type=str, default="/mnt/data2/chaoyue/data/", help="The base folder for data")
    data.add_argument("--ds_split", type=str, default="split_rs123")
    data.add_argument("--num_workers", type=int, default=0, help='The number of workers used for loading data.')
    data.add_argument("--batch_size", type=int, default=4, help="batch size for the graph training")
    data.add_argument("--node_label_cols", type=str, default="dynamic_cat",
                      choices=["dynamic_cat", "extend_dynamic_cat"])
    data.add_argument("--edge_feat_cols", type=str, default="norm_edge_feats_arsinh")
    data.add_argument("--add_self_loop", type=bool, default=False)
    data.add_argument("--bidirection", type=bool, default=True)
    data.add_argument("--demo", type=bool, default=False)

    # Model Option
    model = parser.add_argument_group("Model options")
    model.add_argument("--model", type=str, default="pdglstm_0",
                       choices=["gcn","gat","gin","pdglstm_0","pdglstm_sc","pdglstm_bn"])
    model.add_argument("-n", "--model_num", type=int, default=1, help="The number of model")
    model.add_argument("--loss", type=str, default="ce", choices=["ce"])
    model.add_argument("--loss_ignore_bg", type=bool, default=True, help="Set loss weight as 0 for bg nodes")

    # Train Options
    train = parser.add_argument_group("Train options")
    train.add_argument("--max_epochs", type=int, default=100)
    train.add_argument('--optimizer', default='Adam')
    train.add_argument('--init_lr', '-l', type=float, default=0.001,
                       help='The current learning rate.(SGD/Mom: 0.01, Adam: 0.001)')
    train.add_argument('--min_lr', '-mlr', type=float, default=1e-6,
                       help='The minimum learning rate for training.')
    train.add_argument('--lr_decay_mode', '-lm', type=str, default='step',
                       choices=['exp', 'anneal', 'plateau', 'step', 'warmup'])
    train.add_argument('--lr_decay_step_or_patience', type=int, default=50,
                       help='learning rate decay patience on plateau')
    train.add_argument('--lr_decay_rate', '-a', type=float, default=0.1, help='The learning rate decay speed.')
    train.add_argument('--grad_clip', type=float, default=15)
    train.add_argument('--weight_decay_rate', '-wd', type=float, default=0.0004,
                       help='The weight decay rate for l2 loss.')
    train.add_argument('--early_stopping', default=50, help='The early stopping step.')
    args = parser.parse_args()
    return args
