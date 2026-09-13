#!/usr/bin/env python3

import os
import sys
import json
import time
import socket
import random
import ssl
import re
import shutil
import subprocess
import urllib.parse
import urllib.request
import urllib.error

from datetime import datetime, timezone


# ============================================================
# CHANNEL INFO ENGINE
# WORLDWIDE NEWS WEBSITE SCANNER
# Made by DARK 47
# ============================================================

REPORT_DIR = "channel_info_reports"
USER_AGENT = "CHANNEL-INFO/3.0"


# ============================================================
# COLORS
# ============================================================

RESET = "\033[0m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
DIM = "\033[2m"


# ============================================================
# APPROVED WORLDWIDE NEWS DATABASE
#
# Only these news domains are allowed.
# Random / unrelated websites are rejected.
# ============================================================

KNOWN_CHANNELS = {

    # --------------------------------------------------------
    # PAKISTAN
    # --------------------------------------------------------

    "geo news": "geo.tv",
    "geo": "geo.tv",

    "ary news": "arynews.tv",
    "ary": "arynews.tv",

    "samaa": "samaa.tv",
    "samaa tv": "samaa.tv",

    "dunya news": "dunyanews.tv",
    "dunya": "dunyanews.tv",

    "express news": "express.pk",
    "express": "express.pk",

    "bol news": "bolnews.com",
    "bol": "bolnews.com",

    "aaj news": "aaj.tv",
    "aaj": "aaj.tv",

    "92 news": "92newshd.tv",

    "hum news": "humnews.pk",
    "hum": "humnews.pk",

    "gnn": "gnnhd.tv",
    "gnn news": "gnnhd.tv",

    "ptv news": "ptv.com.pk",
    "ptv": "ptv.com.pk",

    "dawn": "dawn.com",
    "dawn news": "dawn.com",

    "the news": "thenews.com.pk",
    "the news international": "thenews.com.pk",

    "nation": "nation.com.pk",

    "business recorder": "brecorder.com",

    "pakistan today": "pakistantoday.com.pk",

    "express tribune": "tribune.com.pk",
    "tribune pakistan": "tribune.com.pk",

    "nawaiwaqt": "nawaiwaqt.com.pk",

    "daily times pakistan": "dailytimes.com.pk",


    # --------------------------------------------------------
    # INDIA
    # --------------------------------------------------------

    "ndtv": "ndtv.com",
    "ndtv india": "ndtv.com",

    "aaj tak": "aajtak.in",

    "india today": "indiatoday.in",

    "news18": "news18.com",
    "cnn news18": "news18.com",

    "times now": "timesnownews.com",

    "times of india": "timesofindia.indiatimes.com",

    "the hindu": "thehindu.com",

    "hindustan times": "hindustantimes.com",

    "republic world": "republicworld.com",
    "republic tv": "republicworld.com",

    "zee news": "zeenews.india.com",
    "zee media": "zeenews.india.com",

    "wion": "wionews.com",

    "abp news": "abplive.com",

    "tv9 bharatvarsh": "tv9hindi.com",
    "tv9": "tv9.com",

    "india tv": "indiatvnews.com",

    "news24": "news24online.com",

    "news nation": "newsnationtv.com",

    "firstpost": "firstpost.com",

    "the print": "theprint.in",

    "scroll": "scroll.in",

    "the wire": "thewire.in",

    "deccan herald": "deccanherald.com",

    "deccan chronicle": "deccanchronicle.com",

    "telegraph india": "telegraphindia.com",

    "financial express india": "financialexpress.com",

    "business standard": "business-standard.com",


    # --------------------------------------------------------
    # ISRAEL
    # --------------------------------------------------------

    "i24news": "i24news.tv",
    "i24 news": "i24news.tv",

    "times of israel": "timesofisrael.com",

    "jerusalem post": "jpost.com",
    "the jerusalem post": "jpost.com",

    "haaretz": "haaretz.com",

    "israel hayom": "israelhayom.com",

    "channel 12 israel": "mako.co.il",

    "n12": "n12.co.il",

    "kan news": "kan.org.il",
    "kan 11": "kan.org.il",

    "israel national news": "israelnationalnews.com",

    "ynet": "ynet.co.il",

    "yedioth aharonoth": "ynet.co.il",


    # --------------------------------------------------------
    # USA
    # --------------------------------------------------------

    "cnn": "cnn.com",
    "cnn international": "cnn.com",

    "fox news": "foxnews.com",

    "msnbc": "msnbc.com",

    "abc news": "abcnews.go.com",
    "abc": "abcnews.go.com",

    "cbs news": "cbsnews.com",
    "cbs": "cbsnews.com",

    "nbc news": "nbcnews.com",
    "nbc": "nbcnews.com",

    "pbs news": "pbs.org",
    "pbs": "pbs.org",

    "npr": "npr.org",

    "associated press": "apnews.com",
    "ap news": "apnews.com",

    "reuters": "reuters.com",

    "bloomberg": "bloomberg.com",

    "new york times": "nytimes.com",
    "nytimes": "nytimes.com",

    "washington post": "washingtonpost.com",

    "wall street journal": "wsj.com",
    "wsj": "wsj.com",

    "usa today": "usatoday.com",

    "newsweek": "newsweek.com",

    "time": "time.com",

    "politico": "politico.com",

    "the hill": "thehill.com",

    "axios": "axios.com",

    "cnbc": "cnbc.com",

    "forbes": "forbes.com",

    "newsmax": "newsmax.com",


    # --------------------------------------------------------
    # CANADA
    # --------------------------------------------------------

    "cbc news": "cbc.ca",
    "cbc": "cbc.ca",

    "ctv news": "ctvnews.ca",

    "global news": "globalnews.ca",

    "citynews": "citynews.ca",

    "toronto star": "thestar.com",

    "national post": "nationalpost.com",

    "globe and mail": "theglobeandmail.com",


    # --------------------------------------------------------
    # UNITED KINGDOM
    # --------------------------------------------------------

    "bbc": "bbc.com",
    "bbc news": "bbc.com",

    "sky news": "news.sky.com",
    "sky news uk": "news.sky.com",

    "itv news": "itv.com",

    "channel 4 news": "channel4.com",

    "channel 5 news": "channel5.com",

    "the guardian": "theguardian.com",

    "the independent": "independent.co.uk",

    "daily telegraph": "telegraph.co.uk",

    "the times uk": "thetimes.com",

    "financial times": "ft.com",

    "daily mail": "dailymail.co.uk",

    "mirror": "mirror.co.uk",

    "express uk": "express.co.uk",

    "evening standard": "standard.co.uk",

    "gb news": "gbnews.com",


    # --------------------------------------------------------
    # AUSTRALIA / NEW ZEALAND
    # --------------------------------------------------------

    "abc australia": "abc.net.au",
    "abc news australia": "abc.net.au",

    "sbs news": "sbs.com.au",

    "news.com.au": "news.com.au",

    "the australian": "theaustralian.com.au",

    "nine news": "9news.com.au",

    "seven news": "7news.com.au",

    "sky news australia": "skynews.com.au",

    "stuff": "stuff.co.nz",

    "rnz": "rnz.co.nz",

    "1news": "1news.co.nz",

    "new zealand herald": "nzherald.co.nz",


    # --------------------------------------------------------
    # QATAR / UAE / SAUDI / MIDDLE EAST
    # --------------------------------------------------------

    "al jazeera": "aljazeera.com",
    "al jazeera english": "aljazeera.com",

    "al jazeera arabic": "aljazeera.net",

    "al arabiya": "alarabiya.net",

    "al hadath": "alhadath.net",

    "sky news arabia": "skynewsarabia.com",

    "arab news": "arabnews.com",

    "gulf news": "gulfnews.com",

    "khaleej times": "khaleejtimes.com",

    "the national": "thenationalnews.com",

    "middle east eye": "middleeasteye.net",

    "al monitor": "al-monitor.com",

    "asharq al awsat": "aawsat.com",

    "asharq news": "asharq.com",

    "lbc international": "lbcgroup.tv",

    "al araby": "alaraby.co.uk",

    "al mayadeen": "almayadeen.net",


    # --------------------------------------------------------
    # TURKEY
    # --------------------------------------------------------

    "trt world": "trtworld.com",

    "trt haber": "trthaber.com",

    "trt": "trt.net.tr",

    "hurriyet": "hurriyet.com.tr",

    "daily sabah": "dailysabah.com",

    "anadolu agency": "aa.com.tr",

    "aa turkey": "aa.com.tr",

    "haber turk": "haberturk.com",

    "ntv turkey": "ntv.com.tr",


    # --------------------------------------------------------
    # FRANCE / GERMANY / SPAIN / ITALY
    # --------------------------------------------------------

    "france 24": "france24.com",
    "france24": "france24.com",

    "rfi": "rfi.fr",

    "le monde": "lemonde.fr",

    "le figaro": "lefigaro.fr",

    "dw": "dw.com",
    "deutsche welle": "dw.com",
    "dw news": "dw.com",

    "der spiegel": "spiegel.de",

    "tagesschau": "tagesschau.de",

    "zdf": "zdf.de",

    "ard": "ard.de",

    "euronews": "euronews.com",

    "el pais": "elpais.com",

    "rtve": "rtve.es",

    "la vanguardia": "lavanguardia.com",

    "corriere della sera": "corriere.it",

    "la repubblica": "repubblica.it",

    "ansa": "ansa.it",

    "rainews": "rainews.it",


    # --------------------------------------------------------
    # BENELUX / SWITZERLAND
    # --------------------------------------------------------

    "nos": "nos.nl",

    "nrc": "nrc.nl",

    "de telegraaf": "telegraaf.nl",

    "vrt nws": "vrt.be",

    "rtbf": "rtbf.be",

    "le soir": "lesoir.be",

    "swissinfo": "swissinfo.ch",

    "srf news": "srf.ch",


    # --------------------------------------------------------
    # NORDIC
    # --------------------------------------------------------

    "svt": "svt.se",

    "nrk": "nrk.no",

    "dr news": "dr.dk",

    "yle": "yle.fi",

    "tv2 norway": "tv2.no",

    "aftenposten": "aftenposten.no",


    # --------------------------------------------------------
    # EASTERN EUROPE
    # --------------------------------------------------------

    "tvp info": "tvp.info",

    "tvp world": "tvpworld.com",

    "polsat news": "polsatnews.pl",

    "gazeta wyborcza": "wyborcza.pl",

    "ct24": "ct24.ceskatelevize.cz",

    "ceska televize": "ceskatelevize.cz",

    "ukrinform": "ukrinform.net",

    "kyiv independent": "kyivindependent.com",

    "unian": "unian.info",


    # --------------------------------------------------------
    # RUSSIA
    # --------------------------------------------------------

    "tass": "tass.com",

    "rt": "rt.com",

    "rt news": "rt.com",

    "interfax": "interfax.com",

    "moscow times": "themoscowtimes.com",


    # --------------------------------------------------------
    # CHINA / JAPAN / KOREA
    # --------------------------------------------------------

    "cgtn": "cgtn.com",

    "xinhua": "xinhuanet.com",

    "china daily": "chinadaily.com.cn",

    "global times": "globaltimes.cn",

    "nhk": "nhk.or.jp",

    "nhk world": "nhk.or.jp",

    "japan times": "japantimes.co.jp",

    "kyodo news": "kyodonews.net",

    "asahi shimbun": "asahi.com",

    "mainichi": "mainichi.jp",

    "yonhap": "yna.co.kr",

    "korea herald": "koreaherald.com",

    "kbs news": "kbs.co.kr",

    "jtbc": "jtbc.co.kr",


    # --------------------------------------------------------
    # SOUTHEAST ASIA
    # --------------------------------------------------------

    "channel news asia": "channelnewsasia.com",
    "cna": "channelnewsasia.com",

    "straits times": "straitstimes.com",

    "malay mail": "malaymail.com",

    "bernama": "bernama.com",

    "rappler": "rappler.com",

    "abs cbn news": "abs-cbn.com",

    "gma news": "gmanetwork.com",

    "philstar": "philstar.com",

    "bangkok post": "bangkokpost.com",

    "thai pbs": "thaipbs.or.th",

    "vnexpress": "vnexpress.net",

    "vietnam news": "vietnamnews.vn",

    "jakarta post": "thejakartapost.com",

    "kompas": "kompas.com",


    # --------------------------------------------------------
    # BANGLADESH / SRI LANKA / NEPAL
    # --------------------------------------------------------

    "bdnews24": "bdnews24.com",

    "prothom alo": "prothomalo.com",

    "dhaka tribune": "dhakatribune.com",

    "daily star bangladesh": "thedailystar.net",

    "daily mirror sri lanka": "dailymirror.lk",

    "news first sri lanka": "newsfirst.lk",

    "ada derana": "adaderana.lk",

    "kathmandu post": "kathmandupost.com",

    "onlinekhabar": "onlinekhabar.com",


    # --------------------------------------------------------
    # AFRICA
    # --------------------------------------------------------

    "sabc news": "sabcnews.com",

    "news24 south africa": "news24.com",

    "enca": "enca.com",

    "mail guardian south africa": "mg.co.za",

    "daily maverick": "dailymaverick.co.za",

    "citizen kenya": "citizen.digital",

    "nation africa": "nation.africa",

    "standard media kenya": "standardmedia.co.ke",

    "ntv kenya": "ntvkenya.co.ke",

    "the east african": "theeastafrican.co.ke",

    "pulse ghana": "pulse.com.gh",

    "ghanaweb": "ghanaweb.com",

    "myjoyonline": "myjoyonline.com",

    "daily graphic ghana": "graphic.com.gh",

    "premium times nigeria": "premiumtimesng.com",

    "channels tv nigeria": "channelstv.com",

    "thisday nigeria": "thisdaylive.com",

    "punch nigeria": "punchng.com",

    "the guardian nigeria": "guardian.ng",

    "vanguard nigeria": "vanguardngr.com",

    "daily trust nigeria": "dailytrust.com",

    "africa news": "africanews.com",

    "voa africa": "voanews.com",

    "allafrica": "allafrica.com",


    # --------------------------------------------------------
    # NORTH AFRICA
    # --------------------------------------------------------

    "egypt today": "egypttoday.com",

    "ahram online": "english.ahram.org.eg",

    "al masry al youm": "almasryalyoum.com",

    "morocco world news": "moroccoworldnews.com",

    "hespress": "hespress.com",

    "le360": "le360.ma",


    # --------------------------------------------------------
    # LATIN AMERICA
    # --------------------------------------------------------

    "televisa": "televisa.com",

    "univision": "univision.com",

    "telemundo": "telemundo.com",

    "reforma": "reforma.com",

    "milenio": "milenio.com",

    "el universal mexico": "eluniversal.com.mx",

    "clarin": "clarin.com",

    "la nacion argentina": "lanacion.com.ar",

    "infobae": "infobae.com",

    "pagina12": "pagina12.com.ar",

    "o globo": "oglobo.globo.com",

    "folha de sao paulo": "folha.uol.com.br",

    "estadao": "estadao.com.br",

    "g1 brasil": "g1.globo.com",

    "caracol noticias": "caracoltv.com",

    "el tiempo colombia": "eltiempo.com",

    "rcn noticias": "noticiasrcn.com",

    "el comercio peru": "elcomercio.pe",

    "el universo ecuador": "eluniverso.com",


    # --------------------------------------------------------
    # INTERNATIONAL
    # --------------------------------------------------------

    "associated press": "apnews.com",

    "ap": "apnews.com",

    "reuters": "reuters.com",

    "afp": "afp.com",

    "agence france presse": "afp.com",

    "voice of america": "voanews.com",

    "voa": "voanews.com",

    "radio free europe": "rferl.org",

    "radio free asia": "rfa.org",

    "un news": "news.un.org",

    "united nations news": "news.un.org",

}


