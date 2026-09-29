"""Carga de datos y splits.

REGLAS QUE NO SE ROMPEN (y que el revisor del PR comprueba):
  1. El split se hace ANTES de cualquier transformacion ajustada a los datos.
  2. La normalizacion usa estadisticas de ENTRENAMIENTO, nunca del conjunto
     completo. Lo contrario es una fuga: no da error e infla tu metrica.
  3. El data augmentation se aplica a train, jamas a validacion ni a test.
"""

from __future__ import annotations

from array import array
import struct
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset, Subset
from torchvision import transforms


class DatasetPlaceholder(Dataset):
    """Sustituye esto por el dataset de tu paper.

    Se deja aqui un dataset sintetico para que `python run.py --smoke` funcione
    desde el minuto cero, antes de que hayas escrito nada. Es lo que permite que
    tengas el vertical slice en verde el primer dia.
    """

    def __init__(self, n: int = 512, dim: int = 32, clases: int = 10):
        g = torch.Generator().manual_seed(0)
        self.x = torch.randn(n, dim, generator=g)
        self.y = torch.randint(0, clases, (n,), generator=g)

    def __len__(self) -> int:
        return len(self.x)

    def __getitem__(self, i: int):
        return self.x[i], self.y[i]

def construir_loaders(cfg: dict) -> tuple[DataLoader, DataLoader]:
    """Devuelve (train_loader, val_loader) segun la configuracion."""
    dcfg = cfg["datos"]

    train_ds: Dataset = DatasetPlaceholder()
    val_ds: Dataset = DatasetPlaceholder(n=128)

    # Regla 5/20: el subset se aplica DESPUES del split, para no cambiar la
    # distribucion de validacion.
    if dcfg.get("subset"):
        n = int(dcfg["subset"])
        train_ds = Subset(train_ds, range(min(n, len(train_ds))))

    comun = dict(batch_size=dcfg["batch_size"],
                 num_workers=dcfg.get("num_workers", 0))
    return (DataLoader(train_ds, shuffle=True, **comun),
            DataLoader(val_ds, shuffle=False, **comun))

# MNIST Dataset

class MnistDataset(Dataset):
    def __init__(self, images, labels, transform=transforms.ToTensor()):
        super().__init__()
        self.images = images
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        return self.transform(self.images[idx]), self.labels[idx]

class MnistDataloader(object):
    def __init__(self, training_images_filepath,training_labels_filepath,
                 test_images_filepath, test_labels_filepath):
        self.training_images_filepath = training_images_filepath
        self.training_labels_filepath = training_labels_filepath
        self.test_images_filepath = test_images_filepath
        self.test_labels_filepath = test_labels_filepath

    def read_images_labels(self, images_filepath, labels_filepath):
        labels = []
        with open(labels_filepath, 'rb') as file:
            magic, size = struct.unpack(">II", file.read(8))
            if magic != 2049:
                raise ValueError('Magic number mismatch, expected 2049, got {}'.format(magic))
            labels = array("B", file.read())

        with open(images_filepath, 'rb') as file:
            magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
            if magic != 2051:
                raise ValueError('Magic number mismatch, expected 2051, got {}'.format(magic))
            image_data = array("B", file.read())
        images = []
        for i in range(size):
            img = np.array(image_data[i * rows * cols:(i + 1) * rows * cols])
            img = img.reshape(28, 28)
            images.append(img)
        return images, labels

    def get_datasets(self):
        return MnistDataset(self.train_images, self.train_labels, transforms.ToTensor()), MnistDataset(self.test_images, self.test_labels, transforms.ToTensor())
    
    def load_data(self):
        self.train_images, self.train_labels = self.read_images_labels(self.training_images_filepath, self.training_labels_filepath)
        self.test_images, self.test_labels = self.read_images_labels(self.test_images_filepath, self.test_labels_filepath)

    