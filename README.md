# Random Python Utilities

This repository contains a set of short Python scripts which I use to automate some of my tasks. You are free to use them if you want, but I give no guarantees of them working on your system, as they are first and foremost tailored for my use. You are however free to look at the code and fix any issues yourself or to let me know about them in the GitHub Issues section. That said I don't promise on fixing them.

Licensed under MIT license.

## generate_qiime_manifest.py

`generate_qiime_manifest.py` is a simple command-line utility for generating meanifest files for qiime2. 

#### Example

```
$ ./generate_qiime_manifest.py ./directory_with_fastq_files/*.fastq
```
will generate a manifest for all fastq files in `directory_with_fastq_files` and print the result to stdout.

For more options use:
```
$ ./generate_qiime_manifest.py --help
```

## ects.py

`ects.py` calculates a number of ECTS points of subjects given a csv file with subject names and number of their ects points.

#### Example

```
$ ./ects.py ./subjects.csv
```
will simply calculate the sum of ECTS points for all subjects in a file.

For more options use:
```
$ ./ects.py --help
```

## TODO
 - maybe some tests 🤔