# ============================================================
# MATRIX RAIN
# ============================================================

def matrix_rain(seconds=2.5):

    chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&@"

    width = shutil.get_terminal_size(
        (80, 24)
    ).columns

    end_time = time.time() + seconds

    while time.time() < end_time:

        line = "".join(
            random.choice(chars)
            for _ in range(width)
        )

        print(
            RED
            + line
            + RESET
        )

        time.sleep(0.025)

    os.system("clear")


# ============================================================
# BANNER
# ============================================================

def banner():

    print(
        RED
        + r"""
 ██████╗██╗  ██╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██╗
██╔════╝██║  ██║██╔══██╗████╗  ██║████╗  ██║██╔════╝██║
██║     ███████║███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██║
██║     ██╔══██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║
╚██████╗██║  ██║██║  ██║██║ ╚████║██║ ╚████║███████╗███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚══════╝
"""
        + RESET
    )

    print(
        CYAN
        + "                 CHANNEL INFO ENGINE"
        + RESET
    )

    print(
        YELLOW
        + "          WORLDWIDE NEWS WEBSITE SCANNER"
        + RESET
    )

    print()

    print(
        WHITE
        + "                 Made by DARK 47"
        + RESET
    )

    print()


# ============================================================
# DOMAIN NORMALIZATION
# ============================================================

