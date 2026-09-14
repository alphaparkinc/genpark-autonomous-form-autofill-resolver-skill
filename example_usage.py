import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AutonomousFormAutofillResolverClient

def main():
    client = AutonomousFormAutofillResolverClient()
    res = client.resolve_form_autofill()
    print("=== Autonomous Form Autofill Resolver Output ===")
    print(f"Status: {res['status']} ({res['matched_fields_count']}/{res['total_fields']} Fields Matched)")
    print("\nField Assignments:")
    for f in res['field_assignments']:
        print(f"  - [{f['field_name']}] -> '{f['autofill_value']}' (Confidence: {f['confidence']})")

if __name__ == '__main__':
    main()
