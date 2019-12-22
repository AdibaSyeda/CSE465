# -*- coding: utf-8 -*-

import os
orig_input_dataset = "malaria/cell_images"
base_path = "malaria"

train_path = os.path.sep.join([base_path, "training"])
val_path = os.path.sep.join([base_path, "validation"])
test_path = os.path.sep.join([base_path, "testing"])

train_split = 0.8
val_split = 0.1