def clean_domain(value):

    if not value:
        return ""

    value = value.strip().lower()

    if "://" not in value:

        value = "https://" + value

    try:

        parsed = urllib.parse.urlparse(
            value
        )

        host = parsed.hostname or ""

    except Exception:

        host = ""

    host = host.lower().strip()

    # www.example.com -> example.com

    if host.startswith("www."):

        host = host[4:]

    return host


# ============================================================
# SAFE FILE NAME
# ============================================================

def safe_filename(name):

    name = re.sub(
        r"[^a-zA-Z0-9._-]+",
        "_",
        name
    )

    return name[:100] or "channel_report"


# ============================================================
# APPROVED DOMAIN LIST
# ============================================================

def approved_domains():

    return {
        clean_domain(domain)
        for domain in KNOWN_CHANNELS.values()
    }


# ============================================================
# RESOLVE CHANNEL
# ============================================================

def resolve_channel(target):

    original = target.strip()

    if not original:

        return {
            "input": original,
            "name": None,
            "domain": None,
            "method": None,
            "approved": False
        }

    # Normalize channel name

    key = re.sub(
        r"\s+",
        " ",
        original.lower()
    ).strip()

    # --------------------------------------------------------
    # NAME
    # --------------------------------------------------------

    if key in KNOWN_CHANNELS:

        domain = clean_domain(
            KNOWN_CHANNELS[key]
        )

        return {
            "input": original,
            "name": key,
            "domain": domain,
            "method": "channel database",
            "approved": True
        }

    # --------------------------------------------------------
    # WEBSITE
    # --------------------------------------------------------

    domain = clean_domain(
        original
    )

    if domain in approved_domains():

        channel_name = None

        for name, known_domain in KNOWN_CHANNELS.items():

            if clean_domain(
                known_domain
            ) == domain:

                channel_name = name
                break

        return {
            "input": original,
            "name": channel_name,
            "domain": domain,
            "method": "approved news website",
            "approved": True
        }

    # --------------------------------------------------------
    # REJECT
    # --------------------------------------------------------

    return {
        "input": original,
        "name": None,
        "domain": None,
        "method": None,
        "approved": False
    }


