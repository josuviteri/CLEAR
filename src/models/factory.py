"""Construccion del modelo.

Aqui va tu replicacion. El objetivo de E1 es que el forward produzca las
FORMAS que declara el paper, aunque los pesos sean aleatorios.
"""

from __future__ import annotations

import torch.nn as nn


class ModeloPlaceholder(nn.Module):
    """Sustituye esto por la arquitectura del paper."""

    def __init__(self, dim_entrada: int = 32, clases: int = 10):
        super().__init__()
        self.red = nn.Sequential(
            nn.Linear(dim_entrada, 64),
            nn.ReLU(),
            nn.Linear(64, clases),
        )

    def forward(self, x):
        return self.red(x)


def construir_modelo(cfg: dict) -> nn.Module:
    nombre = cfg["modelo"]["nombre"]
    if nombre == "mi_modelo":
        return ModeloPlaceholder()
    raise ValueError(f"modelo desconocido: {nombre}")


class Mnist(nn.Module):
    def __init__(
        self,
        hidden_layer_units: list[int] | None = None,
        output_size: int = 10,
    ):
        super().__init__()

        hidden_layer_units = hidden_layer_units or []
        layers = [nn.Flatten()]
        input_size = 28 * 28

        for units in hidden_layer_units:
            layers.extend([
                nn.Linear(input_size, units),
                nn.ReLU(),
            ])
            input_size = units

        layers.append(nn.Linear(input_size, output_size))
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)


def build_mnist(cfg: dict) -> nn.Module:
    model_cfg = cfg["modelo"]

    return Mnist(
        hidden_layer_units=model_cfg.get("hidden_layers", [256, 128]),
        output_size=model_cfg.get("output_size", 10),
    )