import csv
import json
import click

# Command line configuration

@click.command()
@click.option('--inputcsv', help="CSV File to read")
@click.option('--outputdir', help="Directory to write the JSON to")
def readinput(inputcsv, outputdir):
    print(f"Inputcsv: {inputcsv}")
    print(f"Outputdir: {outputdir}")

if __name__ == "__main__":
    readinput()