# ============================================================
# DNS INFO
# ============================================================

def dns_info(domain):

    result = {
        "hostname": domain,
        "addresses": []
    }

    try:

        infos = socket.getaddrinfo(
            domain,
            443,
            type=socket.SOCK_STREAM
        )

        addresses = set()

        for item in infos:

            try:

                address = item[4][0]

                if address:
                    addresses.add(address)

            except Exception:
                pass

        result["addresses"] = sorted(
            addresses
        )

    except Exception as e:

        result["error"] = str(e)

    return result


# ============================================================
# DNS OVER HTTPS
# ============================================================

def doh_query(domain, record_type):

    url = (
        "https://cloudflare-dns.com/dns-query?"
        + urllib.parse.urlencode({
            "name": domain,
            "type": record_type
        })
    )

    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/dns-json",
            "User-Agent": USER_AGENT
        }
    )

    try:

        with urllib.request.urlopen(
            request,
            timeout=10
        ) as response:

            data = response.read().decode(
                "utf-8",
                errors="ignore"
            )

            return json.loads(
                data
            )

    except Exception as e:

        return {
            "error": str(e)
        }


# ============================================================
# DNS RECORDS
# ============================================================

def collect_dns_records(domain):

    records = {}

    for record_type in [
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT"
    ]:

        records[record_type] = doh_query(
            domain,
            record_type
        )

    return records


