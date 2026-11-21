#!/usr/bin/env python3
"""Check transcribed paper/preprint arithmetic, not raw experimental records."""
import json
from fractions import Fraction as F
from pathlib import Path


def main():
    pdf_count = {'instances': 102, 'passes': 103}
    preprint_count = {'instances': 103, 'passes': 102, 'failures': 1}
    assert pdf_count['passes'] > pdf_count['instances']
    assert preprint_count['passes'] + preprint_count['failures'] == preprint_count['instances']
    assert round(preprint_count['passes']/preprint_count['instances']*100, 1) == 99.0
    basic_instances, basic_passes = 232, 224
    assert basic_instances-basic_passes == 8
    # Illustrative packing only: assumes first ten chronological files are the
    # ten fault-free calibration files; no actual file metadata were inspected.
    basic_full, basic_rem = divmod(474-10, 2)
    extended_full, extended_rem = divmod(420-10, 4)
    assert (basic_full, basic_rem, extended_full, extended_rem) == (232, 0, 102, 2)
    assert F(1769) - F(1766) == 3
    # If P lies between A and B, subtract the projected A distance from A-B.
    conditional_b_projection = F('195.1') - F('92.8')
    assert conditional_b_projection == F('102.3')
    result = {'scope': 'Arithmetic of transcribed statements; no raw-data replay, proof, uncertainty propagation, or demonstrated correction.',
              'supplied_pdf_extended': pdf_count, 'preprint_v2_extended': preprint_count,
              'preprint_extended_percent': 100*102/103, 'basic_percent': 100*224/232,
              'hypothetical_packing_assuming_first_10_are_calibration': {
                  'basic_full_2file_instances': basic_full, 'basic_remaining_files': basic_rem,
                  'extended_full_4file_instances': extended_full, 'extended_remaining_files': extended_rem},
              'v2_table_reported_arrivals_ns': [1766, 1769], 'table_nominal_b_minus_a_ns': 3,
              'v2_narrative_b_minus_a_ns': 9,
              'conditional_between_station_B_projection_m': str(conditional_b_projection)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
