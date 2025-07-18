# Copyright © 2022 BAAI. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
import torch
from flagai.auto_model.auto_loader import AutoLoader
from flagai.model.predictor.predictor import Predictor

# Initialize 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

loader = AutoLoader(task_name="text2img", #contrastive learning
                    model_name="AltDiffusion-m18",  # use m18 to do the experiment
                    model_dir="./checkpoints",
                    fp16=False)

model = loader.get_model()
model.eval()
model.to(device)
predictor = Predictor(model)
predictor.predict_generate_images(
    prompt="smile😁",
    # negative_prompt=negative_prompt,
    # outpath="./AltDiffusionOutputs",
    ddim_steps=20,
    plms=True,
    skip_grid=True,      # or False if you want a grid image
)

