import os

import qrcode
from PIL.ImageQt import ImageQt, Image

from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout
from PySide6.QtCore import QEvent, Qt, Signal
from PySide6.QtGui import QPixmap

from widget.SvgButton import SvgButton
from ui.ui_donations import Ui_Form
from clipboard import *

crypt_addresses = {
    "Adcoin": "AYzMqvwQ6HGBRpsMahW7tCtHm6vmgoKkpf",
    "Akash-Network": "akash1m0aarljq5j5v2ckh2j7tu46fhw0kwzykf2ed5d",
    "Algorand": "OXA777U7QZLOP742XR3W35EYYWNHIV2P5TZQFECPOQW3TVMYGPNCSDXTPY",
    "Anon": "AnYNWXXXLTsuhyn5hmAQKaBY8dwbctVuzhx",
    "Aptos": "0x9416728d24b3d2d028d33eaa3e86ca44a1d3d5feaadcb24537587076736c472f",
    "Arbitrum": "0xCCAad7A87fd81553d0F93F743Fb4Fc6B213b228B",
    "Argoneum": "MNiFdGCrg1CaXxxWbRjjoxkTE8gtd5Zod2",
    "Artax": "AJw97vhnUxDcH1SKYKEgN777fG2Uf6EW21",
    "Aryacoin": "AcQpTsPCHGVfzRwkZCqGSbybogLMqpxC32",
    "Asiacoin": "AcF83LYjqc4Le56VxC4wiug52G8LPtjfaQ",
    "Auroracoin": "ARd5qZbxqCs9YX7mkxyhvYo6dfZdKBc6WG",
    "Avalanche": "P-avax1fc20p9ut0ulgmwgdne4hmy644w04x4gqgzd6kg",
    "Avian": "RReKmu325n3zq9tr8BHTNDJEq355xKCdoa",
    "Axe": "PCdPiKMsCuL1n1MPXycb46b7vkAuHxL5xK",
    "Axelar": "axelar1m0aarljq5j5v2ckh2j7tu46fhw0kwzykqlzzxk",
    "Band-Protocol": "band1rl7nzmenxx8k9rtfne6869utnnsl329sl0n9hm",
    "Bata": "B8FpJGPTd5nKo91shfgecoNte8X7FfdFrH",
    "Beetle-Coin": "BaxHBGdQXhjmdgc7tNmuFGtcqPDvn7nDqh",
    "Bela-Coin": "BKxMHHq52rDze8MAyNSCSkgSSv1jtA6m6f",
    "Binance": "bnb1tl74zfr4z8h6g5r6hc6stnvhllkkrak8jy3l8d",
    "Bit-Cloud": "B9VthtAKmm9qMhSu4TJtkzwh2RCqJNNSuj",
    "Bitcoin": "12uaGVdX1t86FXLQ4yYPrRQDCK7xGGu82r",
    "Bitcoin-Atom": "AZFsfyNScGhQyjXvgZQNgKR6JezsTsCW1X",
    "Bitcoin-Cash": "1BHr4P4aQiDhtuKEda4GkJRaXfXtycRhzU",
    "Bitcoin-Cash-SLP": "1BHr4P4aQiDhtuKEda4GkJRaXfXtycRhzU",
    "Bitcoin-Gold": "GQzYF5Nq71wDYv5G9cHPazCUL8Dx5XQ8PY",
    "Bitcoin-Green": "GUgpMmLcetx845xcHkcabzzAXrnTMhmGhL",
    "Bitcoin-Plus": "B6Sxmzq2PwCcSUr12GReoAXQj5QpyCRkpC",
    "Bitcoin-Private": "b1SKxc4cpfRcz9VeWriKJTDWrKyg2fDN57L",
    "Bitcoin-SV": "163A17p7BkXncfe1yT5VvfsgRgveEugCP7",
    "BitcoinZ": "t1MZpCG1a1UhSMe9gxcSF6MfvAdLxAoASyE",
    "Bitcore": "2Hy1LkYxcuza17wy13ds9aKD6x7TBwi23d",
    "Bit-Send": "iC65d6WigKhNh1aLSZgtgN16zP7xUnaZwx",
    "Blackcoin": "B9UWvykBN73qDMhrK3nkezV91ZERKjVML2",
    "Blocknode": "BEhsjgoJZNJg4LNozmpnXMohASfZx5vYdr",
    "Block-Stamp": "1DRuHzcHHt3V8gj6TihFrZ2XjvWm4MGAeB",
    "Bolivarcoin": "bZRwytXk9D71NywwbYBvm9xqS3ZhS8Bbbc",
    "Brit-Coin": "BCVHsGwA6zbSeZdJAQCzfTkRA27Y9pPcuB",
    "Canada-eCoin": "Cc74bMN7nUPWodKsC3QmmssCTnD5aKAnjH",
    "Cannacoin": "CQKBuxTYbqVwCHYkF5AghtRvJZqgtYdN7H",
    "Cardano": "addr1q9p26pmu30s7ve2l6542eqtg05gyw64z02f49xmgecnh33ljrma797q8k3hpum3vs0ed5359wyeacjew6y9pl9vaa7rqh0zr0d",
    "Celo": "0x7ea4552Dd7e4B97ccd1E3DD08001005C0ce1C2B2",
    "Chihuahua": "chihuahua1m0aarljq5j5v2ckh2j7tu46fhw0kwzyk8yeyv4",
    "Clams": "xAsD6gkJEQkuXsDX7KEo4FQFyYhLPPyCcy",
    "Club-Coin": "CPqt3BmZ7oEuevuhzocUxqS6RVDV1jqw2X",
    "Compcoin": "CGd9h6TrXoJY61u9mUgsbHpwxbzoaHcVqr",
    "Cosmos": "cosmos1m0aarljq5j5v2ckh2j7tu46fhw0kwzyky352dh",
    "CPU-Chain": "CYSs7kGurTmBGM2swiaTsmoFd3X5ocwBMo",
    "Crane-Pay": "CTm9A2sPtroQuSDabExfFL49Pof4VUKzGT",
    "Crave": "VHCM4gbQ5Xj1xsCHmiFLnXeqzzCGS6pcvX",
    "Dash": "XnjbeXDU9tFTZGQnfoAXYXBp1EXVHQTLLL",
    "DeepOnion": "DoqTTxuorEh2VvfKWhYzH3U2UpDP3Ca7qj",
    "Defcoin": "DAM9BDNbSENX75AVhGh5ncTjXBTYLT5fRg",
    "Denarius": "DBwdw5i7cEGAer71znjbGRSNBGL3ir23A7",
    "Diamond": "dH7e3s1qCW4bVH9ig7HfDfVtwBrEH377mn",
    "Digi-Byte": "DD8ze546cLj77yz3o6mHxnACNw2ivXMwKB",
    "Digitalcoin": "DH6j8fgXXZD8w1tMDY3vhEe21X8MtDpadi",
    "Divi": "DLvkZHKmg61ebvQYsFkvL5VqANfpXXSjBJ",
    "Dogecoin": "DEUwb942N13LQucv1zZrPdHSkkvkfc25HV",
    "eCash": "1BHr4P4aQiDhtuKEda4GkJRaXfXtycRhzU",
    "E-coin": "e5QqGAudMQUXoZFXakkx31vAEXdSgKTeL5",
    "EDR-Coin": "eUs2PANaLrTyjPZRCpx5tbMNbMkE6DXZR8",
    "e-Gulden": "LdirznhnW7BwQHF3Az4SVZ77s614x9rtZy",
    "Einsteinium": "EQDkacHYVwZqE2Qht1iZnrFB3c7pa4yTJh",
    "Elastos": "EKNWLoc2pnSNCBL8ByScbEEbmJowcG4viz",
    "Energi": "EJjcsHZJYRCLP95dbzSZdJEoTioiZAygka",
    "EOS": "EOS742k13yyGTCAX3iM5tHiiSGcBfc63jiaoM9oDLYcuDm8kjoYb3",
    "Ergo": "9fD1WdtoUbUbcg3N8mqvX21g7DpTBhzmA1xdKqWMStnhmmeJGEE",
    "Ethereum": "0xCCAad7A87fd81553d0F93F743Fb4Fc6B213b228B",
    "Europe-Coin": "ESnuz1zZUZSVxS8TYFyJ4zHygHjBvwBC75",
    "Evrmore": "EKabzH7nXKVhL2NSnXgvFTVBQtUVGp9n4E",
    "Exclusive-Coin": "ETgRPLnRGnfMLNeHeKhsuPj59Zd6tbJM8o",
    "Fantom": "0xCCAad7A87fd81553d0F93F743Fb4Fc6B213b228B",
    "Feathercoin": "6re88dnSSyyirfqYsXU8zk1S1gdzb3q5gS",
    "Fetch.ai": "fetch1m0aarljq5j5v2ckh2j7tu46fhw0kwzykhvaw0q",
    "Filecoin": "f1f7ems3sg4z5qfgcjmd4hb2tkunazkpf2r2cd2py",
    "Firo": "a2JWJarpYf9iEsVi9aepn7NNKYpVHaFX5f",
    "Firstcoin": "F7mkuAQN5Ginwvvn2TA3aQzX2yT9b5eDwB",
    "FIX": "FFJgKDh7P5Fr4oJfJfWP7LekudMp8LMbDc",
    "Flashcoin": "UiavX7N37sJCmGXgDSihajUM7Gn7PWz2bK",
    "Flux": "t1fgLFm51CJ6PG9t3oTmpEHGsz9KpZmb8FD",
    "Foxdcoin": "F8FoxViMwgRSxtecqNMZDi2kftzNeYs34M",
    "Fuji-Coin": "FXjc9htG2bLrYmcBLz3TTwtUQiDECGpLsj",
    "Game-Credits": "GMFNrY9ZUvKH88sbFmqNsag46G8bzR6LHa",
    "GCR-Coin": "GQvTV41Tvm2rAmDoVDUTN1UBcFdwKQ1MqU",
    "Go-Byte": "GPtwoYAzqd117xGqMGoqKVekA9sD3zQnXT",
    "Gridcoin": "S2KNtHammeAAKybeW6exCYF5XvtZ1dUB9x",
    "Groestl-Coin": "FXbFyEnqWAw6nXVB3SvZa6bGFMnfxed3SM",
    "Gulden": "GNxqrf4X5mP56MGsNVj8dUFXpns4biavJL",
    "Harmony": "one1v5m8h9w0584fzsvxtgyfccwctar6nvm05k2thd",
    "Helleniccoin": "LPqFUtNTVSYRHr1cAam4BJpGp1qZ7Bq6pU",
    "Hempcoin": "HHmdaG5odswVdBpcaTRvvM6PudicaFUWQR",
    "Horizen": "zne2bQkghaGtKaGByKQpKyMFeDVQSPePdxc",
    "Huobi-Token": "0x7F756c263B2Ce8804a4C3561B22E4Cb1B2F18574",
    "Hush": "t1UTutZc2ECMBYfY2afep1oE5hFvd4r5iHp",
    "Icon": "hx2cd29b3dcd9860628b832258f128f500a3ef571c",
    "Injective": "inj1ej4d02rlmq24858e8a6rld8udvsnkg5tqxdxkh",
    "InsaneCoin": "iD4m3CuqdpnENJT83S3cxuhCaYSnosHZrM",
    "Internet-Of-People": "pK5HNomFqBnuUpdnFmP4D7YGqrQHXgfz9t",
    "IRISnet": "iaa13v6yfqhya3el2nuurc7v8dxjqd5zfu0fl372ev",
    "IX-Coin": "xtBJ1xY3giBzvYZXxKv1vwFkyX76JZhPWT",
    "Jumbucks": "Je4mmJQaknBL5nn55fw7W77abNquJNZZdf",
    "Kava": "kava18ex67n3jh3z37n2c5w6znx0xq7s00v4s990yxr",
    "Kobocoin": "FQvJdVuiVNDqVFzwA9Cp2owtmAvriuYNjx",
    "Komodo": "R9khp8yYMYvYJ2Aw7MPcfPi8mxXyUcZGMy",
    "Landcoin": "LUduHrEBCSHKjezVj96nDcATUYBT4Nu8Mn",
    "LBRY-Credits": "bbGXkDPTFvaG8FhoDxFHDbxYVgo8KXQVp8",
    "Linx": "XNAUBjTKK7C5j9o4Ukvtzt5XEB7UrtahfM",
    "Litecoin": "LKimr5icapPsVY8yQs71nijRufmQL9wbkp",
    "Litecoin-Cash": "Ceg1kLJX1wLQuevJ1zJ7w4uHojETcWtp1Y",
    "LitecoinZ": "L1MhAZU4XzAQeu2VQFa56g355AdHGVWi3wv",
    "Lkrcoin": "LcBCuUQy8nosjwDVncFQ3FRArWq8TtMTrV",
    "Lynx": "KFvuuMH8r8Hyjz4pbq88cod6TTePESLBRT",
    "Mazacoin": "MQYEMxGjvnmRUPJMmBhreAsdCfwYG1BMwr",
    "Megacoin": "MBFEqhAkYNcgTib1uBuFKGYd6p5FkQNY6j",
    "Metis": "0xCCAad7A87fd81553d0F93F743Fb4Fc6B213b228B",
    "Minexcoin": "XH4z5cJi5tqdskWT9UVMfQRbZKt2Rz3mvG",
    "Monacoin": "MHLsJWGpFxoQSqecjBjLxhpfHNAzmDohWs",
    "Monk": "MeBZGrVkCEnTpm4vSJe3sS8FVme9FX3x5e",
    "MultiversX": "erd189twxfn6s36c0yn0zxrwcfwmt9vyc77v4hc2c4l8fwc8cpczdk3q82ru87",
    "Myriadcoin": "MNMryFNdEGQN7nAJXkEb9TGzhqzWXEvv4b",
    "Namecoin": "NHp7uJFCeAipuTYAFkDjDSXafe85tw2wBh",
    "Nano": "nano_3uuu6xokkqfppwpq5qetdi8nkhc3e7edqq4rbfr34kgrw9misgrpidpjmaug",
    "Navcoin": "NMCFDvx6A5DwW7PuegWjTWUkndePp8zM32",
    "Near": "b07659c07d4d8a8e27c4eeda234742e9a7cd8e0d28f78259dfb578c09027741a",
    "Neblio": "NQ7sd1WTvMEAFjtbMchUCSiVX9pvoro1wK",
    "Neo": "AXQLZi4scbKiH1NPCseAfp5AnPhxeg6wa8",
    "Neoscoin": "NhsjUVb5NCY2WTzEEMB1jA4TR9D2m1zQVi",
    "Neurocoin": "NiBsypBBCicNHqLoaNZNBL3nUXge9STby1",
    "New-York-Coin": "RUrcmKhgzDCUghgs43pQaDGBGPefG1FDjg",
    "Nine-Chronicles": "0xD9Be52F327C7cbcCc0179E60a37DAAbEa02720a5",
    "NIX": "Gex9tnPdzmbD5KcACyp9dP1FzioaoZ5BkZ",
    "Novacoin": "4RsqojAr6Keou2XDwrucd6YzRADcJ6osRs",
    "NuBits": "B6ucZcryzxCGXyjamA17phXNrgTY1nsvhV",
    "NuShares": "SiwjK2RCQeLF6XC34UFdPRkMaAfh87dzxf",
    "Monero": "46WMwRTfZb5QYrGPws8mxMVbpJCV1ikZS7GfjhRFexPS72HMMRT9HcqZsbCqou2tWjCWyd4nLAX83ZfbBhB5HUK3LHAcdpu",
    "OK-Cash": "PRzTXZBSzMBQu1GPAvaPj4H47D8pQZNjrp",
    "OKT-Chain": "ex1rsxp4xr4qxr0q7sw6jxfnttwdhzdwkdr9etgzl",
    "Omni": "1Q652y198i1fs7RJBbhwGiAeYbFaswcoEn",
    "Onix": "XUPQ57EzAoJr7dRDmziqMWFnQycC1WthLT",
    "Ontology": "AMkfEM2MWyrHSTcRaSC2QCbLXpWBCpQouD",
    "Optimism": "0xCCAad7A87fd81553d0F93F743Fb4Fc6B213b228B",
    "Osmosis": "osmo1m0aarljq5j5v2ckh2j7tu46fhw0kwzykv286m9",
    "Particl": "PumXnDMs5n6v5KHSTncLk9TYmYBzJaGEvW",
    "Peercoin": "PMk3XyLyKXWgjzWr9UEZPgNDoxcmyX93ru",
    "Pesobit": "P8uYGPZrvMHBBeyiKQYcN385v3zyTN6Gke",
    "Phore": "PVCpTRE3d4XgCAqiKVra3ZsXwJWfuPryZP",
    "Pi-Network": "GCZ335XVHH6NNJ6EJ6PA3SDWUR2WU66KJ56PPJ4V52RXHW2P6X6BO6GQ",
    "Pinkcoin": "2YcnvrJwE72M1L3GMYES4yEtPPZYYH2fp5",
    "Pivx": "DN52MjCSGRiuvpuQquv6xVTsZooSE15GoW",
    "Polygon": "0xCCAad7A87fd81553d0F93F743Fb4Fc6B213b228B",
    "PoSW-Coin": "P8mg5zVKgtmS8aiYcu8jApatmWDsyM2Hqi",
    "Potcoin": "PUbPdibJN6TaWPossZK2KCkBEzPRtUy2Wc",
    "Project-Coin": "PALUmGo1nE5FpWuY8SwBeSJHoNdZSZjbvX",
    "Putincoin": "PAUzXjTFqHPu3TkZDnqHcgiXpTirAZyUMn",
    "Qtum": "QNg3ifH9QBXW2DBpyBWnLmPcs1Bt5D2vho",
    "Rapids": "RcZFw6yMHZj1hqDNg6Ni6XGuvQh3ZSoaww",
    "Ravencoin": "RBhtaDAZhC1MQj8nSrgXLqqRQWRxXSivbh",
    "Reddcoin": "RjEihMthNqQKRn6JMGSisiJJJSvdjWxHvk",
    "Ripple": "141ymkx8W51iWv8Gm673VFqf2umMosJSRf",
    "Ritocoin": "BHproEPVgGr6Jd2LHmj5fQaAC5cWevRtZY",
    "RSK": "1K8Xq1WoVepZSjKmzrB7H8WHDF7pgq8H3S",
    "Rubycoin": "RBisueXJPTHeXd9rkddaPJCE5iysWSuUKV",
    "Safecoin": "RwFEYuh2hwret6fXML7B8bExvCBczDxxfJ",
    "Saluscoin": "SaTW9UMJzpipkSUrTdWLKcdwqFnD5K4532",
    "Scribe": "RHUGRKo1dGufnLfyajJn7mm3pjaHk7fq7Z",
    "Secret": "secret1h0dxphjshc4j7pw6zd0ejyfmqp9c3y02nu6rm6",
    "Shadow-Cash": "ShURwxUxosuDoGARnqaS5nw9fmumj9GHtS",
    "Shentu": "certik1m0aarljq5j5v2ckh2j7tu46fhw0kwzykregavu",
    "Slimcoin": "SWhx4UhVr9EU1A5o6S6ZVVFFv73bhn7xv8",
    "Smileycoin": "BCYVkFBqrjMioy4X49sTwsLJJBuYJfqQRA",
    "Solana": "HGQ2YPa7a64WPYjRyqYxUte9hzuLdbX48GNLGdQ8FdZ7",
    "Solarcoin": "8P3ZbeHk4TEREgKpabi4z5qhcR6kjvZzvq",
    "Stafi": "stafi1280afcn35za6qwdwd6f93qf8y9zqc0tl8mgd9h",
    "Stash": "XayLTKNDhPEEtSSdFHV9LaGedZzGZB57wq",
    "Stellar": "SCOT2QQHH63JEEX6EVAHBX2N5O5MNML7CCKMNAZXWMEZIJWWENHVRC6Q",
    "Stratis": "SZfX3xrkqpTDQX23qEDTgLYKkPseLaxhJ1",
    "Sugarchain": "SRPbS4WCktQs2ofVymGkCsh4cKcnrVuGBY",
    "Sui": "0x26ca94f221ff4b5c1b27cee4044657364768e034a596536879948014f4f70a38",
    "Syscoin": "SNTp8ewdjFBb82W7aK1pRgxziygmpLW7r6",
    "Terra": "terra10pa43d9ykwh0x3c9l8cxs6xvecwkvntn43hdwj",
    "Tezos": "tz1cajkTWrVvvnng1ejcNEazwjN72yFyJpix",
    "Theta": "0x2882bBD20166161E2b092E14A091b57586d89027",
    "Thought-AI": "45Eq8Zt3zDMRg13qgFwUTRJ6RWkF3AgiS2",
    "TOA-Coin": "TAU74bYVm5UyuVJz1XQMEJfcDpqTXLyomv",
    "Tron": "TGpEdw5tWQTCBbXe6CiChB1s94ghAMmuD1",
    "TWINS": "Wjhoga6oCPLY8Cm8ThrxkroQWLuFzdGiP8",
    "Ultimate-Secure-Cash": "UbBHF6WszhoCgadtDeTdar7d1Cx9WLhgqu",
    "Unobtanium": "uh7R28J72FCxC4U6VdxjVib1Ugqeqp8emU",
    "Vcash": "VfJF9GavqEyqJkjCZJi5xsj4q5Aid6DTUf",
    "VeChain": "0x4985d58628482a4C0BAcB0d0618E3dD81F8a96B9",
    "Verge": "DLVJdco9VzA8fCkNYW1AybcVS8SRCGq5cX",
    "Vertcoin": "VmVLwSWmxxUthhyyezmyYd949w1MtaAbHZ",
    "Viacoin": "VnHuk2be8cwoRcVqvSpD3KCMNC5iLp84Qw",
    "Vivo": "VWWHgWk36uzWzF89rvrWx2f7bmiieDpHif",
    "Voxels": "VFsUbM2D1u8ZJbMJJYr8QfW7tUEp4SN8pb",
    "Virtual-Cash": "Vh5NnSEDQEGwKzeYWxSTNBtVQnNuXj3veS",
    "Wagerr": "WQac9RPYr3x3xAWirbrfFaGe98vpCxdAB5",
    "Whitecoin": "WjedPnBjGgn5ntAf21wABah4fQzfDu51Mh",
    "Wincoin": "WhJFWk7hES9WXHMPdX1Hnb7tBMBo8ywRn2",
    "XinFin": "xdc90c26ae3A43df10cEB34030303Cb087F05cA7a20",
    "XUEZ": "XZDdLLMTibK9nAWFmRMrHenfXErqxH6Jfn",
    "Ycash": "s1cLHyNENwtDw3pb9EPfxWSnQMwwfrzep4v",
    "Zcash": "t1XsNG9c812S4eksmWGFS4vAEi3BAJCpDif",
    "ZClassic": "t1TgLUgQBtb3jAW3TLgQJSQNFBWenvvi4yA",
    "Zetacoin": "ZMzfCCukxrLGGuvHgw9CYkv26GcDp7uJgu",
    "Zilliqa": "zil1fly3avnhgpaj755wtjg7pkzex7080ec2thmupc",
    "ZooBC": "16rW592zpVDbQkVatMHCvhv9Lo38XTBusX"
}

