# Catholic Compass 1.0 — installable phone test

**Status:** Pre-release testing only. Do not publish as a public launch until QA and parish data checks are finished.

## 1. Build the Flutter web app on your Mac

Open the **CatholicCompass-1.0** project in VS Code. In its Terminal, run:

```sh
flutter pub get
flutter build web --release --no-web-resources-cdn
```

The built site will appear in the project's `build/web` folder. Do **not** upload `lib`, `pubspec.yaml`, or the entire Flutter project as the website: Cloudflare needs the compiled `build/web` assets.

If you need to verify the result on your Mac before deploying:

```sh
cd build/web
python3 -m http.server 8090
```

Then open http://localhost:8090 . Press Ctrl+C to stop the test server.

## 2. Create temporary HTTPS hosting (free tier)

Visit https://dash.cloudflare.com/ and sign in / create a free account. Open **Workers & Pages** and choose **Create application** then **Pages / Drag and drop your files** (the UI wording may change). Use a project name such as `catholic-compass-test`.

Drag the **`build/web` folder** into the upload area, **not** the full source project. Click **Deploy site**. Cloudflare will provide a URL ending in `.pages.dev` over HTTPS.

Keep this URL for testing; do not purchase a domain yet. On Direct Upload projects, future releases require another deployment; they're not connected to GitHub automatically.

## 3. Test on iPhone

Open the HTTPS `.pages.dev` URL in **Safari**. Tap **Share** → **Add to Home Screen** (or **Open as Web App** / **Add** as offered). Launch Catholic Compass using its new home-screen icon.

## 4. Test on Android

Open the HTTPS URL in **Chrome**. Open the menu and choose **Install app** or **Add to Home screen**, then launch the installed icon.

## 5. Test checklist

- [ ] Home page loads without a desktop browser address bar when launched from the installed icon.
- [ ] Bible Journey screens fit on the phone; no sideways scrolling or clipped navigation.
- [ ] Quiz scoring records a wrong first answer correctly; replay does not award a perfect result.
- [ ] XP and Bible Journey progress persist after fully closing and reopening the app.
- [ ] Find Your Parish works for `37110`, `Madison`, `Memphis`, `Green Bay` and `Eau Claire`.
- [ ] Parish **Visit Website** opens the appropriate verified destination; **Directions** opens a separate map.
- [ ] Manual **Check for Updates** works; currently published directory version should be at least 12.
- [ ] After using the app online, put the phone into airplane mode and relaunch. Record which screens load offline; don't assume every screen or image is cached.
- [ ] Turn Wi-Fi back on and verify normal operation resumes.

## 6. Important before launch

- The parish directory remains incomplete; counts and available websites are not proof of complete statewide coverage.
- The app's existing offline service worker uses best-effort runtime caching: this is **not yet proof** all Bible Journey screens are reliably available offline.
- Do not test PWA install by typing the Mac's `localhost` URL into a phone: on a phone, `localhost` refers to that phone. HTTPS hosting is the straightforward path.
- Avoid publishing private keys; the parish data repository is public.
- The app is free to users. Cloudflare Pages has a free tier subject to service limits; custom domain purchase is optional.
- Confirm any Bible text and artwork redistribution rights before opening the site to the public.

## QA results

Paste the final `.pages.dev` URL and notes about what passed/failed here after your first test. Keep this document as a checklist for release readiness.
