🌍 CHANNEL INFO ENGINE

Worldwide News Channel & Website Information Scanner

Made by DARK 47

---

📡 About

CHANNEL INFO ENGINE is a Python-based Termux tool designed to identify and inspect approved news channels and news websites from around the world.

The tool accepts a news channel name, domain, or URL and displays detailed publicly available technical information.

It is designed specifically for news websites/channels, rather than acting as a general-purpose website scanner.

---

✨ Features

- 🌍 Worldwide news-source database
- 📺 TV news channels
- 📰 Newspapers and online news websites
- 🔎 Search by channel name
- 🌐 Search by domain
- 🔗 Full URL support
- 🧹 URL/domain normalization
- 🚫 Rejects non-approved/random websites
- 📡 DNS information
- 🔎 DNS records
- 🌐 IP information
- 🏢 ASN / ISP information
- 🔐 HTTP / HTTPS information
- 🛡️ Security headers
- 🔒 SSL/TLS certificate information
- ☁️ CDN detection
- 📋 WHOIS information when available
- 💾 JSON report saving  

---

🌎 Worldwide News Sources

The database contains news sources from multiple countries and regions.

🇵🇰 Pakistan

- Geo News
- ARY News
- Samaa TV
- Dunya News
- Express News
- BOL News
- Aaj News
- 92 News
- HUM News
- GNN
- PTV News
- Dawn
- The News International
- The Nation
- Business Recorder
- Pakistan Today
- Express Tribune
- Nawaiwaqt
- Daily Times

🇮🇳 India

- NDTV
- Aaj Tak
- India Today
- News18
- Times Now
- Times of India
- The Hindu
- Hindustan Times
- Republic
- Zee News
- WION
- ABP News
- TV9
- India TV
- News24
- News Nation
- Firstpost
- The Print
- Scroll
- The Wire
- Deccan Herald
- Deccan Chronicle
- Telegraph India
- Financial Express
- Business Standard

🇺🇸 United States

- CNN
- Fox News
- MSNBC
- ABC News
- CBS News
- NBC News
- PBS
- NPR
- AP News
- Reuters
- Bloomberg
- New York Times
- Washington Post
- Wall Street Journal
- USA Today
- Newsweek
- TIME
- Politico
- The Hill
- Axios
- CNBC
- Forbes
- Newsmax

🇬🇧 United Kingdom

- BBC News
- Sky News
- ITV News
- Channel 4 News
- Channel 5
- The Guardian
- The Independent
- The Telegraph
- The Times
- Financial Times
- Daily Mail
- Daily Mirror
- Daily Express
- Evening Standard
- GB News

🇮🇱 Israel

- i24NEWS
- Times of Israel
- Jerusalem Post
- Haaretz
- Israel Hayom
- Channel 12 / Mako
- N12
- Kan News
- Israel National News
- Ynet

🌍 Middle East

- Al Jazeera
- Al Arabiya
- Al Hadath
- Sky News Arabia
- Arab News
- Gulf News
- Khaleej Times
- The National UAE
- Middle East Eye
- Al-Monitor
- Asharq Al-Awsat
- Asharq News
- LBC International
- Al Araby
- Al Mayadeen

🇨🇦 Canada

- CBC News
- CTV News
- Global News
- CityNews
- Toronto Star
- National Post
- The Globe and Mail

🇦🇺 Australia / 🇳🇿 New Zealand

- ABC News Australia
- SBS News
- News.com.au
- The Australian
- Nine News
- Seven News
- Sky News Australia
- Stuff
- RNZ
- 1News
- NZ Herald

🇹🇷 Turkey

- TRT World
- TRT Haber
- Anadolu Agency
- Hürriyet
- Daily Sabah
- HaberTürk
- NTV

🇫🇷 France

- France 24
- RFI
- Le Monde
- Le Figaro

🇩🇪 Germany

- Deutsche Welle
- Der Spiegel
- Tagesschau
- ZDF
- ARD

🇪🇸 Spain

- El País
- RTVE
- La Vanguardia

🇮🇹 Italy

- Corriere della Sera
- La Repubblica
- ANSA
- RaiNews

🌏 Asia

- CGTN
- Xinhua
- China Daily
- Global Times
- NHK
- NHK World
- Japan Times
- Kyodo News
- Asahi Shimbun
- Mainichi
- Yonhap
- Korea Herald
- KBS
- JTBC
- Channel NewsAsia
- The Straits Times
- Malay Mail
- Bernama
- Rappler
- ABS-CBN News
- GMA News
- Philstar
- Bangkok Post
- Thai PBS
- VnExpress
- Vietnam News
- Jakarta Post
- Kompas

