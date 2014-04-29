#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# "Standard Abugida"

import sys, re

rtable = "[bcdfghjklmnpqrstvwxyz][aeiou]"

table0={"y": "i"}

table1={"ba": "β",
        "be": "[b]b[/b]",
        "bi": "[f]b[/f]",
        "bu": "[v]b[/v]",
        "by": "[f]b[/f]",
        "ca": "χ",
        "ce": "[b]c[/b]",
        "ci": "[f]c[/f]",
        "cu": "[v]c[/v]",
        "cy": "[f]c[/f]",
        "da": "δ",
        "de": "[b]d[/b]",
        "di": "[f]d[/f]",
        "du": "[v]d[/v]",
        "dy": "[f]d[/f]",
        "fa": "φ",
        "fe": "[b]f[/b]",
        "fi": "[f]f[/f]",
        "fu": "[v]f[/v]",
        "fy": "[f]f[/f]",
        "ga": "γ",
        "ge": "[b]g[/b]",
        "gi": "[f]g[/f]",
        "gu": "[v]g[/v]",
        "gy": "[f]g[/f]",
        "ha": "η",
        "he": "[b]h[/b]",
        "hi": "[f]h[/f]",
        "hu": "[v]h[/v]",
        "hy": "[f]h[/f]",
        "ja": "ϳ",
        "je": "[b]j[/b]",
        "ji": "[f]j[/f]",
        "ju": "[v]j[/v]",
        "jy": "[f]j[/f]",
        "ka": "κ",
        "ke": "[b]k[/b]",
        "ki": "[f]k[/f]",
        "ku": "[v]k[/v]",
        "ky": "[f]k[/f]",
        "la": "λ",
        "le": "[b]l[/b]",
        "li": "[f]l[/f]",
        "lu": "[v]l[/v]",
        "ly": "[f]l[/f]",
        "ma": "μ",
        "me": "[b]m[/b]",
        "mi": "[f]m[/f]",
        "mu": "[v]m[/v]",
        "my": "[f]m[/f]",
        "na": "ν",
        "ne": "[b]n[/b]",
        "ni": "[f]n[/f]",
        "nu": "[v]n[/v]",
        "ny": "[f]n[/f]",
        "pa": "π",
        "pe": "[b]p[/b]",
        "pi": "[f]p[/f]",
        "pu": "[v]p[/v]",
        "py": "[f]p[/f]",
        "qa": "ϟ",
        "qe": "[b]q[/b]",
        "qi": "[f]q[/f]",
        "qu": "[v]q[/v]",
        "qy": "[f]q[/f]",
        "ra": "ρ",
        "re": "[b]r[/b]",
        "ri": "[f]r[/f]",
        "ru": "[v]r[/v]",
        "ry": "[f]r[/f]",
        "sa": "σ",
        "se": "[b]s[/b]",
        "si": "[f]s[/f]",
        "su": "[v]s[/v]",
        "sy": "[f]s[/f]",
        "ta": "τ",
        "te": "[b]t[/b]",
        "ti": "[f]t[/f]",
        "tu": "[v]t[/v]",
        "ty": "[f]t[/f]",
        "va": "ϐ",
        "ve": "[b]v[/b]",
        "vi": "[f]v[/f]",
        "vu": "[v]v[/v]",
        "vy": "[f]v[/f]",
        "wa": "ω",
        "we": "[b]w[/b]",
        "wi": "[f]w[/f]",
        "wu": "[v]w[/v]",
        "wy": "[f]w[/f]",
        "xa": "ξ",
        "xe": "[b]x[/b]",
        "xi": "[f]x[/f]",
        "xu": "[v]x[/v]",
        "xy": "[f]x[/f]",
        "ya": "ψ",
        "ye": "[b]y[/b]",
        "yi": "[f]y[/f]",
        "yu": "[v]y[/v]",
        "yy": "[f]y[/f]",
        "za": "ζ",
        "ze": "[b]z[/b]",
        "zi": "[f]z[/f]",
        "zu": "[v]z[/v]",
        "zy": "[f]z[/f]"}

