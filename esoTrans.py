# -*- coding: utf-8 -*-
# Gen Z++ / TikTok / Italian Brainrot transpiler

import sys

filename = sys.argv[1]

# read the input .py file
with open(filename + '.py', 'r', encoding='utf-8') as f:
    code = f.read()

# full mega dictionary
swap = {
    # Output / Print
    'vibe' : 'print',
    '✨' : 'print',
    'poggers' : 'print',
    'Tralalelo Tralala' : 'print',
    'Bim Bum Bam' : 'print',

    # Variables / Assignment
    'mood' : '',
    '➡️' : '=',
    'Crocodildo Penisini' : '=',

    # Functions / Lambda
    'chickenStars' : 'def',
    'yeet' : 'return',
    'Frigo Camello' : 'def',
    'Frulli Frulla' : 'return',
    'troll' : 'lambda',
    'El szczurito kurwito golfito' : 'lambda',

    # Conditionals
    'sus?' : 'if',
    'cap?' : 'else',
    'bigcap?' : 'elif',
    '@heretic' : 'if',
    'wtf' : 'else',
    'seOH' : 'elif',
    'Tracotocutulo Lirilì Larilà' : 'if',

    # Loops
    'again' : 'for',
    'vibin' : 'while',
    'pogContinue' : 'continue',
    'bruhStop' : 'break',
    'gamming' : 'for',
    'economy' : 'while',
    'clobbong' : 'continue',
    'clong' : 'break',
    'Trippi Troppi' : 'for',
    'Burbaloni Luliloli' : 'while',
    'Bombardino coccodrillo' : 'break',
    'Bombombini Gusini' : 'continue',

    # Error Handling
    'noCapTry' : 'try',
    'capCatch' : 'except',
    'rip' : 'raise',
    'ADL' : 'raise',
    'oil' : 'pass',
    'Trulimero Trulicina' : 'try',
    'Bobrini Cocosini' : 'except',
    'Brr brr Patapim' : 'raise',
    'Sahur Puasa tapi tidak sholat 5 waktu' : 'pass',

    # Boolean / Logic
    'based' : 'True',
    'cringe' : 'False',
    'dead' : 'None',
    'anim' : '==',
    'notVibe' : '!=',
    'unfunwaa' : '<',
    'funwaa' : '>',
    'strikesy' : '<=',
    'tero' : '>=',
    'xon' : 'and',
    'detecotb' : 'or',
    'zenzi' : 'not',
    'fuck' : 'is',
    'Giraffa Celeste' : 'True',
    'Cappuccino Assassino' : 'False',
    'La vaca saturno saturnita' : 'None',

    # Data Types / Collections
    '67' : 'int',
    '69' : 'int',
    '420' : 'int',
    '9000' : 'int',
    'vibefloat' : 'float',
    'chat' : 'str',
    'vibinState' : 'bool',
    'squad' : 'list',
    'balls' : 'list',
    'duo' : 'tuple',
    'dino' : 'tuple',
    'server' : 'dict',
    'blacksheets' : 'dict',
    'reimu' : 'set',
    'Boneca Ambalabu' : 'set',
    'Karpet masjid' : 'list',
    'Monyet pura pura puasa' : 'dict',
    'Pengajak Mokel' : 'tuple',

    # Input / Builtins
    'typeChat' : 'input',
    'cirno' : 'input',
    'Mic Sahur' : 'input',
    'ping()' : 'ping()',
    'DM()' : 'DM()',
    'ban' : 'del',
    'Bobritto bandito' : 'del',
    'jeb' : 'open',
    'epyc' : 'file',
    'skeet' : 'split',
    'femboy' : 'join',
    'goof' : 'append',
    'Cik cik cikal cik' : 'join',
    'Hor Hor Hor Horeg' : 'split',
    'Tang tang tang bayar hutang kau' : 'len',

    # Modules / Imports
    'hpock' : 'import',
    'tysob' : 'from',
    'blorgia' : 'as',
    'Beduk dug dug' : 'import',
    'Pat pat ketupat' : 'from',
    'Polisi sok asik' : 'as',

    # Math Operators
    'sex' : '-',
    'yang' : '+',
    'Ambatron' : '*',
    'gec' : '%',
    'Glorbo Fruttodrillo' : '+',
    'Camelrino Tazzino' : '-',
    'mips' : 'round',
    'vig' : 'sum',
    'basedMax' : 'max',
    'cringeMin' : 'min',

    # Other Functions
    'touhou' : 'chr',
    'osu' : 'map',
    'rshig' : 'zip',
    'racism' : 'type',
    'dong' : 'len',
    'cock' : 'run',

    # Async / Await
    'chungus' : 'async',
    'sus' : 'await',

    # Emojis / Misc
    'doge' : 'finally',
    'Ele_' : 'None',
    'cumburger' : '[]',
    'eburger' : '\'\'',
    'shart' : 'message',
    'sprite' : 'event',

    # TikTok / Internet Slang
    'cheugy' : 'False',
    'mainCharacter' : 'True',
    'ratio' : 'int',
    'noCap' : 'True',
    'cap' : 'False',
    'simp' : 'int',
    'susLevel' : 'int',
    'bruh' : 'pass',

    # Italian / Brainrot / Meme
    'Tung Tung Tung Sahur' : 'raise',
    'Brrr Brrr Brrr' : 'break',
    'Paff Paff' : 'continue',
    'El Bobrito de Kurvito' : 'yield',
    'El szczurito kurwito golfito' : 'lambda',
    'Bombinarium' : 'global',
    'Nerpinarium' : 'nonlocal',
}

# replace Gen Z++ keywords with Python keywords
new_code = code
for key, value in swap.items():
    new_code = new_code.replace(key, value)

# write the transpiled code to a .me file
with open(filename + '.me', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n' + new_code)

print(f"[✅] Transpiled {filename}.py -> {filename}.me")
