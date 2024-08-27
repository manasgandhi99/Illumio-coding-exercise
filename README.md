# Illumio Coding Exercise - Flow Log Analysis Script

## Overview

This Python script processes flow log data and maps tags using a lookup table. It counts occurrences of tags and port/protocol combinations, generating a summary output.

## Assumptions

- Input files are plain text (ASCII) files.
- Flow log file size can be up to 10 MB.
- The lookup file can have up to 10,000 mappings.
- Tags can map to more than one port/protocol combination.
- Matches should be case-insensitive.
- The protocol numbers used in the flow logs are translated into protocol names based on the official list maintained by the Internet Assigned Numbers Authority (IANA) and stored in the 'PROTOCOL_MAP'. The full list of protocol numbers and their corresponding names can be found here: [IANA Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
- Tag count and port/protocol combination count are stored in `output.txt`.


## Requirements

- Python 3.x
- The `lookup_table.csv` and `flow_logs.txt` files should be in the same directory as the script.

## Instructions

1. **Install Python 3**: Ensure Python 3 is installed on your system. If `python3` doesn't work, try using `python` instead, depending on your system configuration.

2. **Prepare Input Files**:
   - `lookup_table.csv`: Contains mappings between destination ports, protocol names, and tags.
   - `flow_logs.txt`: Contains flow log entries with destination ports and protocol numbers.

3. **Run the Script**:
   ```bash
   python3 solution.py

## Tests Conducted

### Basic Functional Test
Tested with sample flow log data and lookup table provided in the problem statement to ensure correct mapping and counting.

### Case Insensitivity Test
Tested with varied cases (e.g., "TCP", "tcp") in the lookup table and flow logs to confirm that matches are case-insensitive.

### Empty Lookup Table
Tested with an empty lookup table to ensure that all flow logs are tagged as "Untagged".

### Large Input Files
Tested with larger flow logs and lookup tables to confirm the script handles up to 10 MB of log data and 10,000 lookup mappings without performance issues.

## Error Handling

### Invalid Protocol Numbers
The flow log contains protocol numbers not listed in the protocol map (e.g., "99").

### Special Characters in Tags
Tags in the lookup table contain special characters or whitespace.

### No Matching Records
The `flow_logs.txt` file contains records that do not match any entries in the `lookup_table.csv`.

### Large Lookup Table with Duplicates
The `lookup_table.csv` contains duplicate entries for the same port/protocol combination.

### Large Flow Log with Multiple Tags
The `flow_logs.txt` file has a large number of entries with varying tags.

### Empty Files
Both `flow_logs.txt` and `lookup_table.csv` files are empty.

## Basic Analysis

### Performance
The program efficiently parses flow logs and maps tags using a dictionary lookup, ensuring fast execution even with large input files.

### Modularity
The code is organized into functions (`load_lookup_table`, `parse_flow_logs`, `write_output`), promoting readability and maintainability.

### Error Handling
The program includes basic error handling for missing or unmatched tags, categorizing them as "Untagged."




