# -*- coding: utf-8 -*-
# Esolang compiler or something

# read the input file (extension is '.me')

import sys

filename = sys.argv[1]

f = open(filename + '.me', 'r', encoding = 'utf-8')

code = f.read()

# dictionary of words to be swapped

swap = {
    'vibe' : 'print',
    '✨' : 'print',
    'poggers' : 'print',
    'Tralalelo Tralala' : 'print',
    'Bim Bum Bam' : 'print',
    
    'mood' : '',
    '➡️' : '=',
    'Crocodildo Penisini' : '=',
    
    'chickenStars' : 'def',
    'yeet' : 'return',
    'frigo camello' : 'def',
    'frulli frulla' : 'return',
    'troll' : 'lambda',
    'El szczurito kurwito golfito' : 'lambda',
    
    'sus?' : 'if',
    'cap?' : 'else',
    'bigcap?' : 'elif',
    '@heretic' : 'if',
    'wtf' : 'else',
    'seOH' : 'elif',
    'Tracotocutulo Lirilì Larilà' : 'if',
    
    'Fuck' : 'for',
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
    
    'noCapTry' : 'try',
    'capCatch' : 'except',
    'rip' : 'raise',
    'ADL' : 'raise',
    'oil' : 'pass',
    'Trulimero Trulicina' : 'try',
    'Bobrini Cocosini' : 'except',
    'Brr brr Patapim' : 'raise',
    'Sahur Puasa tapi tidak sholat 5 waktu' : 'pass',
    
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
    
    'hpock' : 'import',
    'tysob' : 'from',
    'blorgia' : 'as',
    'Beduk dug dug' : 'import',
    'Pat pat ketupat' : 'from',
    'Polisi sok asik' : 'as',
    
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
    
    'touhou' : 'chr',
    'osu' : 'map',
    'rshig' : 'zip',
    'racism' : 'type',
    'dong' : 'len',
    'cock' : 'run',
    
    'chungus' : 'async',
    'sus' : 'await',
    
    'doge' : 'finally',
    'Ele_' : 'None',
    'cumburger' : '[]',
    'eburger' : '\'\'',
    'shart' : 'message',
    'sprite' : 'event',
    
    'cheugy' : 'False',
    'mainCharacter' : 'True',
    'ratio' : 'int',
    'noCap' : 'True',
    'cap' : 'False',
    'simp' : 'int',
    'susLevel' : 'int',
    'bruh' : 'pass',
    
    'Tung Tung Tung Sahur' : 'raise',
    'Brrr Brrr Brrr' : 'break',
    'Paff Paff' : 'continue',
    'El Bobrito de Kurvito' : 'yield',
    'El szczurito kurwito golfito' : 'lambda',
    'Bombinarium' : 'global',
    'Nerpinarium' : 'nonlocal',
}

new = code

for item in swap: new = new.replace(item, swap[item])

# now we just have regular python code

exec('# -*- coding: utf-8 -*-\n' + new)




            
            
  
