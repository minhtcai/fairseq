# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the LICENSE file in
# the root directory of this source tree. An additional grant of patent rights
# can be found in the PATENTS file in the same directory.
#

import argparse

from fairseq import models


def get_parser(desc):
    parser = argparse.ArgumentParser(
        description='Facebook AI Research Sequence-to-Sequence Toolkit -- ' + desc)
    parser.add_argument('--no-progress-bar', action='store_true', help='disable progress bar')
    parser.add_argument('--log-interval', type=int, default=1000, metavar='N',
                        help='log progress every N updates (when progress bar is disabled)')
    parser.add_argument('--seed', default=1, type=int, metavar='N',
                        help='pseudo random number generator seed')
    return parser


def add_dataset_args(parser):
    group = parser.add_argument_group('Dataset and data loading')
    group.add_argument('data', metavar='DIR',
                       help='path to data directory')
    group.add_argument('-s', '--source-lang', default=None, metavar='SRC',
                       help='source language')
    group.add_argument('-t', '--target-lang', default=None, metavar='TARGET',
                       help='target language')
    group.add_argument('-j', '--workers', default=1, type=int, metavar='N',
                       help='number of data loading workers (default: 1)')
    return group


def add_optimization_args(parser):
    group = parser.add_argument_group('Optimization')
    group.add_argument('--lr', '--learning-rate', default=0.25, type=float, metavar='LR',
                       help='initial learning rate')
    group.add_argument('--min-lr', metavar='LR', default=1e-5, type=float,
                       help='minimum learning rate')
    group.add_argument('--force-anneal', '--fa', default=0, type=int, metavar='N',
                       help='force annealing at specified epoch')
    group.add_argument('--max-epoch', '--me', default=0, type=int, metavar='N',
                       help='force stop training at specified epoch')
    group.add_argument('--lrshrink', default=0.1, type=float, metavar='LS',
                       help='learning rate shrink factor for annealing, lr_new = (lr * lrshrink)')
    group.add_argument('--momentum', default=0.99, type=float, metavar='M',
                       help='momentum factor')
    group.add_argument('--clip-norm', default=25, type=float, metavar='NORM',
                       help='clip threshold of gradients')
    group.add_argument('--weight-decay', '--wd', default=0.0, type=float, metavar='WD',
                       help='weight decay')
    group.add_argument('--sample-without-replacement', default=0, type=int, metavar='N',
                       help='If bigger than 0, use that number of mini-batches for each epoch,'
                            ' where each sample is drawn randomly with replacement from the'
                            ' dataset')
    return group


def add_checkpoint_args(parser):
    group = parser.add_argument_group('Checkpointing')
    group.add_argument('--save-dir', metavar='DIR', default='checkpoints',
                       help='path to save checkpoints')
    group.add_argument('--restore-file', default='checkpoint_last.pt',
                       help='filename in save-dir from which to load checkpoint')
    group.add_argument('--save-interval', type=int, default=-1,
                       help='checkpoint every this many batches')
    group.add_argument('--nosave', action='store_true',
                       help='don\'t save models and checkpoints')
    group.add_argument('--no-epoch-checkpoints', action='store_true',
                       help='only store last and best checkpoints')
    return group


def add_generation_args(parser):
    group = parser.add_argument_group('Generation')
    group.add_argument('--beam', default=5, type=int, metavar='N',
                       help='beam size')
    group.add_argument('--nbest', default=1, type=int, metavar='N',
                       help='number of hypotheses to output')
    group.add_argument('--max-len-a', default=0, type=int, metavar='N',
                       help=('generate sequence of maximum length ax + b, '
                             'where x is the source length'))
    group.add_argument('--max-len-b', default=200, type=int, metavar='N',
                       help=('generate sequence of maximum length ax + b, '
                             'where x is the source length'))
    group.add_argument('--remove-bpe', action='store_true',
                       help='remove BPE tokens before scoring')
    group.add_argument('--no-early-stop', action='store_true',
                       help=('continue searching even after finalizing k=beam '
                             'hypotheses; this is more correct, but increases '
                             'generation time by 50%%'))
    group.add_argument('--unnormalized', action='store_true',
                       help='compare unnormalized hypothesis scores')
    group.add_argument('--cpu', action='store_true', help='generate on CPU')
    group.add_argument('--no-beamable-mm', action='store_true',
                       help='don\'t use BeamableMM in attention layers')
    group.add_argument('--lenpen', default=1, type=float,
                       help='length penalty: <1.0 favors shorter, >1.0 favors longer sentences')
    return group


def add_model_args(parser):
    group = parser.add_argument_group('Model configuration')
    group.add_argument('--arch', '-a', default='fconv', metavar='ARCH',
                       choices=models.__all__,
                       help='model architecture ({})'.format(', '.join(models.__all__)))
    group.add_argument('--encoder-embed-dim', default=512, type=int, metavar='N',
                       help='encoder embedding dimension')
    group.add_argument('--encoder-layers', default='[(512, 3)] * 20', type=str, metavar='EXPR',
                       help='encoder layers [(dim, kernel_size), ...]')
    group.add_argument('--decoder-embed-dim', default=512, type=int, metavar='N',
                       help='decoder embedding dimension')
    group.add_argument('--decoder-layers', default='[(512, 3)] * 20', type=str, metavar='EXPR',
                       help='decoder layers [(dim, kernel_size), ...]')
    group.add_argument('--decoder-attention', default='True', type=str, metavar='EXPR',
                       help='decoder attention [True, ...]')
    group.add_argument('--decoder-out-embed-dim', default=256, type=int, metavar='N',
                       help='decoder output embedding dimension')
    group.add_argument('--dropout', default=0.1, type=float, metavar='D',
                       help='dropout probability')
    group.add_argument('--label-smoothing', default=0, type=float, metavar='D',
                       help='epsilon for label smoothing, 0 means no label smoothing')
    return group
