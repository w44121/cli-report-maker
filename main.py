from core.cli import cli
from core.parsers import CSVParser
from core.reports import ReportFactory


def main():
    cli_args = vars(cli.parse_args())
    for file_path in cli_args.get("file path"):
        data = CSVParser(file_path).parse()
        report = ReportFactory().get_report(cli_args.get("report"), data)
        report.grouping()
        report.execute()


if __name__ == "__main__":
    main()
