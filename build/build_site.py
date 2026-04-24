#!/usr/bin/env python3
"""Build every NHCC page. Run: python3 build/build_site.py"""
from __future__ import annotations
import json
from pathlib import Path
from render import (
    write_page, render_wave, asset, PHONE, PHONE_TEL,
    ADDRESS_L1, ADDRESS_L2, EMAIL, BUSINESS, BUSINESS_SHORT, OWNER, CANONICAL_BASE, NAV, OUT
)

IMG  = lambda d, n: asset(d, f"assets/images-webp/{n}")
ICON = lambda d, n: asset(d, f"assets/icons/{n}")
PG   = lambda d, p: asset(d, p)

# =========================================================
# HOME
# =========================================================
def build_home():
    d = 0
    hero_bg = IMG(d, "hero_0000_ave-calvar-4ixi6kpRyaQ-unsplash.webp")
    success = [
      ("icon-one.svg",  "Understand & enjoy conversations again"),
      ("icon-two.svg",  "Reconnect with family, friends & colleagues"),
      ("icon-three.svg","Improve your mental & emotional health"),
    ]
    services = [
      ("icon-five.svg","Hearing<br>enhancement","Hearing devices that fit your lifestyle and any level of hearing"),
      ("icon-four.svg","Hearing aid<br>verification","Real-ear measurements to fit your device to your exact hearing needs"),
      ("icon-six.svg", "Transparent<br>pricing","Itemized pricing so you know exactly what you're paying for"),
    ]
    steps = [
      ("one-icon.svg","1. Schedule your appointment",
        "During your appointment, we'll measure how your hearing system is working and complete a full communication needs assessment."),
      ("two-icon.svg","2. We'll present your options",
        "Based on your testing, choose from our recommended device options or get your current hearing aids recalibrated for a better fit."),
      ("three-icon.svg","3. Enhance your hearing & enjoy your life",
        "Once your device orientation is complete, you'll be able to enjoy improved communication and connection in any setting."),
    ]

    success_html = "".join(f"""
      <div class="col-md-4">
        <div class="success_box" data-aos="fade">
          <img src="{ICON(d,i)}" alt="" width="80" height="80">
          <h3>{t}</h3>
        </div>
      </div>""" for i,t in success)

    services_html = "".join(f"""
      <div class="col-md-6 col-lg-4">
        <div class="service_box" data-aos="fade-right">
          <img src="{ICON(d,i)}" alt="" width="80" height="80">
          <h3>{t}</h3>
          <p>{c}</p>
        </div>
      </div>""" for i,t,c in services)

    steps_html = "".join(f"""
      <div class="col-md-6 col-lg-4">
        <div class="steps_box" data-aos="fade-up">
          <img src="{ICON(d,i)}" alt="" width="90" height="90">
          <div class="steps_box_inner">
            <h3>{t}</h3>
            <p>{c}</p>
          </div>
        </div>
      </div>""" for i,t,c in steps)

    body = f"""
<main id="primary" class="site-main">

  <section class="hero" style="background-image:url('{hero_bg}');">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-10">
          <div class="hero_content">
            <h1 data-aos="fade">Adult Audiologist in Nashville, TN</h1>
            <h2 data-aos="fade">Amplify your hearing,<br>amplify your life.</h2>
            <a class="btn schedule_btn" href="{PG(d,'appointment/')}">Schedule Appointment</a>
          </div>
        </div>
      </div>
    </div>
    {render_wave()}
  </section>

  <section class="success_wrap" aria-label="What you'll gain with care">
    <div class="container">
      <div class="row justify-content-center">{success_html}</div>
    </div>
  </section>

  <section class="half_wrap half_wrap_full" aria-label="Does this sound familiar?">
    <div class="row g-0 justify-content-between align-items-center">
      <div class="col-md-6 col-lg-5" data-aos="fade">
        <img src="{IMG(d,'sq_0005_raj-rana-WENBRUAh7W8-unsplash.webp')}" alt="Two people talking over coffee — conversations feel better with healthy hearing">
      </div>
      <div class="col-md-6 col-lg-7">
        <div class="half_wrap_box" data-aos="fade">
          <h3>Does this sound familiar?</h3>
          <ul>
            <li>“I find myself avoiding large gatherings because I can't hear what others are saying, especially when there's background noise.”</li>
            <li>“I constantly have to ask people to repeat themselves. But sometimes I don't even bother because it's embarrassing.”</li>
            <li>“I'm exposed to loud noises for long periods of time, sometimes without good ear protection.”</li>
            <li>“Sometimes there's a ringing sound in my ears.”</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="full_content_wrap">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <h3>Reengage with your life</h3>
          <p>Hearing loss can make it challenging to stay connected with the world around you, often leading to feelings of frustration and isolation. At {BUSINESS}, we're dedicated to helping you regain those connections.</p>
          <p>{OWNER.split(',')[0]} and our compassionate team provide comprehensive services, including hearing loss treatment, <a href="{PG(0,'hearing-testing/')}">hearing testing</a>, hearing aids, and personalized hearing aid fittings. With the right care, you can enjoy the everyday moments and meaningful conversations that matter most.</p>
          <div class="btn_group">
            <a class="btn schedule_btn" href="{PG(d,'appointment/')}">Schedule Now</a>
            <a class="btn_alt" href="{PG(d,'about/')}">Meet Your Audiologist</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="services_wrap" aria-label="Hearing care personalized for you">
    <div class="container">
      <h2>Hearing care personalized for you</h2>
      <div class="row justify-content-center">{services_html}</div>
      <div class="btn_group">
        <a class="btn schedule_btn" href="{PG(d,'appointment/')}">Schedule Now</a>
        <a class="btn_alt" href="{PG(d,'services/')}">See All Services</a>
      </div>
    </div>
  </section>

  <section class="steps_wrap" aria-label="How to get started">
    <div class="container">
      <h2>How to get started</h2>
      <div class="row justify-content-center">{steps_html}</div>
      <div class="btn_group">
        <a class="btn schedule_btn" href="{PG(d,'appointment/')}">Schedule Now</a>
      </div>
    </div>
  </section>

  <section class="team_section half_wrap" aria-label="Meet your audiologist">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-11">
          <div class="team_card half_wrap_row">
            <div class="row align-items-center">
              <div class="col-lg-6" data-aos="fade">
                <img src="{IMG(d,'headshot.webp')}" alt="Dr. Gina Angley, AuD, CCC-A — owner and audiologist at {BUSINESS}">
              </div>
              <div class="col-lg-6" data-aos="fade">
                <h3>Meet your audiologist</h3>
                <h4>{OWNER}</h4>
                <p>In over 12 years of clinical experience, Dr. Gina Angley has seen patients' lives transformed by improving their hearing. After earning her Doctor of Audiology at Vanderbilt University, Dr. Angley worked at the world-renowned Bill Wilkerson Center as a research and clinical audiologist. And for the past 5 years she has served as Associate Director for the Adult Amplification program. Dr. Angley is excited to bring her experience and expertise to the community she lives in and has loved since 2006.</p>
                <div class="btn_group">
                  <a class="btn schedule_btn" href="{PG(d,'appointment/')}">Schedule Now</a>
                  <a class="btn_alt" href="{PG(d,'about/')}">Learn More</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>
"""
    write_page("", 0,
        title=f"Adult Audiologist in Nashville, TN | {BUSINESS}",
        description="Evidence-based hearing care from Dr. Gina Angley. Hearing tests, hearing aid fittings with real-ear measurements, and transparent unbundled pricing in Nashville, TN.",
        body=body)


