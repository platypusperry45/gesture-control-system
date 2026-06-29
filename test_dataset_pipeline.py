from recognition.dataset import (
    DatasetBuilder,
    DatasetSplitter,
)

from recognition.dataset.statistics import (
    DatasetStatistics,
)

from recognition.dataset.tensorflow_dataset import (
    TensorFlowDatasetBuilder,
)

print("Building dataset...")

builder = DatasetBuilder()

dataset = builder.build()

print(f"Dataset size: {len(dataset)}")

print("Splitting dataset...")

splitter = DatasetSplitter()

bundle = splitter.split(dataset)

DatasetStatistics.print_summary(bundle)

print("Creating TensorFlow datasets...")

tf_builder = TensorFlowDatasetBuilder()

train_ds, val_ds, test_ds = tf_builder.build(bundle)

print("Done!")

print(train_ds)
print(val_ds)
print(test_ds)
print()

print("Checking one batch...")

for inputs, labels in train_ds.take(1):

    print("Image shape      :", inputs["image"].shape)

    print("Landmarks shape  :", inputs["landmarks"].shape)

    print("Labels shape     :", labels.shape)

    print("Image dtype      :", inputs["image"].dtype)

    print("Landmarks dtype  :", inputs["landmarks"].dtype)

    print("Labels dtype     :", labels.dtype)

    break