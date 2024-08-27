# Protocol mapping based on protocol numbers from 'Assigned Internet Protocol Numbers'
PROTOCOL_MAP = {
    "1": "icmp",
    "6": "tcp",
    "17": "udp"
}

# Function to load the lookup table from a CSV file
def load_lookup_table(file_path):
    lookup_table_map = {}
    with open(file_path, "r") as lookup_table:
        for row in lookup_table.readlines():
            row = row.split(',')
            destination_port = row[0]
            protocol_name = row[1]
            # Convert tag to lower - case insensitive
            tag = row[2].strip('\n').lower()

            lookup_table_key = destination_port + '+' + protocol_name
            lookup_table_map[lookup_table_key] = tag
    return lookup_table_map

# Function to parse flow logs and generate tag and port/protocol counts
def parse_flow_logs(log_file, lookup_table_map):
    tag_count_map = {}
    port_protocol_count_map = {}

    with open(log_file, "r") as file:
        for log in file.readlines():
            log = log.split()
            destination_port = log[6]
            protocol_number = log[7]
            # Convert protocol name to lower - case insensitive
            protocol_name = PROTOCOL_MAP.get(protocol_number).lower()

            # Store port/protocol combination count
            port_protocol_count_key = destination_port + '+' + protocol_name
            if port_protocol_count_key in port_protocol_count_map:
                port_protocol_count_map[port_protocol_count_key] += 1
            else:
                port_protocol_count_map[port_protocol_count_key] = 1

            # Store tag count
            lookup_table_key = destination_port + '+' + protocol_name
            tag = lookup_table_map.get(lookup_table_key, 'Untagged')

            if tag in tag_count_map:
                tag_count_map[tag] += 1
            else:
                tag_count_map[tag] = 1

    return tag_count_map, port_protocol_count_map

# Function to write the output to a file
def write_output(tag_count_map, port_protocol_count_map, output_file):
    with open(output_file, 'w') as output:
        output.write("Tag Counts:\n")
        output.write("Tag,Count\n")
        for tag, count in tag_count_map.items():
            output.write(f"{tag},{count}\n")

        output.write("\n\n")

        output.write("Port/Protocol Combination Counts:\n")
        output.write("Port,Protocol,Count\n")
        for key, count in port_protocol_count_map.items():
            port, protocol = key.split('+')
            output.write(f"{port},{protocol},{count}\n")

# Main function to run the process
def main():
    # File paths
    lookup_table_file = "lookup_table.csv"
    flow_logs_file = "flow_logs.txt"
    output_file = "output.txt"

    # Load lookup table
    lookup_table_map = load_lookup_table(lookup_table_file)

    # Parse flow logs and get counts
    tag_count_map, port_protocol_count_map = parse_flow_logs(flow_logs_file, lookup_table_map)

    # Write the counts to the output file
    write_output(tag_count_map, port_protocol_count_map, output_file)

# Entry point for the script
if __name__ == "__main__":
    main()





    