# =========================================================
# ABOUT
# =========================================================
def build_about():
    d = 1
    hero_bg = IMG(d,"hero_0001_AdobeStock_276192047.webp")
    values = [
        ("icon-six.svg","Transparency","Transparency so you understand the difference between the value in the device and the value of the provider"),
        ("icon-seven-edit.svg","Exceptional","Exceptional patient-centered care should be the only care you receive"),
        ("icon-eight-edit.svg","Innovative","Innovative care that is firmly rooted in the latest research and best practices"),
        ("icon-two.svg","Listening","Listening to your challenges and needs rather than talking about all the things I know"),
        ("icon-nine.svg","Accessibility","Accessibility of expertise often sought after at major medical centers"),
    ]
    values_html = "".join(f"""
      <div class="col-md-6 col-lg-4">
        <div class="values_box" data-aos="fade-up">
          <img src="{ICON(d,i)}" alt="" width="70" height="70">
          <h3>{t}</h3>
          <p>{p}</p>
        </div>
      </div>""" for i,t,p in values)

    expects = [
      ("Patient and attentive service",
       "Because we put our value on our medical care and not on device sales, everyone will get the same level of excellent treatment regardless of where they purchase their devices. And you'll never feel rushed or pressured into getting hearing aids or an assistive device if you're not ready."),
      ("Thorough testing & device optimization",
       "Whether you purchase a hearing device from NHCC or elsewhere, we'll conduct thorough testing and real ear measurements to make sure your device is optimized to your unique ear and level of hearing loss."),
      ("Transparent, unbundled pricing",
       "You're not required to purchase your device from NHCC. But if you do, you'll get your device at cost and receive an itemized invoice so you know exactly what you're paying for. We also accept CareCredit financing for those whose insurance doesn't cover audiology services."),
    ]
    expect_html = "".join(f"""
      <div class="col-md-4">
        <div class="expect_box" data-aos="fade-up">
          <h3>{t}</h3>
          <p>{p}</p>
        </div>
      </div>""" for t,p in expects)

    faq = [
      ("What does personalized care at NHCC look like?",
       "At NHCC, we'll do in-depth questioning to understand your particular concerns and struggles and get an accurate picture of how your hearing loss affects your daily life. Expect to do most of the talking during your appointment—we're here to listen. After your full diagnostic testing and interview, you'll get a fully customized plan based on gold standard practices within audiology."),
      ("Why are hearing aids so expensive? Some cost $2,000–$6,000 — sometimes even higher.",
       "Most hearing clinics typically pay $400–$1,300 per hearing aid. Then the costs of the provider's time and expertise, business expenses etc. are bundled into your total price without any transparency of what you're actually paying for."),
      ("What is the difference between a bundled service model and an unbundled service model?",
       "In a bundled service model, the provider or clinic is presenting you with one set price, and you don't see how much of the total cost is the hearing aid and how much of the total cost is related to services. This model is not transparent and has resulted in the misconception that hearing aids are overpriced. At NHCC, you get the advantage of an unbundled service model. You'll always know the cost of the device as it shows on your invoice—what we actually pay for the device. We itemize each service so you know exactly what you're paying for."),
      ("Are real ear measurements really necessary?",
       "Real ear measurement (sometimes known as hearing aid verification) is an evidence-based practice that results in much higher patient satisfaction with their hearing aids. Uncalibrated hearing aids may be better than none at all, but in order to get the full benefit of your device you will need to have them calibrated to your specific ear and hearing loss. For example, you can pick up a pair of readers from a pharmacy or grocery store and they will improve your vision. Those glasses, however, are not tailored to your eyes the way prescription glasses from an optometrist are."),
      ("How does hearing aid verification work?",
       "Also known as real ear measurement, hearing aid verification starts with placing a small, flexible microphone in the ear canal and then placing the hearing aid in the ear. With this microphone, we can then measure how loud the hearing aid is while it is in your ear. While the microphone measures the sound, acoustics, and shape of your ear, we are able to see the data in real time and make changes to your settings."),
      ("Why don't my hearing aids work?",
       "There are three major reasons why people are dissatisfied with their hearing aids: (1) Your hearing aids aren't verified — to ensure patients are receiving the maximum benefit of their hearing aids, the hearing aids should be verified through real-ear measurements, also known as probe microphone measurements. Patients who have had their hearing aids verified report much higher satisfaction. (2) Your hearing aids are not fit to your current hearing — hearing changes over time, and devices need to be adjusted. (3) Your hearing aids aren't the right solution for your hearing profile and lifestyle — we'll evaluate whether your devices, or a different solution, are the best fit."),
      ("If it's not a full-service prescriptive hearing aid that I need, what else could I get?",
       "As of August 17, 2022, the FDA released regulations for a new classification of hearing aid: over-the-counter hearing aids (or OTC). These devices are meant for those with a perceived mild to moderate degree of hearing loss. This may be a better entry point for a patient, and {biz} offers OTC devices to patients. It could also be an accessory or assistive listening device (ALD) for a particular situation. If the only situation where the hearing loss is noticed is, say, at a theater, a personal loop system may be all you need.".format(biz=BUSINESS)),
      ("Are top-of-the-line hearing aids actually worth the money?",
       "There is currently no independent research (research not from a hearing aid manufacturer) that shows more expensive means better understanding and performance. More expensive does not mean that you will understand speech better, that the hearing aid will last longer, or that it's better quality. At {biz}, we help you understand the differences in what is available to you as you make your decision. Once we have an understanding of what your full hearing profile looks like, your lifestyle, and your budget, we can help you make an informed decision on what device will work best for you.".format(biz=BUSINESS)),
    ]
    faq_html = "".join(f"""
      <details class="faq_item" data-aos="fade">
        <summary>{q}</summary>
        <div class="faq_body"><p>{a}</p></div>
      </details>""" for q,a in faq)

    faq_json = {
      "@context":"https://schema.org",
      "@type":"FAQPage",
      "mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq
      ]
    }

    body = f"""
<main id="primary" class="site-main">

  <section class="interior_hero" style="background-image:url('{hero_bg}');">
    <div class="container">
      <h1>About Nashville's Hearing &amp; Communication Center</h1>
      <p>Evidence-based, patient-centered audiology in Nashville, TN — led by Dr. Gina Angley.</p>
    </div>
    {render_wave()}
  </section>

  <section class="about_wrap" aria-label="About Dr. Gina Angley">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-10">
          <div class="about_inner_wrap">
            <div class="row align-items-center">
              <div class="col-md-5" data-aos="fade-right">
                <img src="{IMG(d,'headshot.webp')}" alt="Dr. Gina Angley, AuD, CCC-A — headshot">
              </div>
              <div class="col-md-7" data-aos="fade">
                <h2>About {OWNER.split(',')[0]}</h2>
                <p>You shouldn't feel closed off from your life anymore. Since the beginning of my clinical experience in 2010, I've met with patients who felt like they couldn't be active participants in their lives anymore because of their hearing loss.</p>
                <p>They had a hard time understanding conversations, especially in crowded, noisy spaces. So they stopped going to events, church, or meeting friends, family, colleagues in restaurants because it was just too frustrating.</p>
                <p>They felt embarrassed at work because they had to keep asking coworkers to repeat themselves. And sometimes they missed details that affected their performance. They experienced tension in their relationships, sometimes arguing over the volume on the TV or radio—or their partners thought they weren't listening. They felt isolated, not being able to fully engage with the work, activities, and groups they always loved.</p>
                <p>I started my journey in audiology by earning a bachelor's in Communication Sciences and Disorders from Syracuse University in 2006 (Go Orange!), followed by a Doctor of Audiology degree from Vanderbilt University in 2010. I worked in an ear, nose, and throat office for a few years before rejoining the Vanderbilt Bill Wilkerson Center conducting clinical research and working with patients in the clinic. For 5 years I served as the Associate Director of Adult Amplification before starting {BUSINESS}.</p>
                <p>Amplify your hearing, amplify your life — see your life and relationships transformed simply by improving your hearing. Your initial appointment will be thorough, ensuring that all testing is accurate and that you fully understand your options and costs. Once you have the right device for your lifestyle, fitted to your exact hearing needs, you'll find that you can engage in your life again. And there's no better feeling in the world.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="values_wrap" aria-label="Our values">
    <div class="container">
      <div class="values_top_wrap">
        <h2>Values</h2>
        <p>Since 2010, I've worked with patients who have received exceptional hearing care elsewhere. But for some patients, their experience with audiology has not met their needs. Because of this, {BUSINESS} operates on the following values:</p>
      </div>
      <div class="row justify-content-center">{values_html}</div>
    </div>
  </section>

  <section class="expect_wrap" aria-label="What to expect at NHCC">
    <div class="container">
      <div class="expect_top_wrap">
        <h2>What to expect</h2>
        <p>Throughout your care at {BUSINESS}, you'll experience the gold standard of audiology at every step.</p>
      </div>
      <div class="row justify-content-center">{expect_html}</div>
    </div>
  </section>

  <section class="faq_wrap" aria-label="Frequently asked questions">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-10">
          <h2>FAQ</h2>
          {faq_html}
        </div>
      </div>
    </div>
  </section>

  <section class="reviews_wrap" aria-label="Reviews from our patients">
    <div class="container">
      <h2>Reviews from our patients</h2>
      <div class="reviews_placeholder">
        <p><strong>Patient reviews will be embedded here.</strong></p>
        <p>This section is reserved for the Review Manager / medpb.com widget that appeared on the original NHCC site (<code>results.medpb.com/nsv/</code>). We'll wire it up once the embed credentials are provided.</p>
      </div>
    </div>
  </section>

  <section class="cta_band">
    <div class="container">
      <h2>Ready to talk to your Nashville audiologist?</h2>
      <p>Get top-tier audiology in Nashville. Call {PHONE} to schedule or see all services.</p>
      <div class="btn_group">
        <a class="btn" href="{PHONE_TEL}">Call {PHONE}</a>
        <a class="btn_alt" href="{PG(d,'services/')}">See All Services</a>
      </div>
    </div>
  </section>

</main>
"""
    write_page("about/", 1,
        title=f"About Dr. Gina Angley, AuD | {BUSINESS}",
        description="Meet Dr. Gina Angley, AuD — Doctor of Audiology trained at Vanderbilt. Learn NHCC's values, what to expect, and answers to the top questions about hearing care in Nashville.",
        body=body,
        json_ld=[faq_json])


