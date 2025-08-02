#!/usr/bin/env python3
# Adds confidence tags to ORAC output

def tag_confidence(output_text, confidence_level):
    levels = ['HIGH', 'MEDIUM', 'LOW']
    if confidence_level not in levels:
        raise ValueError(f"Invalid confidence level: {confidence_level}")
    return f"[{confidence_level}] {output_text}"

if __name__ == "__main__":
    sample = "System analysis complete."
    print(tag_confidence(sample, 'HIGH'))
