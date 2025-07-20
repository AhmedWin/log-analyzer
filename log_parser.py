import argparse
import re
from datetime import datetime

def parse_log(file_path, levels=("ERROR", "CRITICAL", "WARNING")):
    results = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            for level in levels:
                if level in line:
                    results.append((line_number, level, line.strip()))
    return results

def save_results(results, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for line_number, level, line in results:
            f.write(f"[{level}] Line {line_number}: {line}\n")

def display_summary(results):
    print("\n🔍 Summary Report:")
    print(f"Total Matches: {len(results)}")
    levels_found = {}
    for _, level, _ in results:
        levels_found[level] = levels_found.get(level, 0) + 1
    for level, count in levels_found.items():
        print(f" - {level}: {count} entries")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log File Analyzer for Error & Critical Events")
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument("-o", "--output", help="Optional output file to save results")
    args = parser.parse_args()

    matches = parse_log(args.logfile)

    if matches:
        print(f"\nFound {len(matches)} important log entries:")
        for line_number, level, line in matches:
            print(f"[{level}] Line {line_number}: {line}")
        display_summary(matches)

        if args.output:
            save_results(matches, args.output)
            print(f"\n✅ Results saved to: {args.output}")
    else:
        print("\n✅ No ERROR or CRITICAL logs found.")