# =========================================================
# SERVICES
# =========================================================
def build_services():
    d = 1
    hero_bg = IMG(d,"hero_0002_AdobeStock_181761153.webp")
    top_boxes = [
      "Comprehensive diagnostic testing",
      "Communication needs assessment",
      "Device verification and orientation appointments",
      "Minimum 30-day trial period for devices purchased from us",
      "Remote care appointments via telehealth",
      "Concierge services for in-home assessments, device setup, and troubleshooting",
      "Return appointments to reassess goals and devices",
      "New Patient Nights to meet fellow patients and learn good communication strategies",
      "CareCredit to make hearing enhancement accessible to all budgets",
      "Insurance coverage for qualifying policies",
    ]
    boxes_html = "".join(f"""
      <div class="col-md-6 col-lg-6">
        <div class="service_box" data-aos="fade-up">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>
          <p>{html_escape_txt(t)}</p>
        </div>
      </div>""" for t in top_boxes)

    brands = [
      ("Sonova","Phonak, Unitron, Advanced Bionics","https://www.sonova.com/en"),
      ("Starkey","Starkey, Audibel, NuEar, MicroTech","https://www.starkey.com/"),
      ("WS Audiology","Signia, Widex","https://www.wsa.com/"),
      ("GN Group","ReSound, Beltone, Jabra","https://www.gn.com/"),
      ("Demant Group","Oticon, Oticon Medical, Bernafon, Sonic Innovations","https://www.demant.com/"),
    ]
    brands_html = "".join(f"""
      <div class="col-md-6 col-lg-4">
        <div class="service_box" data-aos="fade-up">
          <a href="{u}" target="_blank" rel="noopener">{n}</a>
          <p>{sub}</p>
        </div>
      </div>""" for n,sub,u in brands)

    service_schema = {
      "@context":"https://schema.org",
      "@type":"MedicalBusiness",
      "name": BUSINESS,
      "hasOfferCatalog":{
        "@type":"OfferCatalog","name":"Audiology Services",
        "itemListElement":[
          {"@type":"Offer","itemOffered":{"@type":"MedicalProcedure","name":"Diagnostic hearing testing"}},
          {"@type":"Offer","itemOffered":{"@type":"MedicalProcedure","name":"Hearing aid fitting with real-ear measurements"}},
          {"@type":"Offer","itemOffered":{"@type":"MedicalProcedure","name":"Hearing aid follow-up care and calibration"}},
          {"@type":"Offer","itemOffered":{"@type":"MedicalProcedure","name":"Bone-anchored hearing implants"}},
          {"@type":"Offer","itemOffered":{"@type":"MedicalProcedure","name":"Assistive listening devices"}},
          {"@type":"Offer","itemOffered":{"@type":"MedicalProcedure","name":"Third-party hearing aid maintenance and repair"}}
        ]
      }
    }

    body = f"""
<main id="primary" class="site-main">

  <section class="interior_hero" style="background-image:url('{hero_bg}');">
    <div class="container">
      <h1>Audiology Services in Nashville, TN</h1>
      <p>Comprehensive, evidence-based hearing care — with transparent, unbundled pricing.</p>
    </div>
    {render_wave()}
  </section>

  <section class="service_top_wrap" aria-label="What you get as an NHCC patient">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-10">
          <h2 style="text-align:center">Hearing care personalized for you</h2>
          <p style="text-align:center">For the best hearing available to you, there is no one-size-fits-all solution. That's why at {BUSINESS}, we do thorough testing during your initial appointment so we can fit you with the best hearing amplification device that suits your hearing needs, lifestyle, and budget. As one of our patients, you have access to&hellip;</p>
          <div class="row">{boxes_html}</div>
        </div>
      </div>
    </div>
  </section>

  <section class="service_half_wrap" aria-label="Diagnostic hearing testing">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6" data-aos="fade-right">
          <img src="{IMG(d,'sq_0001_AdobeStock_301955302.webp')}" alt="Quiet diagnostic hearing-test booth">
        </div>
        <div class="col-md-6">
          <div class="service_half_inner">
            <h2>Diagnostic hearing testing</h2>
            <p>Comprehensive hearing evaluations — pure-tone audiometry, speech-in-noise testing, tympanometry, and a full communication needs assessment. Every evaluation includes real-ear measurement capability so we have an accurate picture of how your hearing system is working.</p>
            <a class="btn" href="{PG(d,'hearing-testing/')}">Learn about hearing testing</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="service_half_wrap" aria-label="Hearing aid fitting">
    <div class="container">
      <div class="row align-items-center" style="flex-direction:row-reverse">
        <div class="col-md-6" data-aos="fade-right">
          <img src="{IMG(d,'sq_0002_priscilla-du-preez-W3SEyZODn8U-unsplash.webp')}" alt="Patient and audiologist reviewing hearing aid options">
        </div>
        <div class="col-md-6">
          <div class="service_half_inner">
            <h2>Hearing aid fittings &amp; consultations</h2>
            <p>Unbundled pricing means you see every line item. We fit devices from every major manufacturer — Sonova (Phonak), Starkey, WS Audiology (Signia/Widex), GN (ReSound), and Demant (Oticon) — and we don't mark up device costs. Expect a minimum 30-day trial period, device orientation, and a follow-up plan.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="service_half_wrap" aria-label="Follow-up care">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-md-6" data-aos="fade-right">
          <img src="{IMG(d,'sq_0004_rajiv-perera-_JjYYsQPneE-unsplash.webp')}" alt="Older adult adjusting hearing device with provider">
        </div>
        <div class="col-md-6">
          <div class="service_half_inner">
            <h2>Follow-up care, calibration &amp; real-ear measurement</h2>
            <p>Hearing aid verification with real-ear measurements makes sure your device is tailored to the shape and acoustics of your ear. Return appointments reassess goals, adjust settings, and troubleshoot. Telehealth remote care is available for supported devices.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="middle_services" aria-label="Specialty services">
    <div class="container">
      <h2 style="text-align:center">Specialty services</h2>
      <p style="text-align:center">Care that goes beyond traditional hearing aids.</p>
      <div class="row">
        <div class="col-md-4">
          <div class="service_box" data-aos="fade-up">
            <a href="#bone-anchored">Bone-anchored hearing implants</a>
            <p>For single-sided deafness and conductive hearing loss. Full programming, service, and follow-up.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="service_box" data-aos="fade-up">
            <a href="#ald">Assistive listening devices</a>
            <p>TV streamers, captioned phones, FM/loop systems, and personal amplifiers for the situations that challenge you most.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="service_box" data-aos="fade-up">
            <a href="#third-party">Third-party maintenance &amp; repair</a>
            <p>Bring in any brand. We'll clean, check, recalibrate, and support hearing aids purchased elsewhere.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="service_half_wrap" aria-label="Manufacturers we work with">
    <div class="container">
      <h2 style="text-align:center">Manufacturers we work with</h2>
      <p style="text-align:center">Independent. Unbiased. We fit every major platform so your hearing profile and lifestyle — not a sales quota — drive the recommendation.</p>
      <div class="row justify-content-center">{brands_html}</div>
    </div>
  </section>

  <section class="cta_band">
    <div class="container">
      <h2>You don't have to put up with hearing loss anymore</h2>
      <p>Call {PHONE} to schedule a hearing evaluation with Dr. Gina Angley.</p>
      <div class="btn_group">
        <a class="btn" href="{PHONE_TEL}">Call {PHONE}</a>
        <a class="btn_alt" href="{PG(d,'appointment/')}">Request Online</a>
      </div>
    </div>
  </section>

</main>
"""
    write_page("services/", 1,
        title=f"Audiology Services in Nashville, TN | {BUSINESS}",
        description="Diagnostic hearing testing, hearing aid fittings with real-ear measurements, follow-up care, bone-anchored implants, assistive listening devices, and third-party hearing aid repair in Nashville, TN.",
        body=body,
        json_ld=[service_schema])