🌍 Africa

- SABC News
- News24 South Africa
- eNCA
- Mail & Guardian
- Daily Maverick
- Citizen Kenya
- Nation Africa
- Standard Media Kenya
- NTV Kenya
- The East African
- Pulse Ghana
- GhanaWeb
- MyJoyOnline
- Daily Graphic
- Premium Times Nigeria
- Channels TV
- ThisDay
- Punch
- Guardian Nigeria
- Vanguard
- Daily Trust
- Africa News
- VOA Africa
- AllAfrica

🌎 Latin America

- Televisa
- Univision
- Telemundo
- Reforma
- Milenio
- El Universal
- Clarín
- La Nación
- Infobae
- Página/12
- O Globo
- Folha de S.Paulo
- Estadão
- G1
- Caracol Noticias
- El Tiempo
- RCN Noticias
- El Comercio
- El Universo

🌐 International

- Associated Press
- Reuters
- AFP
- Voice of America
- RFE/RL
- Radio Free Asia
- UN News

«The database is curated and can be expanded with additional legitimate news sources.»

---

📸 Screenshot

"CHANNEL INFO ENGINE Screenshot" (Screenshot_20260913_105737_Termux.jpg)

---

📱 Installation on Termux

1. Update Termux

Open Termux and run:

pkg upgrade -y

2. Install Python and Git

pkg install python git -y

Check the installation:

python --version

git --version

---

📥 Download from GitHub

Clone the official repository:

git clone https://github.com/darkfourty7-cyberwarrior/CHANNEL-INFO.git

Enter the project:

cd CHANNEL-INFO

---

▶️ Run the Tool

The main file is:

Channel info.py

Run:

python "Channel info.py"

---

🔎 Usage Examples

Enter a channel name:

CNN

Enter a domain:

cnn.com

Enter a full URL:

https://www.cnn.com/world

Other examples:

BBC News

Al Jazeera

Reuters

---

✅ Accepted Input

CNN                 ✅
cnn.com             ✅
https://cnn.com     ✅
BBC News            ✅
Al Jazeera          ✅
Reuters             ✅

The tool normalizes the input and checks it against the approved news-source database.

---

🚫 Non-News Websites

The tool is focused on approved news sources.

Random or non-approved domains are rejected.

Example:

random-site.com       ❌
example.com            ❌
unknown-domain.com     ❌

---

📊 Scan Information

For an approved public news website, the tool can display detailed information.

DNS INFORMATION

- Hostname
- Resolved addresses
- DNS status

DNS RECORDS

- A
- AAAA
- MX
- NS
- TXT

IP / NETWORK INFORMATION

- Public IP
- ASN
- ISP
- Network information
- Country information when available

HTTP / HTTPS INFORMATION

- HTTP status
- HTTPS status
- Response information
- HTTP headers
- Security headers

SSL / TLS INFORMATION

- TLS version
- Cipher
- Certificate subject
- Certificate issuer
- Certificate serial
- Valid-from date
- Valid-until date

CDN DETECTION

The tool attempts to identify commonly used CDN/network providers.

WHOIS INFORMATION

WHOIS information is displayed when available.

If WHOIS is unavailable, the rest of the scan can continue normally.

---

💾 Reports

Scan reports are saved locally in:

channel_info_reports/

Example:

channel_info_reports/cnn_com.json

Reports contain information collected during the scan.

---

🔄 Update the Tool

To update the project:

cd CHANNEL-INFO
git pull

Then run:

python "Channel info.py"

---

🗑️ Remove the Tool

To remove the project from Termux:

cd ..
rm -rf CHANNEL-INFO

---

🛠️ Requirements

- Android
- Termux
- Python 3
- Git
- Internet connection

---

⚠️ Disclaimer

CHANNEL INFO ENGINE is intended for authorized research, public-information gathering, and technical inspection of public news websites.

The tool does not provide:

- Authentication bypass
- Password theft
- Credential harvesting
- Exploitation
- Unauthorized system access
- Private-data access
- Security-control bypass

Use the tool responsibly and only against systems and information you are authorized to inspect.

---

👤 Author

DARK 47

CHANNEL INFO ENGINE

🌍 Worldwide News
📡 Channel Information
🌐 Website Information
🔎 Public Technical Data

---

⭐ GitHub Repository

Official repository:

https://github.com/darkfourty7-cyberwarrior/CHANNEL-INFO

If you find the project useful, consider giving the repository a ⭐.

---

Made by DARK 47
