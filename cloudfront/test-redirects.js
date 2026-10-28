// Regression test for cloudfront/nashville-hearing-center-redirects.js
//
// Run: node cloudfront/test-redirects.js
//
// Loads the CURRENT (fixed) function source from this file and asserts that:
//   - /reviews/  no longer 301s (the real reviews page must be served)
//   - /about-us/ still 301s to /about/ (unrelated control rule, must be unaffected)
//
// A second copy of the ORIGINAL live source (with the /reviews/ rule still in
// place) is inlined below so this file can also demonstrate the bug it fixes,
// without depending on network access or a second file on disk.

const fs = require("fs");
const vm = require("vm");
const path = require("path");
const assert = require("assert");

function loadHandler(source) {
  const sandbox = {};
  vm.createContext(sandbox);
  vm.runInContext(source + "\nthis.handler = handler;", sandbox);
  return sandbox.handler;
}

function simulate(handler, uri) {
  const event = { request: { uri, headers: {}, querystring: {} } };
  return handler(event);
}

// --- Fixed version: read straight from this repo file ---
const fixedSource = fs.readFileSync(
  path.join(__dirname, "nashville-hearing-center-redirects.js"),
  "utf8"
);
const fixedHandler = loadHandler(fixedSource);

// --- Original LIVE version (ETag E3UN6WX5RRO2AG at fetch time, 2026-09-25),
//     kept inline so the "before" behavior is reproducible without a live fetch. ---
const originalSource = `
function handler(event) {
  var request = event.request;
  var uri = request.uri;
  if (uri.length > 1 && uri.slice(-1) !== '/' && uri.indexOf('.') === -1) {
    uri = uri + '/';
  }
  var map = {
    '/about-us/':                                  '/about/',
    '/patient-information/':                       '/patient-info/',
    '/location-contact/':                          '/contact/',
    '/reviews/':                                   '/about/',
    '/hearing-aid-tips-faq/':                      '/patient-info/'
  };
  var target = map[uri];
  if (target && target !== uri) {
    return {
      statusCode: 301,
      statusDescription: 'Moved Permanently',
      headers: {
        'location': { value: 'https://nashvillehcc.com' + target },
        'cache-control': { value: 'max-age=86400' }
      }
    };
  }
  return request;
}
`;
const originalHandler = loadHandler(originalSource);

let failures = 0;
function check(label, cond) {
  if (cond) {
    console.log(`PASS: ${label}`);
  } else {
    console.log(`FAIL: ${label}`);
    failures++;
  }
}

// --- Original (live today): /reviews/ redirects away, hiding the real page ---
const origReviews = simulate(originalHandler, "/reviews/");
check(
  "original live source: /reviews/ still 301s to /about/ (the bug)",
  origReviews.statusCode === 301 &&
    origReviews.headers.location.value === "https://nashvillehcc.com/about/"
);

// --- Fixed: /reviews/ must fall through (no redirect object; real request served) ---
const fixedReviews = simulate(fixedHandler, "/reviews/");
check(
  "fixed source: /reviews/ no longer redirects (falls through to origin)",
  fixedReviews && fixedReviews.uri === "/reviews/" && fixedReviews.statusCode === undefined
);

// --- Control: /about-us/ must still redirect to /about/ in BOTH versions ---
const origAboutUs = simulate(originalHandler, "/about-us/");
check(
  "original source: /about-us/ redirects to /about/ (control, unaffected)",
  origAboutUs.statusCode === 301 &&
    origAboutUs.headers.location.value === "https://nashvillehcc.com/about/"
);

const fixedAboutUs = simulate(fixedHandler, "/about-us/");
check(
  "fixed source: /about-us/ still redirects to /about/ (control, unaffected)",
  fixedAboutUs.statusCode === 301 &&
    fixedAboutUs.headers.location.value === "https://nashvillehcc.com/about/"
);

if (failures > 0) {
  console.error(`\n${failures} check(s) failed.`);
  process.exit(1);
} else {
  console.log("\nAll checks passed.");
}
