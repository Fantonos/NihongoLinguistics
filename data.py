import genorate_prompt


'''
topics = ["Math", "Alphabet", "Colors", "Month", "Holidays"]

topics_fuctions = {
    "Colors": colors_prompt,
    "Holidays": holidays_prompt
}
'''

Colors = {
    "Red": ["Aka", "あか"],
    "Blue": ["Ao", "あお"],
    "Green": ["Midori", "みどり"],
    "Yellow": ["Kiiro", "きいろ"],
    "White": ["Shiro", "しろ"],
    "Black": ["Kuro", "くろ"],
    "Pink": ["Momoiro", "ももいろ"],
    "Purple": ["Murasaki", "むらさき"],
    "Orange": ["Daidaiiro", "だいだいいろ"],
    "Brown": ["Chairo", "ちゃいろ"],
    "Gray": ["Haiiro", "はいいろ"],
}


Months = {
    "1st": "January", 
    "2nd": "February", 
    "3rd": "March", 
    "4th": "April", 
    "5th": "May", 
    "6th": "June", 
    "7th": "July", 
    "8th": "August", 
    "9th": "September", 
    "10th": "October", 
    "11th": "November", 
    "12th": "December"
}


numbers_dict = {
    "0": ["REI", "れい"],
    "1": ["ICHI", "いち"],
    "2": ["NI", "に"],
    "3": ["SAN", "さん"],
    "4": ["YON", "し"],
    "5": ["GO", "ご"],
    "6": ["ROKU", "ろく"],
    "7": ["NANA", "なな"],
    "8": ["HACHI", "はち"],
    "9": ["KYUU", "きゅう"],
    "10": ["JUU", "じゅう"],
    "11": ["JUU-ICHI", "じゅういち"],
    "12": ["JUU-NI", "じゅうに"],
    "13": ["JUU-SAN", "じゅうさん"],
    "14": ["JUU-YON", "じゅうし"],
    "15": ["JUU-GO", "じゅうご"],
    "16": ["JUU-ROKU", "じゅうろく"],
    "17": ["JUU-NANA", "じゅうなな"],
    "18": ["JUU-HACHI", "じゅうはち"],
    "19": ["JUU-KYUU", "じゅうきゅう"],
    "20": ["NI-JUU", "にじゅう"],
    "21": ["NI-JUU-ICHI", "にじゅういち"],
    "22": ["NI-JUU-NI", "にじゅうに"],
    "23": ["NI-JUU-SAN", "にじゅうさん"],
    "24": ["NI-JUU-YON", "にじゅうし"],
    "25": ["NI-JUU-GO", "にじゅうご"],
    "26": ["NI-JUU-ROKU", "にじゅうろく"],
    "27": ["NI-JUU-NANA", "にじゅうなな"],
    "28": ["NI-JUU-HACHI", "にじゅうはち"],
    "29": ["NI-JUU-KYUU", "にじゅうきゅう"],
    "30": ["SAN-JUU", "さんじゅう"],
    "31": ["SAN-JUU-ICHI", "さんじゅういち"],
    "32": ["SAN-JUU-NI", "さんじゅうに"],
    "33": ["SAN-JUU-SAN", "さんじゅうさん"],
    "34": ["SAN-JUU-YON", "さんじゅうし"],
    "35": ["SAN-JUU-GO", "さんじゅうご"],
    "36": ["SAN-JUU-ROKU", "さんじゅうろく"],
    "37": ["SAN-JUU-NANA", "さんじゅうなな"],
    "38": ["SAN-JUU-HACHI", "さんじゅうはち"],
    "39": ["SAN-JUU-KYUU", "さんじゅうきゅう"],
    "40": ["YON-JUU", "よんじゅう"],
    "41": ["YON-JUU-ICHI", "よんじゅういち"],
    "42": ["YON-JUU-NI", "よんじゅうに"],
    "43": ["YON-JUU-SAN", "よんじゅうさん"],
    "44": ["YON-JUU-YON", "よんじゅうし"],
    "45": ["YON-JUU-GO", "よんじゅうご"],
    "46": ["YON-JUU-ROKU", "よんじゅうろく"],
    "47": ["YON-JUU-NANA", "よんじゅうなな"],
    "48": ["YON-JUU-HACHI", "よんじゅうはち"],
    "49": ["YON-JUU-KYUU", "よんじゅうきゅう"],
    "50": ["GO-JUU", "ごじゅう"]
}


h_alphabet = {
    "あ": "A",
    "い": "I",
    "う": "U",
    "え": "E",
    "お": "O",
    "か": "KA",
    "き": "KI",
    "く": "KU",
    "け": "KE",
    "こ": "KO",
    "さ": "SA",
    "し": "SHI",
    "す": "SU",
    "せ": "SE",
    "そ": "SO",
    "た": "TA",
    "ち": "CHI",
    "つ": "TSU",
    "て": "TE",
    "と": "TO",
    "な": "NA",
    "に": "NI",
    "ぬ": "NU",
    "ね": "NE",
    "の": "NO",
    "は": "HA",
    "ひ": "HI",
    "ふ": "FU",
    "へ": "HE",
    "ほ": "HO",
    "ま": "MA",
    "み": "MI",
    "む": "MU",
    "め": "ME",
    "も": "MO",
    "や": "YA",
    "ゆ": "YU",
    "よ": "YO",
    "ら": "RA",
    "り": "RI",
    "る": "RU",
    "れ": "RE",
    "ろ": "RO",
    "わ": "WA",
    "を": "WO",
    "ん": "N",
    # Dakuten (voiced) variants
    "が": "GA",
    "ぎ": "GI",
    "ぐ": "GU",
    "げ": "GE",
    "ご": "GO",
    "ざ": "ZA",
    "じ": "JI",
    "ず": "ZU",
    "ぜ": "ZE",
    "ぞ": "ZO",
    "だ": "DA",
    "ぢ": "JI",
    "づ": "ZU",
    "で": "DE",
    "ど": "DO",
    "ば": "BA",
    "び": "BI",
    "ぶ": "BU",
    "べ": "BE",
    "ぼ": "BO",
    # Handakuten (p-sound) variants
    "ぱ": "PA",
    "ぴ": "PI",
    "ぷ": "PU",
    "ぺ": "PE",
    "ぽ": "PO"
}