class ClickableFrame(QFrame):
    clicked = Signal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

class Donation(QFrame):
    def __init__(self, *args, **kwargs):
        super(Donation, self).__init__(*args, **kwargs)
        QVBoxLayout(self)

        self.ui = None
        self.margin = 15
        self.width = 465
        self.height = 565

        self.overlay_frame = ClickableFrame(self.parent())
        self.overlay_frame.setStyleSheet("background-color: rgba(0, 0, 0, 128);")
        self.overlay_frame.clicked.connect(self.close)

        self.modal_parent_frame = self.parent().findChild(QFrame, "hdWalletContainerQFrame")
        self.modal_parent_frame.installEventFilter(self)

        self.setObjectName("modalQFrame")

    def re_adjust(self):
        parent_rect = self.parent().rect()
        geo = self.modal_parent_frame.geometry()
        geo.setHeight(geo.height())

        x_pos = geo.width() / 2 - self.width / 2
        y_pos = geo.height() / 2 - self.height / 2
        self.setGeometry(x_pos, y_pos, self.width, self.height)

        self.overlay_frame.setGeometry(0, 0, geo.width(), geo.height())

    def eventFilter(self, obj, event):
        if (event.type() == QEvent.Resize):
            self.re_adjust()
        return super().eventFilter(obj, event)

    def show(self):
        self.overlay_frame.show()
        self.raise_()
        super().show()

    def closeEvent(self, event):
        self.overlay_frame.deleteLater()
        self.deleteLater()

    def update_receive_qr(self, qr_label, text):
        qr_label.setText(None)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="white",
            back_color="#191e24"
        )

        qimage = ImageQt(img)

        pixmap = QPixmap.fromImage(qimage)

        qr_label.setPixmap(pixmap)
        qr_label.setAlignment(Qt.AlignCenter)
        qr_label.setScaledContents(True)


    def __update_btns(self):
        self.ui.donationsCharityQPushButton.setStyleSheet(
            self.ui.donationsCharityQPushButton.styleSheet()
        )
        self.ui.donationsCoreTeamQPushButton.setStyleSheet(
            self.ui.donationsCoreTeamQPushButton.styleSheet()
        )


    def show_charity(self): 
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.donationsCharityQPushButton.setProperty("Active", "true")
        self.ui.donationsCoreTeamQPushButton.setProperty("Active", "")
        self.__update_btns()

    def show_core(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.donationsCharityQPushButton.setProperty("Active", "")
        self.ui.donationsCoreTeamQPushButton.setProperty("Active", "true")
        self.__update_btns()
        
    def core_crypto_changed(self):
        crypto = self.ui.donationsCryptocurrencyQComboBox.currentText()
        addr = crypt_addresses[crypto]

        self.ui.donationsAddressQLabel.setText(f"{addr[:15]}...{addr[-10:]}")
        self.update_receive_qr(self.ui.donationsQRCodeQLabel, addr)

    def charity_crypto_changed(self):
        crypto = self.ui.donationsCharityCryptocurrencyQComboBox.currentText()
        addr = crypt_addresses[crypto]

        self.ui.donationsCharityAddressQLabel.setText(f"{addr[:15]}...{addr[-10:]}")
        self.update_receive_qr(self.ui.donationsCharityQRCodeQLabel, addr)


    @staticmethod
    def show_donation(main_window):
        frame = Donation(main_window)
    
        main_widget = QWidget()
        main_widget.setContentsMargins(0, 0, 0, 0)
        donation_ui = Ui_Form()
        donation_ui.setupUi(main_widget)
        frame.ui = donation_ui

        donation_ui.closeDonationsQPushButton.clicked.connect(frame.close)

        donation_ui.donationsCoreTeamQPushButton.clicked.connect(frame.show_core)
        donation_ui.donationsCharityQPushButton.clicked.connect(frame.show_charity)

        donation_ui.donationsCryptocurrencyQComboBox.addItems(sorted(crypt_addresses.keys()))
        donation_ui.donationsCryptocurrencyQComboBox.currentIndexChanged.connect(frame.core_crypto_changed)
        donation_ui.donationsCryptocurrencyQComboBox.setCurrentText("Ethereum")

        donation_ui.donationsCharityCryptocurrencyQComboBox.addItems(["Bitcoin", "Ethereum"])
        donation_ui.donationsCharityCryptocurrencyQComboBox.currentIndexChanged.connect(frame.charity_crypto_changed)
        donation_ui.donationsCharityCryptocurrencyQComboBox.setCurrentText("Ethereum")

        donation_ui.donationsCoreTeamQPushButton.click()
        donation_ui.donationsCharityCaptionQLabel.setText("This donation is for the charity team, because without "
                                                          "them, we'd have no idea where our good intentions should "
                                                          "go. Cheers to our chaos coordinators! ")
        donation_ui.donationsCaptionQLabel.setText("This donation is for the core team, because without them, we'd be "
                                                   "googling 'how to turn on a computer.' Cheers to our tech wizards!")
        donation_ui.donationsCaptionQLabel.setWordWrap(True)
        donation_ui.donationsCharityCaptionQLabel.setWordWrap(True)

        donation_ui.donationsAddressCopyQPushButton.clicked.connect(
            lambda: copy_to_clipboard(donation_ui.donationsAddressQLabel.text())
        )
        donation_ui.donationsCharityAddressCopyQPushButton.clicked.connect(
            lambda: copy_to_clipboard(donation_ui.donationsCharityAddressQLabel.text())
        )



        frame.layout().addWidget(main_widget)
        frame.re_adjust()
        frame.show()