# ============================================================
# IP / ASN / ISP INFORMATION
# ============================================================

def ip_information(domain):

    result = {}

    dns = dns_info(
        domain
    )

    addresses = dns.get(
        "addresses",
        []
    )

    result["resolved_ips"] = addresses

    if not addresses:

        return result

    # Query every resolved IP, but limit
    # to avoid unnecessary requests.

    ip_results = []

    for ip in addresses[:5]:

        try:

            url = (
                "https://ipwho.is/"
                + urllib.parse.quote(ip)
            )

            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": USER_AGENT
                }
            )

            with urllib.request.urlopen(
                request,
                timeout=10
            ) as response:

                data = response.read().decode(
                    "utf-8",
                    errors="ignore"
                )

                parsed = json.loads(
                    data
                )

                ip_results.append(
                    parsed
                )

        except Exception as e:

            ip_results.append({
                "ip": ip,
                "error": str(e)
            })

    result["ip_details"] = ip_results

    return result


# ============================================================
# HTTP / HTTPS INFORMATION
# ============================================================

def http_information(domain):

    result = {
        "https": {},
        "http": {}
    }

    for scheme in [
        "https",
        "http"
    ]:

        url = (
            f"{scheme}://{domain}/"
        )

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT
            },
            method="GET"
        )

        try:

            with urllib.request.urlopen(
                request,
                timeout=12
            ) as response:

                headers = dict(
                    response.headers
                )

                result[scheme] = {

                    "final_url":
                        response.geturl(),

                    "status":
                        response.status,

                    "server":
                        headers.get(
                            "Server"
                        ),

                    "content_type":
                        headers.get(
                            "Content-Type"
                        ),

                    "content_length":
                        headers.get(
                            "Content-Length"
                        ),

                    "location":
                        headers.get(
                            "Location"
                        ),

                    "headers":
                        headers,

                    "security_headers": {

                        "strict_transport_security":
                            headers.get(
                                "Strict-Transport-Security"
                            ),

                        "content_security_policy":
                            headers.get(
                                "Content-Security-Policy"
                            ),

                        "x_content_type_options":
                            headers.get(
                                "X-Content-Type-Options"
                            ),

                        "x_frame_options":
                            headers.get(
                                "X-Frame-Options"
                            ),

                        "referrer_policy":
                            headers.get(
                                "Referrer-Policy"
                            ),

                        "permissions_policy":
                            headers.get(
                                "Permissions-Policy"
                            )
                    }
                }

        except urllib.error.HTTPError as e:

            result[scheme] = {

                "status": e.code,

                "headers":
                    dict(e.headers)
                    if e.headers
                    else {},

                "error":
                    str(e)
            }

        except Exception as e:

            result[scheme] = {
                "error": str(e)
            }

    return result


# ============================================================
# TLS / SSL INFORMATION
# ============================================================

