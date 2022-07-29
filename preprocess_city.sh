#!/bin/bash

# python ./lib/datasets/preprocess/cityscapes/cityscapes_generator.py --coarse True \
# --save_dir /workspace/workspace/ProtoSeg_local/data/path/to/preprocessed_cityscapes \
# --ori_root_dir /workspace/workspace/ProtoSeg_local/data/original_cityscapes


# python ./lib/datasets/preprocess/cityscapes/cityscapes_generator.py --coarse False \
# --save_dir /workspace/workspace/ProtoSeg_local/data/path/to/preprocessed_cityscapes \
# --ori_root_dir /workspace/workspace/ProtoSeg_local/data/original_cityscapes

#ins

python ./lib/datasets/preprocess/cityscapes/cityscapes_instance_generator.py --coarse True \
--save_dir /workspace/workspace/ProtoSeg_local/data/path/to/preprocessed_cityscapes \
--ori_root_dir /workspace/workspace/ProtoSeg_local/data/original_cityscapes