def html_escape_txt(s:str)->str:
    return (s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))


# =========================================================
# PATIENT INFO
# =========================================================
def build_patient_info():
    d = 1
    hero_bg = IMG(d,"hero_0003_AdobeStock_336257457-1.webp")
    payments = [
      ("Insurance","We accept insurance, but not all insurance plans cover audiology or hearing aids, so be sure to check your policy to see if you qualify."),
      ("CareCredit","We accept CareCredit to ensure that you can get treatment for hearing loss regardless of budget or insurance coverage. <a href=\"https://www.carecredit.com/\" target=\"_blank\" rel=\"noopener\">Get the info you need and apply today</a>."),
      ("Cherry Financing","Simple, low-interest financing for hearing aids and audiology services — apply online with a soft credit check that doesn't impact your score."),
      ("Payment","You'll always see an itemized invoice before payment so you know exactly what you're paying for. NHCC charges for devices at-cost with no markup fees for the patient. We accept cash, check, credit card, CareCredit, and Cherry."),
    ]
    pay_html = "".join(f"""
      <div class="col-md-6 col-lg-3">
        <div class="payment_box" data-aos="fade-up">
          <h3>{t}</h3>
          <p>{p}</p>
        </div>
      </div>""" for t,p in payments)

    body = f"""
<main id="primary" class="site-main">

  <section class="interior_hero" style="background-image:url('{hero_bg}');">
    <div class="container">
      <h1>Patient Information</h1>
      <p>Everything you need to prepare for your first visit to {BUSINESS}.</p>
    </div>
    {render_wave()}
  </section>

  <section class="full_content_wrap">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <h2>What to bring to your appointment</h2>
          <p>To make your first visit smooth, please bring the following:</p>
          <ul style="text-align:left;display:inline-block;font-size:1.1rem;line-height:1.7">
            <li>A photo ID and current insurance card</li>
            <li>Any current hearing aids or assistive listening devices, plus chargers/accessories</li>
            <li>A list of current medications</li>
            <li>A recent audiogram or prior hearing-test results (if available)</li>
            <li>Your completed <a href="{asset(d,'downloads/nhcc-new-patient-paperwork.pdf')}">new patient paperwork (PDF)</a></li>
            <li>A family member or close friend — a second set of ears is genuinely useful</li>
          </ul>
          <div class="btn_group">
            <a class="btn" href="{asset(d,'downloads/nhcc-new-patient-paperwork.pdf')}" download>Download New Patient Paperwork (PDF)</a>
          </div>
          <p style="font-size:.95rem;color:#666;max-width:600px;margin:1rem auto 0">The form is HIPAA-compliant and can be completed at home to save time. Bring the signed pages to your first visit — or ask us to email a secure link.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="payment_wrap" aria-label="Insurance and payment">
    <div class="container">
      <div class="payment_wrap_top">
        <h2>Insurance &amp; Payment</h2>
        <p>Transparent, unbundled pricing — every invoice is itemized.</p>
      </div>
      <div class="row justify-content-center">{pay_html}</div>
      <div class="payment_wrap_bottom">
        <div class="financing_card" style="max-width:720px;margin:2rem auto 0">
          <h3>Cherry Financing</h3>
          <p>Cherry offers simple, low-interest financing plans — apply online and see if you qualify in seconds. Ask us for the link at your appointment, or call {PHONE} and we'll email it to you.</p>
          <a class="btn" href="{PHONE_TEL}">Call {PHONE}</a>
        </div>
      </div>
    </div>
  </section>

  <section class="full_content_wrap" id="privacy">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <h2>Notice of Privacy Practices</h2>
          <p>{BUSINESS} follows HIPAA guidelines to protect your health information. Request a printed copy at the front desk or contact us for the current Notice of Privacy Practices.</p>
          <div class="btn_group">
            <a class="btn_alt" href="{PG(d,'contact/')}">Contact us about privacy</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="cta_band">
    <div class="container">
      <h2>Have a question before you come in?</h2>
      <p>We're happy to help. Call or text {PHONE}, or send a message and we'll respond by the next business day.</p>
      <div class="btn_group">
        <a class="btn" href="{PHONE_TEL}">Call {PHONE}</a>
        <a class="btn_alt" href="{PG(d,'contact/')}">Contact us</a>
      </div>
    </div>
  </section>

</main>
"""
    write_page("patient-info/", 1,
        title=f"Patient Information & New Patient Paperwork | {BUSINESS}",
        description="Download HIPAA-compliant new patient paperwork, learn what to bring, review insurance and payment options including CareCredit and Cherry financing for hearing care in Nashville, TN.",
        body=body)


# =========================================================
# HEARING TESTING
# =========================================================
def build_hearing_testing():
    d = 1
    hero_bg = IMG(d,"hero_0004_AdobeStock_305465055-1.webp")
    procedure_schema = {
      "@context":"https://schema.org",
      "@type":"MedicalProcedure",
      "name":"Diagnostic hearing test (audiometry)",
      "description":"Comprehensive hearing evaluation including pure-tone audiometry, speech testing in quiet and in noise, and a review of results with a Doctor of Audiology.",
      "procedureType":"https://schema.org/DiagnosticProcedure",
      "howPerformed":"The doctor places headphones in or on the ears and plays tones at varying volumes and frequencies. The patient signals when each tone is heard. Speech repetition tasks are then used to assess understanding in quiet and in noise. Results are reviewed immediately with the patient.",
      "performer":{"@type":"Physician","name":"Gina Angley, AuD, CCC-A"},
      "preparation":"No special preparation is required.",
      "followup":"Dr. Angley will review findings with you and, if indicated, discuss next steps such as device options or referrals."
    }
    body = f"""
<main id="primary" class="site-main">

  <section class="interior_hero" style="background-image:url('{hero_bg}');">
    <div class="container">
      <h1>Hearing Testing in Nashville, TN</h1>
      <p>Straightforward, thorough, and reviewed with you by Dr. Gina Angley.</p>
    </div>
    {render_wave()}
  </section>

  <section class="article_wrap">
    <article>
      <h2>What is a hearing test?</h2>
      <p>If you believe that you or a loved one has hearing loss, we invite you to stop in for a hearing test. A hearing test, or audiometry exam, tests your ability to hear sounds. Sounds vary, based on their loudness (intensity) and the speed of sound wave vibrations (tone). As we age, it is important to continue regular hearing screenings to combat issues related with hearing loss.</p>
      <p>Dr. Gina Angley provides expert audiological care to help you maintain optimal hearing health. If you or a loved one suspects hearing loss, our team is here to assist. Visit <a href="{PG(d,'contact/')}">our audiology clinic in Nashville</a> to take the first step toward better hearing and improved quality of life.</p>

      <h2>What happens during the test?</h2>
      <p>At NHCC, our audiologist will perform the hearing test. It is a straightforward experience.</p>
      <ul>
        <li>First, you will be seated in a room.</li>
        <li>The doctor will place headphones in or on your ears.</li>
        <li>The doctor will play different tones at different volume levels to your ears, one ear at a time.</li>
        <li>You may be asked to raise your hand when you hear a sound or push a button.</li>
        <li>The doctor will then ask you to repeat different words and sentences to learn how you understand in quiet and in noise.</li>
        <li>Dr. Gina Angley will review the results with you and answer any questions you have.</li>
      </ul>

      <h2>What does a hearing test tell the doctor?</h2>
      <p>Hearing tests are able to detect where your hearing loss has occurred. Sometimes there is damage to the nerve of the ear and/or the cochlea, and this is called sensorineural hearing loss. Other times you may have damage to the eardrum or the tiny bones, and this is called conductive hearing loss. The test can help determine the type and location of your hearing loss.</p>
      <p>Talk with Dr. Gina Angley about when you started noticing issues related to your hearing. You can review your medical history and discuss several options in addition to your hearing test.</p>

      <h2>Why may I need a hearing test?</h2>
      <p>A hearing test can give you peace of mind and be the start of your journey to a better life. Often our hearing can deteriorate slowly over time. You may not realize how often you are asking someone to repeat, or how loud you are when you speak. You may have the TV volume turned up very loud, or other lifestyle factors that may become more dramatic over time.</p>
      <p>Often, age-related hearing loss typically occurs in our sixties and seventies and develops gradually as we age. Statistically we all start to lose our hearing when we are in our thirties and forties. One adult in five and more than half of all people over the age of 80 suffer from hearing loss. You are not alone.</p>

      <h3>Factors contributing to hearing loss</h3>
      <ul>
        <li>Aging</li>
        <li>Chronic exposure to loud noises</li>
        <li>Genetics/hereditary</li>
        <li>Excessive earwax</li>
        <li>Some medications</li>
        <li>Viruses, diseases or illnesses</li>
        <li>Trauma</li>
      </ul>

      <h2>How can I get a hearing test?</h2>
      <p>Scheduling a hearing test is very straightforward. We perform these tests daily, and we can help you feel comfortable as you plan for yours. Give us a call to get started. Talking with Dr. Gina Angley is the first step to improve your quality of life.</p>
      <div class="btn_group" style="text-align:left">
        <a class="btn" href="{PHONE_TEL}">Call {PHONE}</a>
        <a class="btn_alt" href="{PG(d,'appointment/')}">Request online</a>
      </div>
    </article>
  </section>

</main>
"""
    write_page("hearing-testing/", 1,
        title=f"Hearing Testing in Nashville, TN | {BUSINESS}",
        description="A Nashville hearing test with Dr. Gina Angley: pure-tone audiometry, speech-in-noise, and a full review of results. Straightforward, thorough, and evidence-based.",
        body=body,
        json_ld=[procedure_schema])