def ssl_information(domain):

    result = {}

    context = ssl.create_default_context()

    try:

        with socket.create_connection(
            (domain, 443),
            timeout=10
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as secure_socket:

                certificate = (
                    secure_socket.getpeercert()
                )

                result = {

                    "tls_version":
                        secure_socket.version(),

                    "cipher":
                        secure_socket.cipher(),

                    "certificate_subject":
                        certificate.get(
                            "subject"
                        ),

                    "certificate_issuer":
                        certificate.get(
                            "issuer"
                        ),

                    "certificate_serial":
                        certificate.get(
                            "serialNumber"
                        ),

                    "certificate_not_before":
                        certificate.get(
                            "notBefore"
                        ),

                    "certificate_not_after":
                        certificate.get(
                            "notAfter"
                        )
                }

    except Exception as e:

        result["error"] = str(e)

    return result


# ============================================================
# CDN DETECTION
# ============================================================

def detect_cdn(http_data):

    headers = {}

    try:

        headers = (
            http_data
            .get("https", {})
            .get("headers", {})
        )

    except Exception:
        pass

    joined = " ".join(
        f"{str(k)}:{str(v)}"
        for k, v in headers.items()
    ).lower()

    providers = []

    checks = {

        "Cloudflare": [
            "cloudflare",
            "cf-ray"
        ],

        "Akamai": [
            "akamai",
            "x-akamai"
        ],

        "Fastly": [
            "fastly",
            "x-served-by"
        ],

        "Amazon CloudFront": [
            "cloudfront",
            "x-amz-cf"
        ],

        "Google Cloud": [
            "gfe",
            "google"
        ]
    }

    for provider, keywords in checks.items():

        for keyword in keywords:

            if keyword in joined:

                providers.append(
                    provider
                )

                break

    return {
        "detected": sorted(
            set(providers)
        )
    }


# ============================================================
# WHOIS
# ============================================================

def whois_information(domain):

    if shutil.which("whois") is None:

        return {

            "available": False,

            "message":
                "whois command not installed"
        }

    try:

        process = subprocess.run(

            [
                "whois",
                domain
            ],

            capture_output=True,

            text=True,

            timeout=15
        )

        return {

            "available": True,

            "return_code":
                process.returncode,

            "output":
                (
                    process.stdout
                    or process.stderr
                )[:12000]
        }

    except Exception as e:

        return {

            "available": True,

            "error": str(e)
        }


# ============================================================
# SAVE REPORT
# ============================================================

def save_report(report):

    os.makedirs(
        REPORT_DIR,
        exist_ok=True
    )

    channel = report.get(
        "channel",
        {}
    )

    name = (
        channel.get("name")
        or channel.get("domain")
        or "channel"
    )

    filename = (
        safe_filename(name)
        + "_"
        + datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        + ".json"
    )

    path = os.path.join(
        REPORT_DIR,
        filename
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False
        )

    return path


# ============================================================
# DISPLAY HELPERS
# ============================================================

def print_section(title):

    print()

    print(
        CYAN
        + "╔"
        + "═" * 62
        + "╗"
        + RESET
    )

    print(
        CYAN
        + "║ "
        + WHITE
        + title
        + CYAN
        + " " * max(
            0,
            60 - len(title)
        )
        + "║"
        + RESET
    )

    print(
        CYAN
        + "╚"
        + "═" * 62
        + "╝"
        + RESET
    )


# ============================================================
# DISPLAY FULL ORIGINAL-STYLE RESULT
# ============================================================

def display_report(report):

    channel = report.get(
        "channel",
        {}
    )

    print()

    print(
        RED
        + "=" * 66
        + RESET
    )

    print(
        GREEN
        + "                 CHANNEL SCAN RESULT"
        + RESET
    )

    print(
        RED
        + "=" * 66
        + RESET
    )

    print()

    print(
        WHITE
        + "CHANNEL"
        + RESET
        + "       : "
        + str(
            channel.get(
                "name"
            )
        )
    )

    print(
        WHITE
        + "DOMAIN"
        + RESET
        + "        : "
        + str(
            channel.get(
                "domain"
            )
        )
    )

    print(
        WHITE
        + "METHOD"
        + RESET
        + "        : "
        + str(
            channel.get(
                "method"
            )
        )
    )

    print(
        WHITE
        + "SCAN TIME"
        + RESET
        + "      : "
        + str(
            report.get(
                "scan_time_utc"
            )
        )
    )


    # --------------------------------------------------------
    # DNS
    # --------------------------------------------------------

    print_section(
        "DNS INFORMATION"
    )

    dns = report.get(
        "dns",
        {}
    )

    print(
        "Hostname :",
        dns.get(
            "hostname"
        )
    )

    print(
        "Addresses:"
    )

    for address in dns.get(
        "addresses",
        []
    ):

        print(
            "  └─",
            address
        )

    if dns.get("error"):

        print(
            RED
            + "Error:"
            + RESET,
            dns["error"]
        )


    # --------------------------------------------------------
    # DNS RECORDS
    # --------------------------------------------------------

    print_section(
        "DNS RECORDS"
    )

    records = report.get(
        "dns_records",
        {}
    )

    for record_type, data in records.items():

        print()

        print(
            YELLOW
            + record_type
            + RESET
        )

        if isinstance(
            data,
            dict
        ):

            answers = data.get(
                "Answer",
                []
            )

            if answers:

                for answer in answers:

                    print(
                        "  ",
                        answer.get(
                            "data"
                        )
                    )

            elif data.get("error"):

                print(
                    "  Error:",
                    data.get(
                        "error"
                    )
                )

            else:

                print(
                    "  No record returned."
                )


    # --------------------------------------------------------
    # IP / ASN / ISP
    # --------------------------------------------------------

    print_section(
        "IP / ASN / ISP INFORMATION"
    )

    ip_data = report.get(
        "ip_information",
        {}
    )

    print(
        "Resolved IPs:"
    )

    for ip in ip_data.get(
        "resolved_ips",
        []
    ):

        print(
            "  └─",
            ip
        )

    for item in ip_data.get(
        "ip_details",
        []
    ):

        print()

        if item.get("ip"):

            print(
                "IP:",
                item.get("ip")
            )

        print(
            "Success:",
            item.get("success")
        )

        print(
            "Type:",
            item.get("type")
        )

        print(
            "Continent:",
            item.get("continent")
        )

        print(
            "Country:",
            item.get("country")
        )

        print(
            "Region:",
            item.get("region")
        )

        print(
            "City:",
            item.get("city")
        )

        print(
            "ISP:",
            item.get("connection", {}).get(
                "isp"
            )
        )

        print(
            "Organization:",
            item.get("connection", {}).get(
                "org"
            )
        )

        print(
            "ASN:",
            item.get("connection", {}).get(
                "asn"
            )
        )


    # --------------------------------------------------------
    # HTTP / HTTPS
    # --------------------------------------------------------

    print_section(
        "HTTP / HTTPS INFORMATION"
    )

    http = report.get(
        "http",
        {}
    )

    for scheme in [
        "https",
        "http"
    ]:

        data = http.get(
            scheme,
            {}
        )

        print()

        print(
            MAGENTA
            + scheme.upper()
            + RESET
        )

        print(
            "Status:",
            data.get(
                "status"
            )
        )

        print(
            "Final URL:",
            data.get(
                "final_url"
            )
        )

        print(
            "Server:",
            data.get(
                "server"
            )
        )

        print(
            "Content-Type:",
            data.get(
                "content_type"
            )
        )

        security = data.get(
            "security_headers",
            {}
        )

        print(
            "HSTS:",
            security.get(
                "strict_transport_security"
            )
        )

        print(
            "CSP:",
            security.get(
                "content_security_policy"
            )
        )

        print(
            "X-Content-Type-Options:",
            security.get(
                "x_content_type_options"
            )
        )

        print(
            "X-Frame-Options:",
            security.get(
                "x_frame_options"
            )
        )

        print(
            "Referrer-Policy:",
            security.get(
                "referrer_policy"
            )
        )

        print(
            "Permissions-Policy:",
            security.get(
                "permissions_policy"
            )
        )


    # --------------------------------------------------------
    # TLS
    # --------------------------------------------------------

    print_section(
        "SSL / TLS INFORMATION"
    )

    tls = report.get(
        "tls",
        {}
    )

    print(
        "TLS Version:",
        tls.get(
            "tls_version"
        )
    )

    print(
        "Cipher:",
        tls.get(
            "cipher"
        )
    )

    print(
        "Certificate Subject:",
        tls.get(
            "certificate_subject"
        )
    )

    print(
        "Certificate Issuer:",
        tls.get(
            "certificate_issuer"
        )
    )

    print(
        "Serial:",
        tls.get(
            "certificate_serial"
        )
    )

    print(
        "Valid From:",
        tls.get(
            "certificate_not_before"
        )
    )

    print(
        "Valid Until:",
        tls.get(
            "certificate_not_after"
        )
    )


    # --------------------------------------------------------
    # CDN
    # --------------------------------------------------------

    print_section(
        "CDN DETECTION"
    )

    cdn = report.get(
        "cdn",
        {}
    )

    detected = cdn.get(
        "detected",
        []
    )

    if detected:

        for provider in detected:

            print(
                GREEN
                + "[+] "
                + RESET
                + provider
            )

    else:

        print(
            "No known CDN detected."
        )


    # --------------------------------------------------------
    # WHOIS
    # --------------------------------------------------------

    print_section(
        "WHOIS INFORMATION"
    )

    whois = report.get(
        "whois",
        {}
    )

    if whois.get(
        "available"
    ):

        output = whois.get(
            "output",
            ""
        )

        if output:

            print(
                output
            )

        elif whois.get(
            "error"
        ):

            print(
                RED
                + "WHOIS Error:"
                + RESET,
                whois.get(
                    "error"
                )
            )

        else:

            print(
                "No WHOIS output."
            )

    else:

        print(
            whois.get(
                "message",
                "WHOIS unavailable."
            )
        )


    # --------------------------------------------------------
    # REPORT
    # --------------------------------------------------------

    print()

    print(
        RED
        + "=" * 66
        + RESET
    )

    print(
        GREEN
        + "[+] FULL REPORT SAVED"
        + RESET
    )

    print(
        WHITE
        + "FILE:"
        + RESET,
        report.get(
            "report_file"
        )
    )

    print(
        RED
        + "=" * 66
        + RESET
    )


# ============================================================
# SCAN CHANNEL
# ============================================================

def scan_channel():

    print()

    print(
        CYAN
        + "ENTER NEWS CHANNEL NAME OR WEBSITE"
        + RESET
    )

    print(
        DIM
        + "Examples: CNN | BBC News | Al Jazeera | cnn.com"
        + RESET
    )

    print()

    target = input(
        YELLOW
        + "CHANNEL > "
        + RESET
    ).strip()

    if not target:

        print(
            RED
            + "[X] Empty input."
            + RESET
        )

        return

    resolved = resolve_channel(
        target
    )

    # --------------------------------------------------------
    # STRICT NEWS-ONLY BLOCK
    # --------------------------------------------------------

    if not resolved.get(
        "approved"
    ):

        print()

        print(
            RED
            + "╔══════════════════════════════════════════════╗"
            + RESET
        )

        print(
            RED
            + "║              ACCESS REJECTED                ║"
            + RESET
        )

        print(
            RED
            + "╚══════════════════════════════════════════════╝"
            + RESET
        )

        print()

        print(
            WHITE
            + "This website is not in the approved"
            + RESET
        )

        print(
            WHITE
            + "worldwide news-channel database."
            + RESET
        )

        print()

        print(
            DIM
            + "Only approved news websites can be scanned."
            + RESET
        )

        return


    domain = resolved.get(
        "domain"
    )


    # --------------------------------------------------------
    # APPROVED
    # --------------------------------------------------------

    print()

    print(
        GREEN
        + "[+] NEWS WEBSITE APPROVED"
        + RESET
    )

    print(
        "Channel:",
        resolved.get(
            "name"
        )
    )

    print(
        "Domain:",
        domain
    )

    print()

    print(
        CYAN
        + "[*] Starting public information scan..."
        + RESET
    )


    report = {

        "tool":
            "CHANNEL INFO ENGINE",

        "version":
            "3.0",

        "author":
            "DARK 47",

        "scan_time_utc":
            datetime.now(
                timezone.utc
            ).isoformat(),

        "channel":
            resolved,

        "dns": {},

        "dns_records": {},

        "ip_information": {},

        "http": {},

        "tls": {},

        "cdn": {},

        "whois": {}
    }


    # --------------------------------------------------------
    # DNS
    # --------------------------------------------------------

    print(
        CYAN
        + "[1/7] DNS information..."
        + RESET
    )

    report["dns"] = dns_info(
        domain
    )


    # --------------------------------------------------------
    # DNS RECORDS
    # --------------------------------------------------------

    print(
        CYAN
        + "[2/7] DNS records..."
        + RESET
    )

    report["dns_records"] = (
        collect_dns_records(
            domain
        )
    )


    # --------------------------------------------------------
    # IP / ASN / ISP
    # --------------------------------------------------------

    print(
        CYAN
        + "[3/7] IP / ASN / ISP..."
        + RESET
    )

    report["ip_information"] = (
        ip_information(
            domain
        )
    )


    # --------------------------------------------------------
    # HTTP / HTTPS
    # --------------------------------------------------------

    print(
        CYAN
        + "[4/7] HTTP / HTTPS..."
        + RESET
    )

    report["http"] = (
        http_information(
            domain
        )
    )


    # --------------------------------------------------------
    # TLS
    # --------------------------------------------------------

    print(
        CYAN
        + "[5/7] SSL / TLS..."
        + RESET
    )

    report["tls"] = (
        ssl_information(
            domain
        )
    )


    # --------------------------------------------------------
    # CDN
    # --------------------------------------------------------

    print(
        CYAN
        + "[6/7] CDN detection..."
        + RESET
    )

    report["cdn"] = (
        detect_cdn(
            report["http"]
        )
    )


    # --------------------------------------------------------
    # WHOIS
    # --------------------------------------------------------

    print(
        CYAN
        + "[7/7] WHOIS..."
        + RESET
    )

    report["whois"] = (
        whois_information(
            domain
        )
    )


    # --------------------------------------------------------
    # SAVE
    # --------------------------------------------------------

    path = save_report(
        report
    )

    report["report_file"] = path


    # Save final report with path

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False
        )


    # --------------------------------------------------------
    # SHOW FULL RESULT
    # --------------------------------------------------------

    display_report(
        report
    )


