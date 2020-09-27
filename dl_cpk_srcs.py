from bs4 import BeautifulSoup
import re
import requests

import os

#credit https://gist.github.com/gruber/249502
urlregex = r"""(?xi)
\b
(                           # Capture 1: entire matched URL
  (?:
    [a-z][\w-]+:                # URL protocol and colon
    (?:
      /{1,3}                        # 1-3 slashes
      |                             #   or
      [a-z0-9%]                     # Single letter or digit or '%'
                                    # (Trying not to match e.g. "URI::Escape")
    )
    |                           #   or
    www\d{0,3}[.]               # "www.", "www1.", "www2." ... "www999."
    |                           #   or
    [a-z0-9.\-]+[.][a-z]{2,4}/  # looks like domain name followed by a slash
  )
  (?:                           # One or more:
    [^\s()<>]+                      # Run of non-space, non-()<>
    |                               #   or
    \(([^\s()<>]+|(\([^\s()<>]+\)))*\)  # balanced parens, up to 2 levels
  )+
  (?:                           # End with:
    \(([^\s()<>]+|(\([^\s()<>]+\)))*\)  # balanced parens, up to 2 levels
    |                                   #   or
    [^\s`!()\[\]{};:'".,<>?]        # not a space or one of these punct chars
  )
)"""
regex = re.compile(urlregex)

url = "https://www.mediafire.com/file/o0wirp8aepbjy80/vox-cpk.pth.tar/file"
s = requests.session()
result = s.get(url)

soup = BeautifulSoup(result.content, 'html.parser')

div_tag = soup.find_all("div", class_="download_link")
cpks_link = re.findall(regex, str(div_tag[0].contents))[0][0]

src_vid_link = "https://cdn.discordapp.com/attachments/620751621592449055/738487948252676217/bakamitai_template.mp4"

src_aud_link = "https://cdn.discordapp.com/attachments/758371620531732531/759696211157581844/dmdn.mp3"

if not os.path.isfile("vox-cpk.pth.tar"):
    print("Downloading checkpoints...")
    with open("vox-cpk.pth.tar", "wb") as f:
        cpk_fille = requests.get(cpks_link, allow_redirects=True)
        f.write(cpk_fille.content)
else:
    print("Checkpoints are already downloaded.")

if not os.path.isfile("bakamitai_template.mp4"):
    print("Downloading template video...")
    with open("bakamitai_template.mp4", "wb") as f:
        src_vid_fille = requests.get(src_vid_link, allow_redirects=True)
        f.write(src_vid_fille.content)
else:
    print("Template is already downloaded.")
    
if not os.path.isfile("dmdn.mp3"):
    print("Downloading Baka Mitai audio...")
    with open("dmdn.mp3", "wb") as f:
        src_aud_fille = requests.get(src_aud_link, allow_redirects=True)
        f.write(src_aud_fille.content)
else:
    print("Baka Mitai audio is already downloaded.")
