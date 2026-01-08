#!/usr/bin/env ruby
# Script to parse TextMe app SMS transaction logs
# Extracts sender, receiver, and flags from log entries

# Get the log line from command line argument
log_line = ARGV[0]

# Regular expression to match the pattern:
# [from:SENDER] [to:RECEIVER] [flags:FLAGS]
# Use scan to extract all three groups at once
matches = log_line.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# Output in format: SENDER,RECEIVER,FLAGS
if matches && matches[0]
  sender = matches[0][0]
  receiver = matches[0][1]
  flags = matches[0][2]
  puts "#{sender},#{receiver},#{flags}"
end
