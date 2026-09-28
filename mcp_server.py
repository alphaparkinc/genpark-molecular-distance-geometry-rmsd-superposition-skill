"""MCP stdio server for Molecular RMSD Superposition."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import KabschSuperposition

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "compute_rmsd",
                        "description": "Compute RMSD and centroid-aligned superposition between 3D coordinate sets",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "coords_P": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3}
                                },
                                "coords_Q": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3}
                                }
                            },
                            "required": ["coords_P", "coords_Q"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "compute_rmsd":
            P = [tuple(p) for p in args.get("coords_P", [])]
            Q = [tuple(q) for q in args.get("coords_Q", [])]
            res = KabschSuperposition.align_and_rmsd(P, Q)
            return {"jsonrpc": "2.0", "id": req_id, "result": res}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
