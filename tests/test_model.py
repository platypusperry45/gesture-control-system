"""
Test the complete Gesture Recognition Model.

Verifies:

1. Imports
2. Model construction
3. Forward pass
4. Output shape
5. Model summary
"""

import tensorflow as tf

from recognition.network import GestureRecognitionModel


def main():

    print("=" * 60)
    print("Creating model...")
    print("=" * 60)

    model = GestureRecognitionModel.build_model(
        num_classes=6,
    )

    print("\nModel created successfully.\n")

    model.summary()

    print("\n" + "=" * 60)
    print("Creating dummy batch...")
    print("=" * 60)

    dummy_inputs = {

        "image": tf.random.uniform(
            (
                4,
                224,
                224,
                3,
            ),
            dtype=tf.float32,
        ),

        "landmarks": tf.random.uniform(
            (
                4,
                63,
            ),
            dtype=tf.float32,
        ),
    }

    print("Image shape      :", dummy_inputs["image"].shape)
    print("Landmarks shape  :", dummy_inputs["landmarks"].shape)

    print("\n" + "=" * 60)
    print("Running forward pass...")
    print("=" * 60)

    outputs = model(
        dummy_inputs,
        training=False,
    )

    print("Output shape :", outputs.shape)

    print("Output dtype :", outputs.dtype)

    print("\nPredictions:")

    print(outputs.numpy())

    print("\nPredicted class indices:")

    print(tf.argmax(outputs, axis=1).numpy())

    print("\nProbability sums:")

    print(tf.reduce_sum(outputs, axis=1).numpy())

    print("\n")

    if outputs.shape == (4, 6):

        print("✓ Output shape is correct.")

    else:

        print("✗ Incorrect output shape.")

    print("\nModel test completed successfully.")


if __name__ == "__main__":

    main()