import json
import unittest
from pathlib import Path


class StudyInputTests(unittest.TestCase):
    def test_domain_references_and_units(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'fixtures/study-input.json').read_text())
        from bed_events.schema import parse_package
        catalog,events=parse_package(data['document'])
        from bed_events.timeline import bed_timeline
        p=data['study']
        for bed in {r['bed'] for r in events.rows}:
            timeline=bed_timeline(catalog,events,bed,p['start'],p['end'],p['known_at'])
            self.assertEqual(sum(r['seconds'] for r in timeline['intervals']),timeline['seconds'])