# =========================================================
# APPOINTMENT
# =========================================================
def build_appointment():
    d = 1
    hero_bg = IMG(d,"hero_0001_AdobeStock_276192047.webp")
    body = f"""
<main id="primary" class="site-main">

  <section class="interior_hero" style="background-image:url('{hero_bg}');">
    <div class="container">
      <h1>Schedule an Appointment</h1>
      <p>Call or text {PHONE} — or request a visit online below.</p>
    </div>
    {render_wave()}
  </section>

  <section class="full_content_wrap">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-5">
          <div class="contact_sidebar">
            <h3>Call or text</h3>
            <p><a href="{PHONE_TEL}">{PHONE}</a></p>
            <h3>Visit us</h3>
            <p>{ADDRESS_L1}<br>{ADDRESS_L2}</p>
            <h3>Office hours</h3>
            <p>Monday – Thursday<br>8:00&nbsp;am – 4:00&nbsp;pm</p>
            <p>Friday<br>8:00&nbsp;am – 11:30&nbsp;am</p>
            <p>Saturday &amp; Sunday — closed</p>
          </div>
        </div>
        <div class="col-md-7">
          <h2 style="text-align:left">Request an appointment</h2>
          <p style="text-align:left">Fill out the form and we'll confirm your visit by phone or email within one business day.</p>
          <form class="nhcc-form" action="{PG(d,'appointment/thanks.html')}" method="post" novalidate>
            <div class="form-grid">
              <div>
                <label for="name">Your name</label>
                <input id="name" name="name" type="text" required autocomplete="name">
              </div>
              <div>
                <label for="phone">Phone</label>
                <input id="phone" name="phone" type="tel" required autocomplete="tel">
              </div>
            </div>
            <div class="form-grid">
              <div>
                <label for="email">Email</label>
                <input id="email" name="email" type="email" required autocomplete="email">
              </div>
              <div>
                <label for="pref_date">Preferred date</label>
                <input id="pref_date" name="pref_date" type="date">
              </div>
            </div>
            <div>
              <label for="reason">Reason for visit</label>
              <select id="reason" name="reason">
                <option value="">— Choose one —</option>
                <option>Hearing test / first visit</option>
                <option>Hearing aid fitting consultation</option>
                <option>Hearing aid follow-up or calibration</option>
                <option>Real-ear measurement</option>
                <option>Hearing aid repair or maintenance</option>
                <option>Assistive listening device consult</option>
                <option>Something else</option>
              </select>
            </div>
            <div>
              <label for="message">Anything else we should know?</label>
              <textarea id="message" name="message" rows="5"></textarea>
            </div>
            <div><button class="btn" type="submit">Send request</button></div>
          </form>
        </div>
      </div>
    </div>
  </section>

</main>
"""
    write_page("appointment/", 1,
        title=f"Schedule an Appointment | {BUSINESS}",
        description=f"Request an appointment with Dr. Gina Angley at {BUSINESS} in Nashville, TN. Call or text {PHONE}.",
        body=body)

    thanks_body = f"""
<main id="primary" class="site-main">
  <section class="interior_hero" style="background:#315daa"><div class="container"><h1>Thanks — we got your request</h1><p>We'll confirm your visit by phone or email within one business day.</p></div></section>
  <section class="full_content_wrap"><div class="container"><div class="row justify-content-center"><div class="col-md-8" style="text-align:center">
    <p>Need something sooner? Call or text <a href="{PHONE_TEL}">{PHONE}</a>.</p>
    <div class="btn_group"><a class="btn" href="{PG(1,'index.html')}">Back to home</a></div>
  </div></div></div></section>
</main>
"""
    # Thanks page lives inside appointment/
    write_page("appointment/thanks.html", 1,
        title=f"Appointment Request Received | {BUSINESS}",
        description="Thanks for requesting an appointment with Nashville Hearing & Communication Center.",
        body=thanks_body)


# =========================================================
# CONTACT
# =========================================================
def build_contact():
    d = 1
    hero_bg = IMG(d,"hero_0002_AdobeStock_181761153.webp")
    map_q = "8008+TN-100,+Nashville,+TN+37221"
    body = f"""
<main id="primary" class="site-main">

  <section class="interior_hero" style="background-image:url('{hero_bg}');">
    <div class="container">
      <h1>Contact Us</h1>
      <p>Call or text, message us, or drop by our Bellevue office.</p>
    </div>
    {render_wave()}
  </section>

  <section class="full_content_wrap">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-5">
          <div class="contact_sidebar">
            <h3>Address</h3>
            <p>{ADDRESS_L1}<br>{ADDRESS_L2}</p>
            <h3>Phone &amp; text</h3>
            <p><a href="{PHONE_TEL}">{PHONE}</a></p>
            <h3>Email</h3>
            <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
            <h3>Hours</h3>
            <p>Monday – Thursday: 8:00&nbsp;am – 4:00&nbsp;pm<br>Friday: 8:00&nbsp;am – 11:30&nbsp;am<br>Weekends: closed</p>
          </div>
        </div>
        <div class="col-md-7">
          <h2 style="text-align:left">Send us a message</h2>
          <p style="text-align:left">Use the form below to contact our team.</p>
          <form class="nhcc-form" action="{PG(d,'contact/thanks.html')}" method="post" novalidate>
            <div class="form-grid">
              <div><label for="name">Your name</label><input id="name" name="name" type="text" required></div>
              <div><label for="email">Email</label><input id="email" name="email" type="email" required></div>
            </div>
            <div><label for="phone">Phone</label><input id="phone" name="phone" type="tel"></div>
            <div><label for="message">Message</label><textarea id="message" name="message" rows="6" required></textarea></div>
            <div><button class="btn" type="submit">Send</button></div>
          </form>
        </div>
      </div>
    </div>
  </section>

  <section class="map_wrap" aria-label="Map">
    <iframe
      title="Map to {BUSINESS}"
      loading="lazy"
      src="https://www.google.com/maps?q={map_q}&output=embed"
      referrerpolicy="no-referrer-when-downgrade">
    </iframe>
  </section>

</main>
"""
    write_page("contact/", 1,
        title=f"Contact {BUSINESS} | Nashville, TN",
        description=f"Call or text {PHONE}. Visit us at {ADDRESS_L1}, {ADDRESS_L2}. Open Monday – Friday.",
        body=body)

    # contact thanks page
    thanks_body = f"""
<main id="primary" class="site-main">
  <section class="interior_hero" style="background:#315daa"><div class="container"><h1>Thanks for reaching out</h1><p>We'll reply within one business day.</p></div></section>
  <section class="full_content_wrap"><div class="container"><div class="row justify-content-center"><div class="col-md-8" style="text-align:center">
    <p>Need an answer now? Call <a href="{PHONE_TEL}">{PHONE}</a>.</p>
    <div class="btn_group"><a class="btn" href="{PG(1,'index.html')}">Back to home</a></div>
  </div></div></div></section>
</main>
"""
    write_page("contact/thanks.html", 1,
        title=f"Message sent | {BUSINESS}",
        description="Thanks for contacting Nashville Hearing & Communication Center.",
        body=thanks_body)


