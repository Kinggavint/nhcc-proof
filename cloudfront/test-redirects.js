// Run: node cloudfront/test-redirects.js
// Checks the repo redirect function: the new /reviews -> /reviews/ 301,
// /reviews/ served as-is, and that all existing WordPress 301s still work.
const fs = require("fs"), vm = require("vm"), path = require("path");
const src = fs.readFileSync(path.join(__dirname, "nashville-hearing-center-redirects.js"), "utf8");
const sb = {}; vm.createContext(sb); vm.runInContext(src + "\nthis.handler = handler;", sb);
const run = (uri) => sb.handler({ request: { uri, headers: {}, querystring: {} } });
let fail = 0;
const check = (label, ok) => { console.log((ok ? "PASS: " : "FAIL: ") + label); if (!ok) fail++; };
const loc = (r) => r && r.headers && r.headers.location && r.headers.location.value;

let r = run("/reviews");
check("/reviews -> 301 https://nashvillehcc.com/reviews/", r.statusCode === 301 && loc(r) === "https://nashvillehcc.com/reviews/");
r = run("/reviews/");
check("/reviews/ is served (no redirect)", r.statusCode === undefined && r.uri === "/reviews/");
for (const u of ["/", "/about/", "/services/", "/contact/", "/blog/", "/reviews/index.html"]) {
  r = run(u); check(u + " is served (no redirect)", r.statusCode === undefined && r.uri === u);
}
// Every existing map rule, with and without trailing slash, still 301s to the same target.
const map = src.match(/var map = \{([\s\S]*?)\};/)[1];
const rules = [...map.matchAll(/'([^']+)':\s*'([^']+)'/g)];
let ok = 0;
for (const [, from, to] of rules) {
  for (const u of [from, from.replace(/\/$/, "")]) {
    const x = run(u);
    if (x.statusCode === 301 && loc(x) === "https://nashvillehcc.com" + to) ok++;
    else check("legacy " + u + " -> " + to, false);
  }
}
check(`legacy rules: ${ok}/${rules.length * 2} (each with and without slash) still 301 to the same target`, ok === rules.length * 2);
if (fail) { console.error(`\n${fail} check(s) failed.`); process.exit(1); }
console.log("\nAll checks passed.");
