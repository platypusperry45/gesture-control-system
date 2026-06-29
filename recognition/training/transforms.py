"""
Image augmentation transforms.

Part B1:
- Rotation
- Translation
- Scaling
- Brightness
- Contrast
- Gamma
"""

from __future__ import annotations

import random

import cv2
import numpy as np

from .config import AugmentationConfig


# ==========================================================
# Rotation
# ==========================================================

def rotate(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    angle = random.uniform(
        -config.max_rotation,
        config.max_rotation,
    )

    h, w = image.shape[:2]

    matrix = cv2.getRotationMatrix2D(
        (w / 2, h / 2),
        angle,
        1.0,
    )

    return cv2.warpAffine(
        image,
        matrix,
        (w, h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REFLECT_101,
    )


# ==========================================================
# Translation
# ==========================================================

def translate(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    h, w = image.shape[:2]

    tx = random.uniform(
        -config.max_translation,
        config.max_translation,
    ) * w

    ty = random.uniform(
        -config.max_translation,
        config.max_translation,
    ) * h

    matrix = np.float32([
        [1, 0, tx],
        [0, 1, ty],
    ])

    return cv2.warpAffine(
        image,
        matrix,
        (w, h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REFLECT_101,
    )


# ==========================================================
# Scaling
# ==========================================================

def scale(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    factor = random.uniform(
        config.min_scale,
        config.max_scale,
    )

    h, w = image.shape[:2]

    matrix = cv2.getRotationMatrix2D(
        (w / 2, h / 2),
        0,
        factor,
    )

    return cv2.warpAffine(
        image,
        matrix,
        (w, h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REFLECT_101,
    )


# ==========================================================
# Brightness
# ==========================================================

def brightness(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    delta = random.uniform(
        -config.brightness_delta * 255.0,
        config.brightness_delta * 255.0,
    )

    result = image.astype(np.float32)

    result += delta

    result = np.clip(result, 0.0, 255.0)

    return result.astype(np.uint8)

# ==========================================================
# Contrast
# ==========================================================

def contrast(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    alpha = random.uniform(
        config.min_contrast,
        config.max_contrast,
    )

    result = image.astype(np.float32)

    result = result * alpha

    result = np.clip(
        result,
        0,
        255,
    )

    return result.astype(np.uint8)


# ==========================================================
# Gamma Correction
# ==========================================================

def gamma(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    image = image.astype(np.uint8)

    gamma_value = random.uniform(
        config.min_gamma,
        config.max_gamma,
    )

    table = np.array(
        [
            ((i / 255.0) ** (1.0 / gamma_value)) * 255.0
            for i in range(256)
        ],
        dtype=np.uint8,
    )

    return cv2.LUT(
        image,
        table,
    )
# ==========================================================
# Gaussian Noise
# ==========================================================

def gaussian_noise(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    noise = np.random.normal(
        0,
        config.noise_std,
        image.shape,
    )

    result = image.astype(np.float32)

    result += noise

    result = np.clip(
        result,
        0,
        255,
    )

    return result.astype(np.uint8)


# ==========================================================
# Motion Blur
# ==========================================================

def motion_blur(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    kernel_size = random.choice(
        [3, 5]
        if config.max_blur_kernel >= 5
        else [3]
    )

    if kernel_size % 2 == 0:
        kernel_size += 1

    kernel = np.zeros(
        (kernel_size, kernel_size),
        dtype=np.float32,
    )

    kernel[kernel_size // 2, :] = 1.0

    kernel /= kernel_size

    return cv2.filter2D(
        image,
        -1,
        kernel,
    )


# ==========================================================
# Perspective Warp
# ==========================================================

def perspective(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    h, w = image.shape[:2]

    margin = config.perspective_scale

    dx = w * margin
    dy = h * margin

    src = np.float32([
        [0, 0],
        [w, 0],
        [w, h],
        [0, h],
    ])

    dst = src + np.float32([

        [
            random.uniform(-dx, dx),
            random.uniform(-dy, dy),
        ],

        [
            random.uniform(-dx, dx),
            random.uniform(-dy, dy),
        ],

        [
            random.uniform(-dx, dx),
            random.uniform(-dy, dy),
        ],

        [
            random.uniform(-dx, dx),
            random.uniform(-dy, dy),
        ],

    ])

    matrix = cv2.getPerspectiveTransform(
        src,
        dst,
    )

    return cv2.warpPerspective(
        image,
        matrix,
        (w, h),
        borderMode=cv2.BORDER_REFLECT_101,
    )


# ==========================================================
# Random Shadow
# ==========================================================

def shadow(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    result = image.astype(np.float32)

    h, w = image.shape[:2]

    x1 = random.randint(0, w)

    x2 = random.randint(0, w)

    mask = np.zeros(
        (h, w),
        dtype=np.float32,
    )

    for y in range(h):

        x = int(
            x1 +
            (x2 - x1) *
            y / h
        )

        mask[y, :x] = 1.0

    if random.random() < 0.5:

        mask = np.fliplr(mask)

    factor = 1.0 - config.shadow_strength

    result[:, :, 0] *= np.where(mask == 1, factor, 1)
    result[:, :, 1] *= np.where(mask == 1, factor, 1)
    result[:, :, 2] *= np.where(mask == 1, factor, 1)

    return np.clip(
        result,
        0,
        255,
    ).astype(np.uint8)


# ==========================================================
# Horizontal Flip
# ==========================================================

def horizontal_flip(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    return cv2.flip(
        image,
        1,
    )


# ==========================================================
# Resize
# ==========================================================

def resize(
    image: np.ndarray,
    config: AugmentationConfig,
) -> np.ndarray:

    image = image.astype(np.uint8)

    return cv2.resize(
        image,
        config.image_size,
        interpolation=cv2.INTER_AREA,
    )