# =========================================================
# BLOG INDEX + 2 POSTS
# =========================================================
def build_blog():
    d = 1
    hero_bg = IMG(d,"hero_0003_AdobeStock_336257457-1.webp")
    posts = [
      {
        "slug":"how-to-preserve-and-protect-your-hearing/",
        "title":"How to preserve and protect your hearing as you grow older",
        "date":"2024-11-20",
        "excerpt":"Loud noise exposure has lasting effects on your hearing. Here's how to protect your ears and enjoy better hearing at any age.",
      },
      {
        "slug":"how-to-properly-clean-your-hearing-aid/",
        "title":"How to properly clean your hearing aid",
        "date":"2024-12-05",
        "excerpt":"Regular cleaning keeps your hearing aids working at their best. Easy, actionable tips from Dr. Gina Angley.",
      },
    ]
    post_cards = "".join(f"""
      <article class="post_card" data-aos="fade-up">
        <h3><a href="{asset(d, 'blog/' + p['slug'])}">{p['title']}</a></h3>
        <p class="meta">{p['date']} · {OWNER.split(',')[0]}</p>
        <p>{p['excerpt']}</p>
      </article>""" for p in posts)

    body = f"""
<main id="primary" class="site-main">

  <section class="interior_hero" style="background-image:url('{hero_bg}');">
    <div class="container">
      <h1>NHCC Blog</h1>
      <p>Hearing-care articles, patient education, and practical tips from Dr. Gina Angley.</p>
    </div>
    {render_wave()}
  </section>

  <section class="post_list">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-10">{post_cards}</div>
      </div>
    </div>
  </section>

</main>
"""
    write_page("blog/", 1,
        title=f"Blog — hearing care articles | {BUSINESS}",
        description="Patient education, hearing protection tips, and hearing aid care guides from Dr. Gina Angley in Nashville, TN.",
        body=body)

    # Post 1
    post1_json = {
      "@context":"https://schema.org","@type":"BlogPosting",
      "headline":"How to preserve and protect your hearing as you grow older",
      "author":{"@type":"Person","name":"Gina Angley, AuD"},
      "publisher":{"@type":"Organization","name":BUSINESS,"logo":{"@type":"ImageObject","url":CANONICAL_BASE+"/assets/icons/NHCC-Full-2Color-new.svg"}},
      "datePublished":"2024-11-20","dateModified":"2024-11-20",
      "mainEntityOfPage":CANONICAL_BASE+"/blog/how-to-preserve-and-protect-your-hearing/",
      "image":CANONICAL_BASE+"/assets/images-webp/man-struggling-to-hear.webp",
    }
    post1_body = f"""
<main id="primary" class="site-main">
  <section class="article_wrap">
    <article>
      <p class="meta"><a href="{asset(2,'blog/')}">&larr; All articles</a> · November 20, 2024</p>
      <h1>How to preserve and protect your hearing as you grow older</h1>
      <p>Have you ever reminisced about attending rock concerts in the '70s or '80s? Many of us fondly remember those loud, electrifying moments, but if you've been to a boy band concert in the '90s or 2000s, you know the volume—and the screams—can reach another level. Whether it's rock, pop, or power tools, loud noise exposure has lasting effects on our hearing health. Here's how you can protect your ears and enjoy better hearing as you age.</p>

      <img src="{asset(2,'assets/images-webp/man-struggling-to-hear.webp')}" alt="Older man struggling to hear a conversation">

      <h2>When does hearing loss begin?</h2>
      <p>Did you know that hearing changes start as early as 30? Hearing loss often creeps in so gradually that many don't notice until it significantly impacts their daily life. By age 65, one-third of people experience hearing loss, and over half of those older than 75 have difficulty hearing.</p>
      <p>This age-related hearing loss, called <strong>presbycusis</strong>, typically affects both ears. However, it's not limited to older adults. Surprisingly, 10% of Americans aged 18 and older already experience some form of hearing loss.</p>

      <h2>What causes age-related hearing loss (presbycusis)?</h2>
      <p>While there have been studies to look at what changes we see in hearing solely due to age, most of us do not live in a community devoid of noise (although there are days I wish for that — anyone else?). This means there are many factors that play a role in how our hearing changes over time. We all have different noise exposure in our life, we each have unique life experiences, our genetics are different, and our health is different. All of these factors play a role in how our hearing will change as we age, so it's important to manage or control as many factors as we can.</p>

      <h2>Safeguarding your hearing</h2>
      <p>Since there are so many factors that can impact your hearing, the next logical question is: is there anything I can do to prevent it? We can't prevent changes that happen from Father Time, but we can prevent changes due to noise exposure. Protecting yourself from noise-induced hearing loss (NIHL) is crucial, regardless of your age. Exposure to loud noises can significantly impact your hearing health — and it's not just the volume of sound that matters but also how long you are in those environments. These damaging noises can come from various sources such as loud music, headphones used at high volumes, construction sites, fireworks, guns, power tools, and motorcycles.</p>
      <p>As you age, it becomes even more important to safeguard your hearing. Here are some steps you can take:</p>
      <ul>
        <li><strong>Avoid loud sounds:</strong> Be mindful of your surroundings and avoid environments where loud noises are prevalent, or take breaks if you find yourself in such situations.</li>
        <li><strong>Reduce exposure:</strong> Again, it's not just level of sound but length of exposure too. Limit the amount of time you spend in environments with loud sounds. This could involve reducing the duration of activities like concerts, using power tools, or attending sporting events.</li>
        <li><strong>Use protective gear:</strong> Wear earplugs or protective earmuffs when you anticipate exposure to loud noises. This is particularly important when engaging in activities such as mowing the lawn, attending concerts, or operating machinery. If you're like me and have small ear canals, the over-the-counter options can usually be uncomfortable. If you are around loud sounds frequently, I would consider investing in some custom hearing protection — this ensures accuracy of placement and comfort.</li>
      </ul>
      <p>By taking these proactive measures, you can help preserve your hearing and enjoy a better quality of life as you age.</p>

      <h2>Safe listening tips</h2>
      <p>With the explosion of personal listening devices, there are some additional ways to reduce your risk of developing NIHL.</p>
      <ul>
        <li>Never listen at 100% volume. If there is someone in the room with you, and they can hear your music, it's too loud.</li>
        <li>Follow the 60:60 rule. Listen at 60% maximum volume for no longer than 60 minutes per day.</li>
        <li>Use the "smart volume" feature if your device has one to regulate the volume automatically.</li>
        <li>Keep the volume low even in noisy environments.</li>
        <li>Take periodic breaks for 15 minutes.</li>
        <li>You should be able to hear someone call your name.</li>
      </ul>

      <h2>Do what you can</h2>
      <p>There are many health conditions that can impact hearing like heart disease, diabetes, and smoking, so striving to live a healthy and active lifestyle can also lead to healthy hearing.</p>
      <p>By taking these proactive measures, you can help preserve your hearing and enjoy a better quality of life as you age.</p>
      <p>If you suspect you are having hearing issues, make an appointment with {BUSINESS}. Call <a href="{PHONE_TEL}">{PHONE}</a> to schedule an appointment in Nashville.</p>

      <p class="meta" style="margin-top:2rem">Sources: <a href="https://www.nidcd.nih.gov/health/age-related-hearing-loss" rel="noopener" target="_blank">NIH/NIDCD — Age-Related Hearing Loss (Presbycusis)</a>, <a href="https://hearing.health.mil/Prevention/Dangers-of-Loud-Noise/Safe-Listening" rel="noopener" target="_blank">Hearing Center of Excellence — Safe Listening</a>, <a href="https://www.summithealth.com/health-wellness/five-ways-protect-your-hearing-any-age" rel="noopener" target="_blank">Summit Health</a>, <a href="https://www.webmd.com/a-to-z-guides/hearing-loss-prevention" rel="noopener" target="_blank">WebMD — How to Prevent Hearing Loss</a>.</p>

      <div class="btn_group" style="text-align:left">
        <a class="btn" href="{asset(2,'appointment/')}">Schedule a hearing test</a>
        <a class="btn_alt" href="{asset(2,'blog/')}">More articles</a>
      </div>
    </article>
  </section>
</main>
"""
    write_page("blog/how-to-preserve-and-protect-your-hearing/", 2,
        title="How to preserve and protect your hearing as you grow older | NHCC",
        description="Dr. Gina Angley on the causes of age-related hearing loss, noise-induced hearing loss, safe-listening tips, and hearing protection strategies.",
        body=post1_body,
        json_ld=[post1_json])

    # Post 2
    post2_json = {
      "@context":"https://schema.org","@type":"BlogPosting",
      "headline":"How to properly clean your hearing aid",
      "author":{"@type":"Person","name":"Gina Angley, AuD"},
      "publisher":{"@type":"Organization","name":BUSINESS},
      "datePublished":"2024-12-05","dateModified":"2024-12-05",
      "mainEntityOfPage":CANONICAL_BASE+"/blog/how-to-properly-clean-your-hearing-aid/",
      "image":CANONICAL_BASE+"/assets/images-webp/man-cleaning-hearing-aids.webp"
    }
    post2_body = f"""
<main id="primary" class="site-main">
  <section class="article_wrap">
    <article>
      <p class="meta"><a href="{asset(2,'blog/')}">&larr; All articles</a> · December 5, 2024</p>
      <h1>How to properly clean your hearing aid</h1>
      <p>Hearing aids are a valuable investment in your hearing health. To ensure they continue to perform at their best, regular maintenance is key. Let's explore some easy tips for properly cleaning your hearing aids.</p>

      <img src="{asset(2,'assets/images-webp/man-cleaning-hearing-aids.webp')}" alt="Person cleaning a hearing aid with a brush">

      <h2>Daily cleaning and professional maintenance</h2>
      <p>Keeping your hearing aids working well requires some regular cleaning. It's not an intensive or long procedure, but should be done daily or at least on a weekly basis. However, just as you seek specialized cleaning from your dentist even though you brush your teeth every day, periodic professional cleaning from Dr. Gina Angley will keep your aids working their absolute best. Your hearing specialist will recommend how often you should bring your hearing aids in for a thorough cleaning, usually every 6 months.</p>

      <h2>General care for your hearing aids</h2>
      <p>Use the following general care tips to keep your hearing aids clean and prevent issues.</p>
      <ul>
        <li>Keep your aids away from moisture and chemicals. Take them out when showering or bathing. Finish using all hair products and sprays before putting them in your ears.</li>
        <li>Clean them at bedtime which gives them time to dry out.</li>
        <li>Avoid extreme temperatures. Leave them in the house if you are shoveling snow in very cold temps, and of course take them out before getting into a pool. However, it's not a good idea to leave them sitting on a table by the pool.</li>
        <li>When not using your aids, keep them in a case or charger unit to avoid dirt and damage.</li>
        <li>Always wash your hands before handling your hearing aids.</li>
        <li>Store your aids in a dehumidifier for storage at night.</li>
      </ul>

      <h2>Hearing aid cleaning tools</h2>
      <p>Ask Dr. Gina Angley about purchasing hearing aid tools for cleaning. They often include:</p>
      <ul>
        <li>A brush</li><li>A slim tube cleaning tool</li><li>Wax loops</li>
        <li>An ear mold tubing blower</li><li>Mini pipe cleaners</li>
        <li>A microfiber cloth</li><li>Hearing aid dryers</li>
      </ul>

      <h2>Cleaning different types of hearing aids</h2>
      <p>The right cleaning routine will depend on the type of hearing aid you have.</p>

      <h3>How to clean In-The-Ear (ITE) hearing aids</h3>
      <ol>
        <li>Holding the aid face down, remove any debris or earwax with the cleaning brush from the outer parts.</li>
        <li>Use a pick or a loop to remove wax left after the brushing.</li>
        <li>Push the slim tube cleaning tool completely through the ventilation tube. Reverse this step and go the other way, cleaning the outer portion with a soft cloth.</li>
        <li>Clean the entire surface with a microfiber or soft cloth and test.</li>
      </ol>

      <h3>How to clean Behind-The-Ear (BTE) hearing aids</h3>
      <ol>
        <li>Start by removing the tubing from the aid.</li>
        <li>Put the aid face down and use the brush to clean off any debris and wax including the receiver and microphone cover.</li>
        <li>Use a wax loop or pick to remove anything that didn't come off with the brush.</li>
        <li>Use the brush and clean the microphone openings.</li>
        <li>Remove the tubing and clean with a pipe cleaner. After one pass through, clean with a cloth and go in the other direction.</li>
        <li>Remove and clean the ear mold per the manufacturer's instructions. Soak in warm soapy water and use the ear mold tubing blower to remove any moisture or debris.</li>
        <li>Dry the ear mold and ventilation tubing with a soft clean cloth.</li>
        <li>Once everything is dry, reassemble the hearing aids and test.</li>
      </ol>
      <p>Prevent ear infections by keeping your own ears clean and free from wax buildup along with regular cleaning of your hearing aids.</p>
      <p>Contact Dr. Gina Angley at <a href="{PHONE_TEL}">{PHONE}</a> with any additional questions about cleaning your hearing aids or to schedule a professional cleaning in Nashville, TN.</p>

      <p class="meta" style="margin-top:2rem">Sources: <a href="https://www.webmd.com/healthy-aging/how-to-clean-hearing-aids" target="_blank" rel="noopener">WebMD — How to Clean Your Hearing Aids</a>, <a href="https://www.healthyhearing.com/help/hearing-aids/cleaning" target="_blank" rel="noopener">HealthyHearing — How to clean your hearing aids</a>, <a href="https://www.audibel.com/hearing-loss-treatment/hearing-aid-cleaning-guide/" target="_blank" rel="noopener">Audibel — Daily Cleaning Guide</a>.</p>

      <div class="btn_group" style="text-align:left">
        <a class="btn" href="{asset(2,'appointment/')}">Schedule a cleaning</a>
        <a class="btn_alt" href="{asset(2,'blog/')}">More articles</a>
      </div>
    </article>
  </section>
</main>
"""
    write_page("blog/how-to-properly-clean-your-hearing-aid/", 2,
        title="How to properly clean your hearing aid | NHCC",
        description="Daily cleaning, BTE vs ITE care, tools, and professional cleaning guidance from Dr. Gina Angley in Nashville.",
        body=post2_body,
        json_ld=[post2_json])


