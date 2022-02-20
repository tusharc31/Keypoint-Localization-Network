import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import torch.optim as optim
import os
import pandas as pd
from torchvision.io import read_image

import requests
import shutil

headers = {"Host": "iiitaphyd-my.sharepoint.com",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://iiitaphyd-my.sharepoint.com/personal/robotics_iiit_ac_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Frobotics%5Fiiit%5Fac%5Fin%2FDocuments%2FDRACO%2Fcar%5Freflection%5Fcanonical%5Fwo%5Fdepth%2Ezip&parent=%2Fpersonal%2Frobotics%5Fiiit%5Fac%5Fin%2FDocuments%2FDRACO&originalPath=aHR0cHM6Ly9paWl0YXBoeWQtbXkuc2hhcmVwb2ludC5jb20vOnU6L2cvcGVyc29uYWwvcm9ib3RpY3NfaWlpdF9hY19pbi9FZW45d1NBX1BZbEhoZUlXcGpweV9XTUJ1Tl9VdTR3bXlzaVd5VGFDLU5KWTB3P3J0aW1lPTR6X2Itcnh2MlVn",
"DNT": "1",
"Connection": "keep-alive",
"Cookie": "FedAuth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+VjExLDBoLmZ8bWVtYmVyc2hpcHx1cm4lM2FzcG8lM2Fhbm9uIzY0YTFkZjc1NmMzNzYyNDhkMzFiMmE1MGE5YTE4YzY0MTRjNmFjOGRmNDdhNjBkYTViYWUyNjY4OTBmOWJlYTUsMCMuZnxtZW1iZXJzaGlwfHVybiUzYXNwbyUzYWFub24jNjRhMWRmNzU2YzM3NjI0OGQzMWIyYTUwYTlhMThjNjQxNGM2YWM4ZGY0N2E2MGRhNWJhZTI2Njg5MGY5YmVhNSwxMzI3NTI0NTA3MDAwMDAwMDAsMCwxMzI3NTMzMTE3MDI1MzA3ODAsMC4wLjAuMCwyNTgsNTJlMmE4MzYtNDg2My00NWJmLWFhODItYjAyNTkxZjZjNTY4LCwsNjIzYmVjOWYtMDAzNC0wMDAwLWFkNDctYTE5YjQ1Y2RlYTQ2LDYyM2JlYzlmLTAwMzQtMDAwMC1hZDQ3LWExOWI0NWNkZWE0Nix4UUQzUVBIcjFrR0NkbGQ0b01oWVN3LDAsMCwwLCwsLDI2NTA0Njc3NDM5OTk5OTk5OTksMCwsLCwsLCwwLFRLUXJ3TUJZR21zaVlOZzQvVXZVYUNwV3JvckFCRHFBbFY3S3JFU2hIY1NmdDBVZGZVcGx1QU9XN2lBSTE3Y2VPNDg2bks3QVNFeVplNUhtKzcxNUdTNDZRQzFsbHdoQkdaQVNwcm1hTnBPeUVNQ2RrSW9mZnRIaEFJK2ppQlk4Wk9TSVl4emtOUFZjT2hSN3RLZzI5NkRKcFFoakphSGxHRE9WS2ZVa3VUZHJMYVVINmFBU1hONUdOd09ZczBGZVA0cmQ0d2E5ZGVNcmFuN2d1RFhoTmhZWkFFUUJ3S2Z5eUxxcGQ0K0puWGxqTUQrMC9TS3dWZHFyOFpjV0FxV005djB0WEkvRXhVN1FEM1JwWGd1RHVZZHdNMEVqcmRBNkF3WmlnK1VVajdybTNHSkJSU1RPMk8raDZlUlQ1MnVEd3BQWXFLalBOcW5LbW9zY1FvVXdJUT09PC9TUD4=",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "iframe",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-GPC": "1"}

r = requests.get("https://iiitaphyd-my.sharepoint.com/personal/robotics_iiit_ac_in/_layouts/15/download.aspx?SourceUrl=/personal/robotics_iiit_ac_in/Documents/DRACO/car_reflection_canonical_wo_depth.zip",headers=headers, stream=True)

path=f"./car_reflection_canonical.zip"
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f) 

#!unzip car_reflection_canonical.zip
#!ls