# ============================================================
# SAVED REPORTS
# ============================================================

def saved_reports():

    print()

    print_section(
        "SAVED CHANNEL REPORTS"
    )

    if not os.path.exists(
        REPORT_DIR
    ):

        print(
            YELLOW
            + "No reports found."
            + RESET
        )

        return


    files = sorted(
        [
            file
            for file in os.listdir(
                REPORT_DIR
            )
            if file.endswith(
                ".json"
            )
        ]
    )


    if not files:

        print(
            YELLOW
            + "No reports found."
            + RESET
        )

        return


    for index, filename in enumerate(
        files,
        1
    ):

        print(
            f"{index}. {filename}"
        )


# ============================================================
# ABOUT
# ============================================================

def about():

    print_section(
        "ABOUT CHANNEL INFO"
    )

    print(
        "CHANNEL INFO ENGINE"
    )

    print(
        "Worldwide approved-news website scanner"
    )

    print()

    print(
        "Public information collected:"
    )

    print(
        "• DNS"
    )

    print(
        "• DNS Records"
    )

    print(
        "• IP addresses"
    )

    print(
        "• ASN / ISP information"
    )

    print(
        "• HTTP / HTTPS headers"
    )

    print(
        "• TLS certificate information"
    )

    print(
        "• CDN detection"
    )

    print(
        "• WHOIS"
    )

    print(
        "• JSON reports"
    )

    print()

    print(
        RED
        + "Random websites are rejected."
        + RESET
    )

    print()

    print(
        WHITE
        + "Made by DARK 47"
        + RESET
    )


