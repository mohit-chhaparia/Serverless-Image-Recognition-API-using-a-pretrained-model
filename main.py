from fastapi import FastAPI, UploadFile, File, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from PIL import Image, UnidentifiedImageError
import io

import torch
import torch.nn.functional as F
from torchvision.models import resnet18, ResNet18_Weights

app = FastAPI(title="Image Classifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