# =========================================================
# NEWSLETTERS
# =========================================================
def build_newsletters():
    d = 1
    hero_bg = IMG(d,"hero_0004_AdobeStock_305465055-1.webp")
    items = [
      ("january2025/","Launching our monthly newsletter","January 2025",
       "Each month we'll explore how hearing health connects to heart health, nutrition, stress, and your overall wellness — starting this issue."),
      ("february-2025/","Heart Health Month — love your ears, love your heart","February 2025",
       "A closer look at the science connecting cardiovascular health and your hearing, plus heartfelt tips for healthy ears."),
      ("february2025/","How heart health impacts your hearing","February 2025",
       "Research-based tips on circulation, hydration, diet, and hearing — with a direct link to schedule a test."),
    ]
    cards = "".join(f"""
      <article class="post_card" data-aos="fade-up">
        <h3><a href="{asset(d,'newsletters/'+slug)}">{t}</a></h3>
        <p class="meta">{date}</p>
        <p>{desc}</p>
      </article>""" for slug,t,date,desc in items)

    body = f"""
<main id="primary" class="site-main">
  <section class="interior_hero" style="background-image:url('{hero_bg}');">
    <div class="container">
      <h1>NHCC Newsletters</h1>
      <p>Monthly notes on hearing health and whole-body wellness from Dr. Gina Angley.</p>
    </div>
    {render_wave()}
  </section>
  <section class="post_list">
    <div class="container"><div class="row justify-content-center"><div class="col-lg-10">{cards}</div></div></div>
  </section>
</main>
"""
    write_page("newsletters/", 1,
        title=f"Newsletters | {BUSINESS}",
        description="NHCC monthly newsletters on hearing health, heart health, and wellness from Dr. Gina Angley.",
        body=body)

    # Jan 2025
    jan_body = f"""
<main id="primary" class="site-main">
  <section class="article_wrap">
    <article>
      <p class="meta"><a href="{asset(2,'newsletters/')}">&larr; All newsletters</a> · January 2025</p>
      <h1>Launching our monthly newsletter</h1>
      <p style="text-align:center"><em>Stay Informed, Stay Healthy!</em></p>
      <p>We're thrilled to announce something new and exciting just for you — starting next month, you'll receive a monthly email newsletter designed to keep you informed about how hearing health connects to your overall well-being.</p>
      <h2>What to expect</h2>
      <p>Each month, we'll explore how hearing health relates to various health conditions and awareness topics, like:</p>
      <ul>
        <li><strong>Heart health</strong> — discover the surprising connection between your ears and your cardiovascular system.</li>
        <li><strong>Nutrition</strong> — learn how your diet can impact your hearing.</li>
        <li><strong>Stress management</strong> — find out how reducing stress can improve your hearing (and your life!).</li>
        <li>And more!</li>
      </ul>
      <p>Our goal is to provide practical tips, engaging stories, and useful insights to help you take charge of your hearing health while understanding its role in your total wellness.</p>
      <h2>Why hearing health matters</h2>
      <p>Your hearing is more than just about sound — it's about connection, safety, and living life to the fullest. By staying informed, you can take simple steps to protect your hearing and improve your quality of life. Keep an eye on your inbox — your first issue is on the way soon!</p>
      <p>To your health and happiness,<br>Dr. Gina and Suzanne</p>
    </article>
  </section>
</main>
"""
    write_page("newsletters/january2025/", 2,
        title="January 2025 Newsletter | NHCC",
        description="Launching our monthly newsletter on hearing health and whole-body wellness from Dr. Gina Angley.",
        body=jan_body)

    # Feb 2025 (heart health tips — article-style)
    feb1_body = f"""
<main id="primary" class="site-main">
  <section class="article_wrap">
    <article>
      <p class="meta"><a href="{asset(2,'newsletters/')}">&larr; All newsletters</a> · February 2025</p>
      <h1>How heart health impacts your hearing: what you need to know</h1>
      <p>When we think about heart health, we often picture strong arteries, steady pulses, and blood pressure readings. But what if we told you that your heart's well-being could influence how well you hear the world around you? It's true — your heart and ears are more connected than you might realize.</p>
      <h3>The connection between cardiovascular health and hearing loss</h3>
      <p>Your cardiovascular system is like a highway delivering oxygen and nutrients throughout your body — including your ears. The inner ear is home to delicate hair cells that rely on a steady, rich blood supply to function properly. When blood flow is reduced due to conditions like high blood pressure or arterial blockages, these cells may not get the oxygen they need, making them more vulnerable to damage. The result? Hearing difficulties, including increased risk of hearing loss and even tinnitus.</p>
      <h3>Can hearing loss be a sign of heart problems?</h3>
      <p>Interestingly, changes in your hearing can sometimes be an early indicator of cardiovascular concerns. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6145783/" target="_blank" rel="noopener">Research</a> suggests that certain types of hearing loss — especially in the low frequencies — may signal underlying heart issues. While hearing tests can't diagnose heart disease, they can provide valuable clues about your overall circulation and health.</p>
      <h3>How to improve heart and hearing health</h3>
      <ul>
        <li><strong>Stay active to boost circulation</strong> — exercise isn't just great for your heart; it supports good circulation to your ears, keeping those hair cells nourished and strong.</li>
        <li><strong>Hydrate for better blood flow</strong> — proper hydration helps maintain good circulation, reducing strain on both your heart and ears.</li>
        <li><strong>Limit salt &amp; sugar intake</strong> — high sodium and excessive sugar consumption can contribute to high blood pressure, which in turn may impact hearing function.</li>
        <li><strong>Monitor your blood pressure</strong> — high blood pressure is linked to both heart disease and hearing loss. Regular check-ups help catch issues early.</li>
        <li><strong>Check your hearing, check your heart</strong> — a hearing test isn't just about hearing. It's an easy, painless way to gain insights into your overall wellness.</li>
      </ul>
      <h3>Final thoughts</h3>
      <p>This February, as we celebrate Heart Health Month, let's take a moment to appreciate the incredible ways our body systems work together. A strong heart means vibrant hearing, so let's care for both.</p>
      <div class="btn_group" style="text-align:left">
        <a class="btn" href="{asset(2,'appointment/')}">Schedule a hearing test</a>
      </div>
    </article>
  </section>
</main>
"""
    write_page("newsletters/february2025/", 2,
        title="February 2025 — How heart health impacts your hearing | NHCC",
        description="Your heart and ears are more connected than you think. Research-based tips on circulation, hydration, and hearing from Dr. Gina Angley.",
        body=feb1_body)

    # February long-form
    feb2_body = f"""
<main id="primary" class="site-main">
  <section class="article_wrap">
    <article>
      <p class="meta"><a href="{asset(2,'newsletters/')}">&larr; All newsletters</a> · February 2025</p>
      <h1 style="text-align:center">February is Heart Health Month — love your ears, love your heart</h1>
      <p>As February rolls in, we're reminded of the importance of heart health, not just for your overall well-being but for your hearing, too. At {BUSINESS}, we're celebrating Heart Health Month by exploring the intriguing relationship between cardiovascular health and your auditory system.</p>
      <h3>The science behind the connection</h3>
      <p>Your heart is the powerhouse that keeps your body functioning, pumping blood rich with oxygen and nutrients to every cell. This includes the delicate hair cells in your inner ear, which are essential for converting sound waves into signals your brain can interpret. When your cardiovascular health is compromised, and blood flow is reduced, these cells can suffer damage, leading to hearing loss.</p>
      <h3>Heartfelt tips for healthy ears</h3>
      <p>To maintain both heart and hearing health, consider incorporating these habits into your daily routine:</p>
      <p><strong>Stay active:</strong> Engaging in regular physical activity not only strengthens your heart but also supports good circulation, essential for healthy hearing. Activities like walking, cycling, or swimming can make a significant difference.</p>
      <p><strong>Eat heart-healthy foods:</strong> Your diet plays a crucial role in maintaining cardiovascular health. Focus on consuming whole grains, lean proteins, and plenty of fruits and vegetables. These foods can help keep your blood vessels clear and your blood pressure in check.</p>
      <p><strong>Avoid smoking:</strong> Smoking is a known risk factor for both heart disease and hearing loss. By quitting smoking, you can significantly improve your overall health and protect your ears.</p>
      <p><strong>Monitor your blood pressure:</strong> High blood pressure can have a detrimental effect on your hearing. Regular check-ups with your healthcare provider can help you keep it under control.</p>
      <h3>Taking action this February</h3>
      <p>This Heart Health Month, take proactive steps to protect your heart and hearing. Scheduling your annual hearing exam can be a vital first step toward better health. Our team at NHCC is here to support you on your journey, offering comprehensive diagnostic testing and personalized care.</p>
      <h3>Listen with your heart</h3>
      <p>As we celebrate Valentine's season, remember to listen with your heart. Taking care of your hearing is a loving gesture to yourself and those around you. Let us assist you in maintaining optimal hearing health, ensuring you don't miss out on the moments that matter.</p>
      <p>Happy Heart Health Month from all of us at {BUSINESS}. Schedule your appointment today and embrace a healthier you.</p>
      <p>To your health and happiness,<br>Dr. Gina</p>
      <div class="btn_group" style="text-align:left">
        <a class="btn" href="{asset(2,'appointment/')}">Schedule your hearing exam</a>
      </div>
    </article>
  </section>
</main>
"""
    write_page("newsletters/february-2025/", 2,
        title="February 2025 — Heart Health Month | NHCC",
        description="Love your ears, love your heart. Heart-healthy habits that also protect your hearing, from Dr. Gina Angley.",
        body=feb2_body)


# =========================================================
# MAIN
# =========================================================
def main():
    build_home()
    build_about()
    build_services()
    build_patient_info()
    build_hearing_testing()
    build_appointment()
    build_contact()
    build_blog()
    build_newsletters()
    # robots + sitemap
    write_robots_and_sitemap()
    print("ok")


def write_robots_and_sitemap():
    routes = [
      "", "about/", "services/", "patient-info/", "hearing-testing/",
      "appointment/", "contact/", "blog/",
      "blog/how-to-preserve-and-protect-your-hearing/",
      "blog/how-to-properly-clean-your-hearing-aid/",
      "newsletters/",
      "newsletters/january2025/",
      "newsletters/february2025/",
      "newsletters/february-2025/",
    ]
    urls = []
    for r in routes:
        loc = CANONICAL_BASE + "/" + r
        urls.append(f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{'1.0' if r=='' else '0.8'}</priority></url>")
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    (OUT / "sitemap.xml").write_text(sm, encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {CANONICAL_BASE}/sitemap.xml\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print("wrote sitemap.xml, robots.txt, .nojekyll")


if __name__ == "__main__":
    main()
