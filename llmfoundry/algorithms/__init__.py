# Copyright 2024 MosaicML LLM Foundry authors
# SPDX-License-Identifier: Apache-2.0

from composer.algorithms import (
    Alibi,
    GatedLinearUnits,
    GradientClipping,
    LowPrecisionLayerNorm,
    LabelSmoothing,
)

from llmfoundry.registry import algorithms

algorithms.register('gradient_clipping', func=GradientClipping)
algorithms.register('label_smoothing', func=LabelSmoothing)
algorithms.register('alibi', func=Alibi)
algorithms.register('gated_linear_units', func=GatedLinearUnits)
algorithms.register('low_precision_layernorm', func=LowPrecisionLayerNorm)
