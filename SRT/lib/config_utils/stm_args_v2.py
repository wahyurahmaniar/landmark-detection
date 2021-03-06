# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import os, sys, time, random, argparse
from .share_args import add_shared_args

def obtain_stm_args_v2():
  parser = argparse.ArgumentParser(description='Train facial landmark detectors on 300-W or AFLW', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('--train_lists',      type=str,   nargs='+',      help='The list file path to the video training dataset.')
  parser.add_argument('--eval_vlists',      type=str,   nargs='+',      help='The list file path to the video testing dataset.')
  parser.add_argument('--eval_ilists',      type=str,   nargs='+',      help='The list file path to the image testing dataset.')
  parser.add_argument('--num_pts',          type=int,                   help='Number of point.')
  parser.add_argument('--x68to49',          action='store_true',        help='For 300-W 300VW, convert 68 points to 49 points.')
  parser.add_argument('--model_config',     type=str,                   help='The path to the model configuration')
  parser.add_argument('--opt_config',       type=str,                   help='The path to the optimizer configuration')
  parser.add_argument('--stm_config',       type=str,                   help='The path to the supervision-by-registration configuration')
  parser.add_argument('--init_model',       type=str,                   help='The path to the initial detection model.')
  parser.add_argument('--procedure',        type=str,                   help='The procedure basic prefix.')
  add_shared_args( parser )
  # Optimization options
  parser.add_argument('--debug',            action='store_true',        help='debug or not ')
  parser.add_argument('--eval_first',       action='store_true',        help='Evaluate before training?')
  parser.add_argument('--i_batch_size',     type=int,   default=2,      help='Batch size for images during training.')
  parser.add_argument('--v_batch_size',     type=int,   default=2,      help='Batch size for video data during training.')
  parser.add_argument('--m_batch_size',     type=int,   default=2,      help='Batch size for multiview data during training.')
  args = parser.parse_args()

  if args.rand_seed is None or args.rand_seed < 0:
    args.rand_seed = random.randint(1, 100000)
  assert args.save_path is not None, 'save-path argument can not be None'
  args.use_gray = args.use_gray > 0
  #state = {k: v for k, v in args._get_kwargs()}
  #Arguments = namedtuple('Arguments', ' '.join(state.keys()))
  #arguments = Arguments(**state)
  return args
