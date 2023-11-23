# nextflow_docker_pipeline
An example of a nexflow pipeline using python scritping. 

## Dependencies 

* Unix-like operating system (Linux, Solaris, OS X, etc)
* Java 7 or 8 
* WSL if using windows
* Docker

## Get started

Install Nextflow by copying and pasting the following snippet in your shell terminal: 

    curl -fsSL get.nextflow.io | bash

It will download the `nextflow` application launcher in your working directory. 
When done, you may want to complete the installation moving the `nextflow` executable 
into a directory in your `$PATH` variable.

To run the pipeline ensure you have bam and bed files in the data/input file and run the following command:

    nexflow run main.nf

This will pull a docker container with the required packages and automatically run 
the data from the input folder.
The code is made to get the product of all bam and bed files in the folder so if 
you had 2 bam and 2 bed you will end up with 2 fasta files and 2 bed files at the end.
if all the bed files only contained one region that is! 

Each fasta is created based on a line in the bed file so you could end up with a lot of files
but each will have a unique name. 

## Running tests

To run the simple tests I've created you need to create a virtual enviroment. To do this do the following:

* Run 
    pipenv shell
* Run pipenv 
    pipenv install -r requirements.txt
* Finally run 
     python -m pytest


# Outputs:

The outputs of this code are the following:

* A sorted bam file for each bam input
* A indexed filed for each sorted bam file.
* A json with counts for each region
* A fasta file for all sequences aligned to the regions mentioned in the bed file. 