table2={"bo": "[s]b[/s]",
        "co": "[s]c[/s]",
        "do": "[s]d[/s]",
        "fo": "[s]f[/s]",
        "go": "[s]g[/s]",
        "ho": "[s]h[/s]",
        "jo": "[s]j[/s]",
        "ko": "[s]k[/s]",
        "lo": "[s]l[/s]",
        "mo": "[s]m[/s]",
        "no": "[s]n[/s]",
        "po": "[s]p[/s]",
        "qo": "[s]q[/s]",
        "ro": "[s]r[/s]",
        "so": "[s]s[/s]",
        "to": "[s]t[/s]",
        "vo": "[s]v[/s]",
        "wo": "[s]w[/s]",
        "xo": "[s]x[/s]",
        "yo": "[s]y[/s]",
        "zo": "[s]z[/s]"}

table3={"ab": "°β",
        "eb": "[b]°b[/b]",
        "ib": "[f]°b[/f]",
        "ub": "[v]°b[/v]",
        "yb": "[f]°b[/f]",
        "ac": "°χ",
        "ec": "[b]°c[/b]",
        "ic": "[f]°c[/f]",
        "uc": "[v]°c[/v]",
        "yc": "[f]°c[/f]",
        "ad": "°δ",
        "ed": "[b]°d[/b]",
        "id": "[f]°d[/f]",
        "ud": "[v]°d[/v]",
        "yd": "[f]°d[/f]",
        "af": "°φ",
        "ef": "[b]°f[/b]",
        "if": "[f]°f[/f]",
        "uf": "[v]°f[/v]",
        "yf": "[f]°f[/f]",
        "ag": "°γ",
        "eg": "[b]°g[/b]",
        "ig": "[f]°g[/f]",
        "ug": "[v]°g[/v]",
        "yg": "[f]°g[/f]",
        "ah": "°η",
        "eh": "[b]°h[/b]",
        "ih": "[f]°h[/f]",
        "uh": "[v]°h[/v]",
        "yh": "[f]°h[/f]",
        "aj": "°ϳ",
        "ej": "[b]°j[/b]",
        "ij": "[f]°j[/f]",
        "uj": "[v]°j[/v]",
        "yj": "[f]°j[/f]",
        "ak": "°κ",
        "ek": "[b]°k[/b]",
        "ik": "[f]°k[/f]",
        "uk": "[v]°k[/v]",
        "yk": "[f]°k[/f]",
        "al": "°λ",
        "el": "[b]°l[/b]",
        "il": "[f]°l[/f]",
        "ul": "[v]°l[/v]",
        "yl": "[f]°l[/f]",
        "am": "°μ",
        "em": "[b]°m[/b]",
        "im": "[f]°m[/f]",
        "um": "[v]°m[/v]",
        "ym": "[f]°m[/f]",
        "an": "°ν",
        "en": "[b]°n[/b]",
        "in": "[f]°n[/f]",
        "un": "[v]°n[/v]",
        "yn": "[f]°n[/f]",
        "ap": "°π",
        "ep": "[b]°p[/b]",
        "ip": "[f]°p[/f]",
        "up": "[v]°p[/v]",
        "yp": "[f]°p[/f]",
        "aq": "°ϟ",
        "eq": "[b]°q[/b]",
        "iq": "[f]°q[/f]",
        "uq": "[v]°q[/v]",
        "yq": "[f]°q[/f]",
        "ar": "°ρ",
        "er": "[b]°r[/b]",
        "ir": "[f]°r[/f]",
        "ur": "[v]°r[/v]",
        "yr": "[f]°r[/f]",
        "as": "°σ",
        "es": "[b]°s[/b]",
        "is": "[f]°s[/f]",
        "us": "[v]°s[/v]",
        "ys": "[f]°s[/f]",
        "at": "°τ",
        "et": "[b]°t[/b]",
        "it": "[f]°t[/f]",
        "ut": "[v]°t[/v]",
        "yt": "[f]°t[/f]",
        "av": "°ϐ",
        "ev": "[b]°v[/b]",
        "iv": "[f]°v[/f]",
        "uv": "[v]°v[/v]",
        "yv": "[f]°v[/f]",
        "aw": "°ω",
        "ew": "[b]°w[/b]",
        "iw": "[f]°w[/f]",
        "uw": "[v]°w[/v]",
        "yw": "[f]°w[/f]",
        "ax": "°ξ",
        "ex": "[b]°x[/b]",
        "ix": "[f]°x[/f]",
        "ux": "[v]°x[/v]",
        "yx": "[f]°x[/f]",
        "ay": "°ψ",
        "ey": "[b]°y[/b]",
        "iy": "[f]°y[/f]",
        "uy": "[v]°y[/v]",
        "yy": "[f]°y[/f]",
        "az": "°ζ",
        "ez": "[b]°z[/b]",
        "iz": "[f]°z[/f]",
        "uz": "[v]°z[/v]",
        "yz": "[f]°z[/f]"}

