#!/usr/bin/env python3
from tika import parser
import sys, os, re, string
from google_trans_new import google_translator

def main():
    if len(sys.argv) == 4:
        target_pdf = sys.argv[1]
        out_base = os.path.splitext(target_pdf)[0]
        src_lang = sys.argv[2]
        target_lang = sys.argv[3]
        pdf_content = parser.from_file(target_pdf)
        out_str = pdf_content['content']
        with open('{}_{}.txt'.format(out_base, src_lang), 'w+') as src_out:
            src_out.write(out_str)
        translated_sents = []
        with open('{}_{}.txt'.format(out_base, src_lang), 'r') as to_trans:
            trans_src = to_trans.readlines()
            try:
                for sentence in trans_src:
                    sentence = sentence.strip()
                    print(sentence)
                    translator = google_translator()
                    new_sent = translator.translate(sentence.translate(str.maketrans('','', string.punctuation)), lang_src=src_lang, lang_tgt=target_lang)
                    print(new_sent)
                    translated_sents.append(new_sent)
            except:
                print("sheeeeeiiiiiittttt")
        with open('{}_{}.txt'.format(out_base, target_lang), 'w+') as tgt_out:
            [tgt_out.write("{}\n".format(x)) for x in translated_sents]
    else:
        print("""You need to provide three arguments.

Usage:
\t./pdf_trans.sh file.pdf src-lang tgt-lang

Get your arguments in order and try again.
""")
if __name__ == '__main__':
	main()
