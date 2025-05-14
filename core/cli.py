import argparse as ap


cli = ap.ArgumentParser(
    prog="cli reporter",
    description="script for parsing data from csv files and subsequent report generation",
)

cli.add_argument("file path", nargs="+", help="file path")
cli.add_argument(
    "-r", "--report", type=str, help="select report type", default="payout"
)