table4={"ob": "[s]°b[/s]",
        "oc": "[s]°c[/s]",
        "od": "[s]°d[/s]",
        "of": "[s]°f[/s]",
        "og": "[s]°g[/s]",
        "oh": "[s]°h[/s]",
        "oj": "[s]°j[/s]",
        "ok": "[s]°k[/s]",
        "ol": "[s]°l[/s]",
        "om": "[s]°m[/s]",
        "on": "[s]°n[/s]",
        "op": "[s]°p[/s]",
        "oq": "[s]°q[/s]",
        "or": "[s]°r[/s]",
        "os": "[s]°s[/s]",
        "ot": "[s]°t[/s]",
        "ov": "[s]°v[/s]",
        "ow": "[s]°w[/s]",
        "ox": "[s]°x[/s]",
        "oy": "[s]°y[/s]",
        "oz": "[s]°z[/s]"}

table5={"a": "α",
        "e": "ε",
        "i": "ι",
        "o": "ο",
        "u": "υ"}

table6={"[s]": "[strike]",
        "[/s]": "[/strike]",
        "[f]": "[i]",
        "[/f]": "[/i]",
        "[v]": "[u]",
        "[/v]": "[/u]"}

table7=["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

def decode(string, translate=False, html_mode=False):
    brf = []
    nstring = string.split()
    for lstring in nstring:
        for dic in (table0,table1,table2,table3,table4,table5,table6,table7):
            if type(dic) is list:
                for char in dic:
                    lstring = lstring.replace(char, "↑" + char.lower())
            else:
                for key in dic.keys():
                    r = dic[key]
                    if html_mode:
                        r = r.replace("[", "<").replace("]", ">")
                    if key in lstring:
                        lstring = lstring.replace(key, r)
                    if key.capitalize() in lstring:
                        if "[/" in r:
                            lstring = lstring.replace(key.capitalize(), r.replace("]", "]↑", 1))
                        else:
                            lstring = lstring.replace(key.capitalize(), "↑" + r)
        if html_mode:
            lstring = list(lstring)
            for i in range(0, len(lstring)):
                if not re.match("[1-9a-zA-Z\]\[/!?\"'.,()<>]", lstring[i]):
                    try: lstring[i] = "&#%s;" % (ord(lstring[i]),)
                    except: print(lstring[i])
            lstring = "".join(lstring)
        brf.append(lstring)
    return " ".join(brf) + ("\n[i]%s[/i]" % (string,) if translate else "")

def main(argv=[]):
    vinfo = tuple(str(x) for x in sys.version_info[:3])
    print("Standard Abugida Converter (Python %s)" % (".".join(vinfo),))
    print("Enter blank input for options...")
    x = " ".join(argv)
    options = {"translation": False, "HTML mode": False}
    if len(x) == 0:
        x = input("> ")
    while 1:
        if x == "":
            y = input("Options\n%s\n>>> " % ("\n".join([x[0][0] + ": " + ("Disable " if x[1] else "Enable ") + x[0] for x in options.items()])))
            changed = False
            for key in options.keys():
                if y.lower() == str(key)[0].lower():
                    options[key] = not options[key]
                    print("%s %s." % (key.capitalize(), "enabled" if options[key] else "disabled"))
                    changed = True
                    break
            if not changed:
                print("Nothing changed.")
        else:
            print(decode(x, options["translation"], options["HTML mode"]))
        x = input("> ")

if __name__ == "__main__":
    main(sys.argv[1::])
