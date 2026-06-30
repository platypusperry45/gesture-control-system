"""
TensorFlow Dataset Builder.

Converts DatasetBundle objects into tf.data.Dataset pipelines.
"""

from __future__ import annotations
import numpy as np
import tensorflow as tf

from recognition.training.augmenter import Augmenter
from recognition.training.config import AugmentationConfig

from .models import DatasetSplit


class TensorFlowDatasetBuilder:
    """
    Builds TensorFlow datasets from DatasetBundle.
    """

    def __init__(
        self,
        image_size: tuple[int, int] = (224, 224),
        batch_size: int = 32,
        shuffle_buffer: int = 1000,
        cache: bool = True,
        augment: bool = True,
    ):

        self.image_size = image_size

        self.batch_size = batch_size

        self.shuffle_buffer = shuffle_buffer

        self.cache = cache

        self.augment = augment

        self.augmenter = Augmenter(
            AugmentationConfig()
        )

    # =====================================================
    # Image Loading
    # =====================================================

    def _load_image(
        self,
        path: tf.Tensor,
    ) -> tf.Tensor:

        image = tf.io.read_file(path)

        image = tf.image.decode_png(
            image,
            channels=3,
        )

        image = tf.image.resize(
            image,
            self.image_size,
        )

        image = tf.cast(
            image,
            tf.float32,
        )

        image /= 255.0

        return image

    # =====================================================
    # Parse One Sample
    # =====================================================

    def _parse_sample(
        self,
        image_path: tf.Tensor,
        landmarks: tf.Tensor,
        label: tf.Tensor,
    ):

        image = self._load_image(
            image_path,
        )

        return (

            {
                "image": image,
                "landmarks": landmarks,
            },

            label,

        )

    # =====================================================
    # Build One Split
    # =====================================================

    def _build_split(
        self,
        split: DatasetSplit,
    ) -> tf.data.Dataset:

        image_paths = [

            str(sample.image_path)

            for sample in split.samples

        ]

        landmarks = [

            sample.landmarks

            for sample in split.samples

        ]

        labels = [

            sample.label

            for sample in split.samples

        ]

        dataset = tf.data.Dataset.from_tensor_slices(

            (

                image_paths,

                landmarks,

                labels,

            )

        )

        dataset = dataset.map(

            self._parse_sample,

            num_parallel_calls=tf.data.AUTOTUNE,

        )

        return dataset
    
    def _augment_numpy(
        self,
        image,
    ):
        """
        Runs OpenCV augmentation on uint8 images.
        Called through tf.py_function.
        """

        image = image.numpy()

        # Convert from normalized float32 [0,1] to uint8 [0,255]
        image = (image * 255.0).astype(np.uint8)

        image = self.augmenter(image)

        # Convert back to normalized float32
        image = image.astype(np.float32) / 255.0

        return image
    
    def _augment_tf(
        self,
        inputs,
        label,
    ):
        """
        TensorFlow wrapper around the OpenCV augmenter.
        """

        image = tf.py_function(

            func=self._augment_numpy,

            inp=[inputs["image"]],

            Tout=tf.float32,

        )

        image.set_shape(

            (
             self.image_size[0],
             self.image_size[1],
             3,
            )

        )

        return (

        {

            "image": image,

            "landmarks": inputs["landmarks"],

        },

        label,

    )

    def _prepare_dataset(
        self,
        dataset: tf.data.Dataset,
        *,
        training: bool,
    ) -> tf.data.Dataset:
       """
       Applies the standard TensorFlow dataset pipeline.
       """

       if training:

        dataset = dataset.shuffle(
            self.shuffle_buffer,
        )

       if training and self.augment:

        dataset = dataset.map(

            self._augment_tf,

            num_parallel_calls=tf.data.AUTOTUNE,

        )

       if self.cache:

        dataset = dataset.cache()

        dataset = dataset.batch(
            self.batch_size,
        )

        dataset = dataset.prefetch(
            tf.data.AUTOTUNE,
        )

       return dataset
    
    # =====================================================
    # Public API
    # =====================================================

    def build(
        self,
        split: DatasetSplit,
        *,
        training: bool = False,
    ) -> tf.data.Dataset:
        """
        Builds a TensorFlow dataset for a single split.
        """

        dataset = self._build_split(
            split,
        )

        dataset = self._prepare_dataset(
            dataset,
            training=training,
        )

        return dataset
    
    @property
    def input_shape(
        self,
    ):

      return (

            self.image_size[0],

            self.image_size[1],

            3,

        )
    @property
    def image_height(
        self,
    ):

        return self.image_size[0]


    @property
    def image_width(
        self,
    ):

        return self.image_size[1]