

# دیکشنری برای تبدیل کلمات کلیدی
keyword_mapping = {
    "ba":"with",
    "darhalike":"while",
    "talash":"try",
    "bargasht":"return",
    "khali":"pass",
    "ya":"or",
    "nabodan":"not",
    "ast":"is",
    "dar":"in",
    "vared":"import",
    "agar":"if",
    "jahani":"global",
    "az":"from",
    "baraye":"for",
    "saranjam":"finally",
    "khatadad":"except",
    "gheyre":"else",
    "vagheyre":"elif",
    "hazf":"del",
    "tabe":"def",
    "edame":"continue",
    "kelas":"class",
    "tavaghof":"break",
    "beonvane":"as",
    "va":"and",
    "dorost":"True",
    "hichi":"None",
    "ghalat":"False",
    "barresishart":"assert",
    "tabebinam":"lambda",
    "gharibe":"nonlocal",
    "estesnayedasty":"raise",
    "tolidkonande":"yield",
    "chap":"print",
}

# تابعی برای تبدیل کد به پایتون
def convert_code(code):
    for key, value in keyword_mapping.items():
        code = code.replace(key, value)
    return code

# تابعی برای اجرا کردن کد
def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        print(f"khata: {e}")

# ورودی از کاربر
user_code = """
tabe greet(name):
    agar name:
        chap("salam"+" "+ name) 
    gheyre:
        chap("khodahafez ...")

greet("ali")
"""

# تبدیل و اجرا
python_code = convert_code(user_code)
execute_code(python_code)

