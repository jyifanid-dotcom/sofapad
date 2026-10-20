# SofaPad

Use a tablet or phone as a Mac touchpad, keyboard and Touch Bar-style shortcut strip. Android supports an APK; iPhone and iPad use the browser. It works with a Mac mini connected to a TV, a MacBook, or another Mac.

![Living-room concept](living-room-vibe-coding.png)

AI-generated scenario illustration. Actual software UI uses the shared browser/APK page:

![Actual isolated UI demo](software-demo.gif)

![Dot-matrix ripple animation](dot-matrix-ripple.gif)

Actual renderer sampled with synthetic touch points. No personal device data or input content is shown.

[Download the complete buildable source ZIP](SofaPad-0.4.17-public-source.zip?raw=1). This web publication contains documentation, media and installers; full source directories and workflows are inside the archive.

## What is available

- Android APK: LAN HTTP/WebSocket or standard Bluetooth HID, depending on device/ROM support.
- iPhone/iPad: browser interface. There is no native iOS application.
- Mac: Python3 receiver, standard library and macOS frameworks, Accessibility permission required.
- Pointer/tap/double-tap drag, two-finger right click, scrolling/inertia, LAN continuous magnification where supported, Bluetooth shortcut zoom, three/four-finger shortcut gestures and screenshot/volume/lock controls.

Current test version:0.4.17. The LAN transport is intentionally plaintext and requires a trusted private network; do not use it for sensitive passwords. Bluetooth Unicode injection and Apple's native Force Touch/Taptic hardware are not provided. Automatic reconnection and long-duration hardware/network behavior remain under testing.

Kindle/e-ink readers are an experimental possibility, not a tested compatibility claim. A usable browser needs the required JavaScript, WebSocket and touch-event capabilities; opening a web page is insufficient.

## Try it

[Android APK](SofaPad-0.4.17-test.apk?raw=1) · [Mac receiver](SofaPad-Mac-0.4.17.zip?raw=1) · [Chinese getting-started guide](GETTING_STARTED.md) · [Full gesture guide](GESTURES.md)

The repository also shares five hardware concept images, dimensioned orthographic/section/exploded studies, an A3 vector PDF and scripts: [hardware concept](HARDWARE.md). They are not manufacturing-ready plans, nor an Apple announcement or affiliation.

Python + Java + HTML/CSS/JavaScript, not Rust. MIT for original project source; third-party MIT/Apache-2.0 notices retained. See [SECURITY](SECURITY.md), [development](DEVELOPMENT.md) and [media provenance](MEDIA.md).
