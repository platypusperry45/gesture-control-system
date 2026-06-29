"""
Entry point for the Dataset Validator.

Run:

python -m recognition.validator
"""

from .validator import DatasetValidator
from .report import ReportPrinter


def main():

    print()

    print("Scanning dataset...")

    validator = DatasetValidator()

    report = validator.validate()

    ReportPrinter.print(report)


if __name__ == "__main__":

    main()