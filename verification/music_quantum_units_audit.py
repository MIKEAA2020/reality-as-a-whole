#!/usr/bin/env python3
"""Check specific music/unit comparisons; no inference to ontology or music preference."""
from fractions import Fraction as F
from math import log2
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
# Exact SI numerical values in J s and J respectively (BIPM).
h = F(662607015, 10**8) * F(1, 10**34)
ev = F(1602176634, 10**9) * F(1, 10**19)
f_ev = ev / h  # cycles per second
assert F(2417989,10**6)*10**14 < f_ev < F(2417990,10**6)*10**14

# Article's reference: 880 Hz shifted up 38 octaves, or 440*2^39.
f_440 = F(880)*2**38
assert f_440 == F(440)*2**39
folded_ev = f_ev/2**39
folded_mev = (f_ev/1000)/2**29
assert folded_mev/folded_ev == F(128,125)
assert folded_ev != 440
comma = F(3**12, 2**19)
assert comma > 1
result = {
    'scope': 'Arithmetic in declared units and tuning convention only; no empirical judgment, experiential identity, quantum-gravity result, or metaphysical conclusion.',
    'h_J_s_exact': '6.62607015e-34', 'one_eV_J_exact': '1.602176634e-19',
    'one_eV_over_h_Hz': float(f_ev), 'article_880_times_2_to_38_Hz': int(f_440),
    'article_reference_relative_error_percent': float(100*(f_440/f_ev - 1)),
    'folded_one_eV_at_39_octaves_Hz': float(folded_ev),
    'one_eV_relative_to_A440_cents': 1200*log2(float(folded_ev/440)),
    'folded_one_meV_at_29_octaves_Hz': float(folded_mev),
    'one_meV_relative_to_A440_cents': 1200*log2(float(folded_mev/440)),
    'meV_vs_eV_folded_ratio': str(folded_mev/folded_ev),
    'pythagorean_comma_exact': str(comma), 'pythagorean_comma_cents': 1200*log2(float(comma)),
    'caveat': '1 eV and 1 meV denote different physical energies; changing the unit does not alter a fixed energy. Neither approximate coincidence establishes a physical law.'
}
(ROOT / 'verification/music_quantum_units_audit.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
