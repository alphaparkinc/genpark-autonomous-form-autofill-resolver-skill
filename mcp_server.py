import json, sys
from client import AutonomousFormAutofillResolverClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "form-autofill-resolver", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "resolve_form_autofill", "description": "Heuristically maps buyer profile to checkout web forms."}]}}
    elif method == "tools/call":
        client = AutonomousFormAutofillResolverClient()
        res = client.resolve_form_autofill()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AutonomousFormAutofillResolverClient()
        print(json.dumps(client.resolve_form_autofill(), indent=2))
