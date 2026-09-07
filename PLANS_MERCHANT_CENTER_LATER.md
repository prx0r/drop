# Plans for Later — Merchant Center Integration

*Created: 2026-09-07*
*Status: QUEUED — Not blocking current work*

---

## What We Have

| Credential | Value | Status |
|------------|-------|--------|
| Merchant Center ID | 5849184805 | Working |
| Merchant Email | idonietaS@gmail.com | Working |
| Google Ads Customer ID | 3775149829 | Working |
| Developer Token | Z5PRn4Hra3... | Working |
| Refresh Token | Working | Working |

---

## What Needs to Be Done

### 1. Enable Content API for Shopping
- Go to https://console.developers.google.com/apis/api/shoppingcontent.googleapis.com/overview?project=326625299811
- Click "Enable"
- Wait 2-3 minutes

### 2. Create New Merchant Center Accounts
Each niche gets its own account:
- hyttekomponenter.no (Norwegian balcony-door)
- reservedeler.fi (Finnish heat-pump)
- nordicparts.com (multi-niche)

### 3. Build Product Feed
- Use Feedify or direct CSV
- Fill conversational attributes
- Submit to Merchant Center

### 4. Test API Interaction
- List accounts
- Upload products
- Check feed status
- Fix disapprovals

---

## Priority

**Not blocking current work.**

Current priority: Build the balcony-door subgraph in voiceagent, deploy to Cloudflare, test with real queries.

Merchant Center integration comes after the subgraph is working.

---

## Commands (for later)

```bash
# Enable API (manual step in console)
# Then test:
python3 -c "
import subprocess
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

creds = Credentials(
    token=None,
    refresh_token=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_REFRESH_TOKEN', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
    token_uri='https://oauth2.googleapis.com/token',
    client_id=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLIENT_ID', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
    client_secret=subprocess.run(['agent-vault', 'vault', 'credential', 'get', 'GOOGLE_CLIENT_SECRET', '--vault', 'oracle'], capture_output=True, text=True).stdout.strip(),
)
creds.refresh(Request())

# Test Merchant Center API
headers = {'Authorization': f'Bearer {creds.token}', 'Content-Type': 'application/json'}
url = 'https://shoppingcontent.googleapis.com/content/v2.1/5849184805/accounts/5849184805'
response = requests.get(url, headers=headers)
print(f'Status: {response.status_code}')
"
```
