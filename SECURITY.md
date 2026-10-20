# Network, privacy and security

## Current transport: plaintext LAN

Current LAN mode intentionally uses HTTP/WebSocket on local IPv4, without TLS or certificate installation. Text and pairing credentials can be observed or altered by an attacker on the same network. Pairing, revocation, Origin/Host checks and one-controller rules are useful access controls, but do not provide transport encryption or cryptographic receiver authentication.

Use only a trusted private network. Do not expose ports8765/8766 to the public Internet, add router port forwarding, or use it to type sensitive passwords. A saved receiver ID prevents some accidental IP reuse, not active impersonation.

## What devices can see

The tablet, operating system, input method and app/browser necessarily handle text entered there. The privacy-input switch masks the local field and requests reduced input learning; it cannot make an untrusted tablet safe for secret entry.

Mac credentials and pairing records are stored under the current user's local Application Support directory, outside this repository. APK credentials use AndroidKeyStore-backed storage. Do not publish real QR codes, pairing links, cookies, logs containing input, local-admin capabilities or signing keys.

## Permissions and control

Mac input needs Accessibility permission for the launching terminal/application. Android camera permission is requested for local QR scanning; the bundled decoder works offline. Standard Bluetooth HID support varies by Android version and ROM.

Loss of connection/background/timeout cancels active input and releases held buttons. These safeguards are implementation behavior, not a guarantee against every device/OS/network failure.

## Reporting a problem

Do not post exploit details, live credentials or private logs in a public Issue. Until a private reporting channel is configured, contact the repository owner through an available private channel first. General non-sensitive reproduction steps may be reported publicly.
