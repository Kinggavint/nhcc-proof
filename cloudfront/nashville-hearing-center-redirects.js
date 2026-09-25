// CloudFront Function: nashville-hearing-center-redirects
// Smart 301s from old WordPress URLs to the new site.
// Runtime: cloudfront-js-2.0, event: viewer-request
//
// Committed here 2026-09-25 (86bbpv5r6) as source of truth - this file did not
// previously exist in git, only as the LIVE CloudFront function. Fetched read-only
// via `aws cloudfront get-function --name nashville-hearing-center-redirects --stage
// LIVE` (ETag at fetch time: E3UN6WX5RRO2AG) and then had the stale
// '/reviews/' -> '/about/' rule removed: /reviews/ is a real page in this repo
// (commit 4044948) and in S3, so the WordPress-era redirect was shadowing it and
// blocking the BreadcrumbList schema verification. Not yet published to LIVE -
// see NEEDS GAVIN in the PR description for the exact update-function command.

function handler(event) {
  var request = event.request;
  var uri = request.uri;

  // Normalize trailing slash - old WordPress URLs always end with /
  if (uri.length > 1 && uri.slice(-1) !== '/' && uri.indexOf('.') === -1) {
    uri = uri + '/';
  }

  var map = {
    // Core pages
    '/about-us/':                                  '/about/',
    '/patient-information/':                       '/patient-info/',
    '/location-contact/':                          '/contact/',
    '/hearing-aid-tips-faq/':                      '/patient-info/',
    '/privacy-policy/':                            '/patient-info/',
    '/hearing-tips/':                              '/blog/',

    // Services family -> /services/
    '/hearing-aid-fittings/':                      '/services/',
    '/hearing-aid-repair/':                        '/services/',
    '/hearing-protection/':                        '/services/',
    '/earwax-removal/':                            '/services/',
    '/tinnitus-relief/':                           '/services/',

    // Hearing aids family -> /services/
    '/best-hearing-aids/':                         '/services/',
    '/best-hearing-aid-brands/':                   '/services/',
    '/hearing-aids-plans-and-pricing/':            '/services/',
    '/over-the-counter-hearing-aids/':             '/services/',
    '/phonak-hearing/':                            '/services/',
    '/in-the-canal-itc-hearing-aids/':             '/services/',
    '/in-the-ear-ite-hearing-aids/':               '/services/',
    '/completely-in-canal-cic-hearing-aids-in-nashville-tn/': '/services/',
    '/best-hearing-aids/in-the-ear-ite-hearing-aids-in-nashville-tn/': '/services/',

    // Hearing loss family -> /hearing-testing/
    '/hearing-loss-causes-symptoms/':              '/hearing-testing/',
    '/conductive-hearing-loss-treatment/':         '/hearing-testing/',
    '/sensorineural-hearing-loss-treatment/':      '/hearing-testing/',

    // Blog posts (WP hearing-loss-articles/*) -> new blog
    '/hearing-loss-articles/the-negative-effects-of-ignoring-hearing-loss/':      '/blog/',
    '/hearing-loss-articles/will-i-get-my-hearing-back-after-an-ear-infection/':  '/blog/',
    '/hearing-loss-articles/early-signs-of-hearing-loss-what-to-watch-for/':      '/blog/',
    '/hearing-loss-articles/early-signs-of-hearing-loss/':                        '/blog/',
    '/hearing-loss-articles/noise-exposure-over-time/':                           '/blog/',
    '/hearing-loss-articles/sudden-hearing-loss/':                                '/blog/',
    '/hearing-loss-articles/dont-dissmiss-early-hearing-loss/':                   '/blog/',
    '/hearing-loss-articles/hearing-loss-and-job-performance/':                   '/blog/',
    '/hearing-loss-articles/ototoxic-medications-and-hearing-loss/':              '/blog/',
    '/hearing-loss-articles/seasonal-hearing-loss/':                              '/blog/',
    '/hearing-loss-articles/hearing-loss-myths/':                                 '/blog/',
    '/hearing-loss-articles/what-is-auditory-fatigue/':                           '/blog/',
    '/hearing-loss-articles/cognitive-hearing-loss/':                             '/blog/',
    '/hearing-loss-articles/ear-buds-and-hearing-loss/':                          '/blog/',
    '/hearing-loss-articles/hearing-aids-and-medicare/':                          '/blog/',
    '/hearing-loss-articles/why-is-tinnitus-louder-at-night/':                    '/blog/',

    // Blog posts (WP hearing-aids-news/*) -> new blog
    '/hearing-aids-news/when-is-it-time-to-update-your-hearing-aids/':                                       '/blog/how-to-properly-clean-your-hearing-aid/',
    '/hearing-aids-news/exploring-and-understanding-each-type-of-hearing-aid/':                              '/blog/',
    '/hearing-aids-news/how-bluetooth-hearing-aids-can-simplify-and-enrich-your-daily-life/':                '/blog/',
    '/hearing-aids-news/blue-tooth-hearing-aids/':                                                           '/blog/',
    '/hearing-aids-news/hearing-aids-and-brain-health/':                                                     '/blog/',
    '/hearing-aids-news/how-to-afford-hearing-aids/':                                                        '/blog/',
    '/hearing-aids-news/how-to-afford-hearing-aids-2/':                                                      '/blog/',
    '/hearing-aids-news/forget-the-bulky-devices-of-the-past-discover-how-modern-discreet-hearing-aids-are-smaller-more-comfortable-and-packed-with-smart-technology/': '/blog/',

    // Tinnitus articles
    '/tinnitus-articles/tinnitus-in-older-adults-whether-its-age-related-and-your-next-steps/': '/blog/',

    // Category landing pages
    '/hearing-loss-articles/':                     '/blog/',
    '/hearing-aids-news/':                         '/blog/',
    '/tinnitus-articles/':                         '/blog/'
  };

  var target = map[uri];
  // A rule pointing at its own path would 301 forever and make the page
  // unreachable (the request never reaches S3). Serve it instead.
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
