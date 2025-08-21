import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

def scan_port(target: str, port: int, timeout: float = 1.0) -> Dict:
    result = {"port": port, "open": False, "service": None}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((target, port))
            result["open"] = True
            try:
                s.settimeout(0.5)
                banner = s.recv(1024).decode(errors="ignore").strip()
                if banner:
                    result["service"] = banner
            except Exception:
                pass
        except (socket.timeout, ConnectionRefusedError):
            pass
        except Exception as e:
            result["error"] = str(e)
    return result

def tcp_scan(target: str, ports: List[int], workers: int = 100) -> Dict:
    results = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(scan_port, target, p): p for p in ports}
        for fut in as_completed(futures):
            results.append(fut.result())
    open_ports = [r for r in results if r.get("open")]
    return {"target": target, "scanned": len(ports), "open_ports": open_ports, "raw": results}

if __name__ == "__main__":
    import sys, json
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    ports = [22, 80, 443, 3306, 8080, 8443]
    out = tcp_scan(target, ports)
    print(json.dumps(out, indent=2))