# ============================================================
# MENU
# ============================================================

def menu():

    while True:

        print()

        print(
            RED
            + "╔════════════════════════════════════════════╗"
            + RESET
        )

        print(
            RED
            + "║          CHANNEL INFO ENGINE               ║"
            + RESET
        )

        print(
            RED
            + "╠════════════════════════════════════════════╣"
            + RESET
        )

        print(
            WHITE
            + "║  1. CHANNEL INFO                          ║"
            + RESET
        )

        print(
            WHITE
            + "║  2. SAVED REPORTS                         ║"
            + RESET
        )

        print(
            WHITE
            + "║  3. ABOUT                                 ║"
            + RESET
        )

        print(
            WHITE
            + "║  0. EXIT                                  ║"
            + RESET
        )

        print(
            RED
            + "╚════════════════════════════════════════════╝"
            + RESET
        )

        print()

        choice = input(
            YELLOW
            + "Channel info @ Dark 47> "
            + RESET
        ).strip()


        if choice == "1":

            scan_channel()


        elif choice == "2":

            saved_reports()


        elif choice == "3":

            about()


        elif choice == "0":

            print()

            print(
                GREEN
                + "CHANNEL INFO SHUTDOWN."
                + RESET
            )

            break


        else:

            print()

            print(
                RED
                + "Invalid option."
                + RESET
            )


# ============================================================
# MAIN
# ============================================================

def main():

    try:

        matrix_rain()

        banner()

        menu()

    except KeyboardInterrupt:

        print()

        print(
            RED
            + "Interrupted."
            + RESET
        )

    except Exception as e:

        print()

        print(
            RED
            + "Unexpected error:"
            + RESET,
            e
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    main()
